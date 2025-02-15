import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key="enter your api key"
)

def is_last_message_from_sender(chat_log, sender_name="maa"):
    messages = chat_log.strip().split("/2025")[-1]
    if sender_name in messages:
        return True
    return False
   

# Click on the chrome icon at (920, 1042)
pyautogui.click(920, 1042)
# Wait for a moment before execution
time.sleep(2)

while True:
   

    # Click and drag to select the text
    pyautogui.moveTo(883, 295)
    pyautogui.mouseDown()
    pyautogui.moveTo(1892, 907, duration=1)  # Dragging smoothly
    pyautogui.mouseUp()

    # Copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1892, 907)

    # Small delay to ensure the text is copied
    time.sleep(1)

    # Get the copied text from clipboard
    chat_History = pyperclip.paste()

    # Print or use the copied text
    print("chat_History:", chat_History)

    if is_last_message_from_sender(chat_History):  # Fixed function call
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a person named rimel who speaks english, bengali and hindi. You are from India and you are a coder. You analyze chat history and respond like Rimel. Output should be the next chat response as Rimel."},
                {"role": "user", "content": chat_History}
            ]
        )
        response = completion.choices[0].message.content
        pyperclip.copy(response)
        pyautogui.click(1280, 980)
        time.sleep(1)  # Small delay to ensure the input field is active

        # Paste the copied text (Ctrl + V)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)  # Short delay before pressing enter

        # Press Enter
        pyautogui.press('enter')
