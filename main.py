import aiohttp
import discord
from discord.ext import commands
from discord.commands import Option, OptionChoice
from preprompts import preprompts
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve sensitive information from environment variables
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
DISCORD_SERVER_ID = int(os.getenv('DISCORD_SERVER_ID'))
LOCALHOST_URL = os.getenv('LOCALHOST_URL')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to simulate storing context
context_storage = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.slash_command(guild_ids=[DISCORD_SERVER_ID], description="Ask a question to the AI, starting with a preprompt.")
async def ask(ctx, preprompt: Option(str, "Choose a preprompt", choices=[OptionChoice(key, key) for key in preprompts.keys()]), question: str):
    await ctx.defer()
    preprompt_text = preprompts[preprompt]  # Fetch the full preprompt text based on the selected key
    prompt = f"{preprompt_text} {question}"  # Concatenate the full preprompt first, then the question
    user_id = str(ctx.author.id)

    # Retrieve the last context
    last_context = context_storage.get(user_id, None)

    async with aiohttp.ClientSession() as session:
        payload = {
            "model": "llama3:latest",
            "prompt": prompt,
            "stream": False,
            "context": last_context  # Include the last context if available
        }
        async with session.post(LOCALHOST_URL, json=payload) as resp:
            if resp.status == 200:
                data = await resp.json()
                response = data.get('response', 'No response from AI.')
                new_context = data.get('context')  # Fetch the new context from the response

                # Update the context in storage
                if new_context:
                    context_storage[user_id] = new_context

                # Split the response into chunks of 2000 characters or less
                response_chunks = [response[i:i + 2000] for i in range(0, len(response), 2000)]
                for chunk in response_chunks:
                    await ctx.followup.send(chunk)

# Run the bot
bot.run(DISCORD_BOT_TOKEN)