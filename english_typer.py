# korean_typer.py
# This script simulates typing to bypass copy-paste restrictions on websites.

import pyautogui
import time
import pyperclip # A library to easily work with the clipboard

def main():
    """
    Main function to run the auto-typer.
    """
    try:
        # Get the Korean text from the user's clipboard
        korean_text = "sadfsdfsdfdsf"

        if not korean_text:
            print("Your clipboard is empty. Please copy the Korean answer text first.")
            return

        print(f"Text to be typed: '{korean_text}'")
        
        # --- (Optional) You can modify this value ---
        # This is the delay (in seconds) before the script starts typing.
        # It gives you time to switch from this window and click on the exam text box.
        # Increase it if you need more time.
        delay_before_typing = 5  

        print("---------------------------------------------------------")
        print(f"The script will start typing in {delay_before_typing} seconds.")
        print("ACTION REQUIRED: Click on the text box in your browser NOW!")
        print("---------------------------------------------------------")

        # Countdown timer in the console
        for i in range(delay_before_typing, 0, -1):
            print(f"...{i}")
            time.sleep(1)

        print("\nTyping...")

        # This is the core of the script. It types the text character by character.
        # The 'interval' adds a small, human-like delay between each keystroke.
        pyautogui.write(korean_text, interval=0.1)

        print("\n✅ Typing complete!")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure you have installed the required libraries with 'pip install pyautogui pyperclip'.")

if __name__ == "__main__":
    main()