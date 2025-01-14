# OpenAI Chatbot

This repository contains a simple chatbot implementation using OpenAI's GPT-3.5-turbo model. The chatbot interacts with users through the console and provides responses based on user input.

## Features
- Interactive chatbot experience through console input.
- Uses OpenAI's GPT-3.5-turbo model for generating responses.
- Includes error handling for API issues.

## Prerequisites
To run this chatbot, ensure you have the following installed:

- Python 3.7 or later
- OpenAI Python library (`openai`)

You also need an OpenAI API key to access the GPT-3.5-turbo model.

## Setup
1. Clone this repository or download the code file.
2. Install the required Python library:
   ```bash
   pip install openai
   ```
3. Obtain an OpenAI API key by signing up at [OpenAI's platform](https://platform.openai.com/).
4. Replace the placeholder `API_KEY` in the code with your actual OpenAI API key:
   ```python
   openai.api_key = "YOUR_API_KEY"
   ```

## Usage
1. Run the script using the following command:
   ```bash
   python chatbot.py
   ```
2. Interact with the chatbot by typing your messages into the console.
3. To exit the chatbot, type `exit`.

## Example
```bash
Welcome to the OpenAI Chatbot!
You: Hello, how are you?
Chatbot: I'm just a program, but I'm here to assist you! How can I help today?
You: exit
Chatbot: Goodbye! Have a great day!
```

## Error Handling
If an error occurs during the API call (e.g., due to network issues or invalid API key), the program will display an error message and continue running.

## Notes
- The `max_tokens` parameter is set to 100 to limit the response length. Adjust this value based on your needs.
- The chatbot is currently designed for console interaction only. To build a more advanced application, consider integrating it with a web or GUI framework.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

## Acknowledgments
- [OpenAI](https://openai.com/) for providing the GPT-3.5-turbo model.
- The Python community for creating and maintaining the `openai` library.

