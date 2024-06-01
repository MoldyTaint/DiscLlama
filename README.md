# Ollama Discord Bot

Welcome to the Ollama Discord Bot project! 🎉 This bot leverages the Ollama API to bring some cool functionalities to your Discord server. Whether you're here to contribute, learn, or just check it out, we're glad to have you!

**Warning** - I still have no idea what I am doing. I am learning as I go. Expect things to break, expect descriptions to suck however enjoy the ride because I am glad you are here.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

- Latest Version of Python
- A Discord account along with a Bot already made
(UPDATE BOT CREATION LATER)
- An Ollama server configured and running

### Installation

1. **Clone the repo:**

    ```bash
    git clone https://github.com/MoldyTaint/DiscLlama.git
    cd DiscLlama
    ```

2. **Install dependencies:**

    ```
    sudo apt install python3
    ```

    ```
    pip install py-cord
    ```

3. **Configure your environment:**

    There is a file labled .env. This file is housing sensitive information like your Discord Bot Tokern, Guild ID, and Ollama Server.

    ```
    DISCORD_BOT_TOKEN=Discord Bot Token Here
    DISCORD_SERVER_ID=Discord Server ID Here
    LOCALHOST_URL=http://localhost/api/generate
    ```

4. **Run the bot:**

    ```
    python3 main.py
    ```

    Your bot should now be online!

## Usage

Invite the bot to your Discord server and use the following commands to interact with it:

- **`/ask`** - Displays a list of available commands.
- **`/ask Question`** - Ask something and get a response using the Ollama API.

## Contributing

Contributions are what make the open-source community such an amazing place to be. Any contributions you make are **greatly appreciated**.

**How to Contribute**

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the GNU GENERAL PUBLIC LICENSE. See `LICENSE` for more information.

## Acknowledgements

- Thanks to [Ollama](https://ollama.com) for their awesome LLM engine.

## Contact

If you have any questions or feedback, feel free to open an issue or reach out directly.
