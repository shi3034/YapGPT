import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key = 'sk-None-ogsCfim1X4ztYGGYI0nMT3BlbkFJsQJ8Dk0TnqWxlyKEGV9X',
)

def is_last_message_from_sender(chat_log, sender_name="Mumma"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

# Click on the  icon at (1639, 1412)
pyautogui.click(1291, 1044)
time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    # Move to the starting point of the text selection
    pyautogui.moveTo(1105, 813)
    time.sleep(0.5)  # Short pause

    # Drag to the end point of the text selection
    pyautogui.dragTo(1413, 811, duration=1.0,button='left')  # Duration makes the drag smoother
    time.sleep(0.5)  # Short pause

    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1548,771) #to deselect the text
    time.sleep(0.5)  # Wait for clipboard to update

    # Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()


    # Print the retrieved text to verify
    print(chat_history)
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named shivangi srivastva who speaks Hindi as well as English. You are from India and are a coder. You analyze chat history and respond like shivangi srivastva. Output should be the next chat response (text message only). Do not start like this [21:02, 12/6/2024] Mumma:"},
            {"role": "user", "content": chat_history}
        ]
        )

        response=(completion.choices[0].message)
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1216,929)
        pyautogui.click(1216, 929)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')
