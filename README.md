
Auto Reply Chatbot

What is this?

Hey there! This is a little Python script I made to automatically reply to WhatsApp messages. It reads messages using PyAutoGUI, checks if the last message is from "Maa", and then replies using OpenAI's GPT-4o-mini. Pretty cool, right?

How does it work?

The script opens WhatsApp Web in Chrome.

It copies the latest chat messages.

If the last message is from "Maa", it sends the chat history to OpenAI's API.

It pastes the AI-generated response back into the chat and sends it.

What you need:

Python 3.x installed on your system.

Install these libraries:

pip install pyautogui pyperclip openai

Your own OpenAI API key (replace "enter your api key" in the script) if you want to run this code.

How to set it up:

Make sure WhatsApp Web is open.

Adjust the PyAutoGUI coordinates if needed (since screen resolutions vary).

Run the script and let it handle replies for you!

Troubleshooting:

Wrong clicks? Adjust the coordinates where PyAutoGUI interacts.

Encoding errors? Set your terminal to UTF-8.

OpenAI errors? Check your API key and usage limits.

Final Note:

This is a beginner-level project, so feel free to make changes and experiment with the code!

Use this responsibly! It’s meant for fun and convenience, not spam or anything unethical.

Happy coding! 😊

