# korean_typer.py
# This script simulates REAL Korean typing by decomposing characters into their
# base components (jamos) and pressing the corresponding keys.
# This method is designed to bypass even the strictest copy-paste restrictions.

import pyautogui
import time
import pyperclip
import sys

# --- Data for Hangul Decomposition ---
# Lists of the basic building blocks of Korean characters.
CHOSEONG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNGSEONG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONGSEONG_LIST = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# --- Mapping from Jamo to English Keyboard Keys (Dubeolsik/2-Set Layout) ---
# This dictionary is the key to the script. It translates each Korean component
# into the actual key you would press on a QWERTY keyboard.
# Uppercase letters represent a Shift + key press.
# Multi-character strings represent compound characters that require multiple key presses.
KOR_TO_ENG_MAP = {
    'ㄱ': 'r', 'ㄲ': 'R', 'ㄴ': 's', 'ㄷ': 'e', 'ㄸ': 'E', 'ㄹ': 'f',
    'ㅁ': 'a', 'ㅂ': 'q', 'ㅃ': 'Q', 'ㅅ': 't', 'ㅆ': 'T', 'ㅇ': 'd',
    'ㅈ': 'w', 'ㅉ': 'W', 'ㅊ': 'c', 'ㅋ': 'z', 'ㅌ': 'x', 'ㅍ': 'v', 'ㅎ': 'g',
    'ㅏ': 'k', 'ㅐ': 'o', 'ㅑ': 'i', 'ㅒ': 'O', 'ㅓ': 'j', 'ㅔ': 'p',
    'ㅕ': 'u', 'ㅖ': 'P', 'ㅗ': 'h', 'ㅛ': 'y', 'ㅜ': 'n', 'ㅠ': 'b',
    'ㅡ': 'm', 'ㅣ': 'l',
    'ㅘ': 'hk', 'ㅙ': 'ho', 'ㅚ': 'hl', 'ㅝ': 'nj', 'ㅞ': 'np', 'ㅟ': 'nl', 'ㅢ': 'ml',
    'ㄳ': 'rt', 'ㄵ': 'sw', 'ㄶ': 'sg', 'ㄺ': 'fr', 'ㄻ': 'fa', 'ㄼ': 'fq',
    'ㄽ': 'ft', 'ㄾ': 'fx', 'ㄿ': 'fv', 'ㅀ': 'fg', 'ㅄ': 'qt'
}

def decompose_hangul(syllable):
    """
    Decomposes a complete Hangul syllable into its constituent jamos.
    For example: '한' -> ['ㅎ', 'ㅏ', 'ㄴ']
    """
    # Check if the character is a Hangul syllable
    if '가' <= syllable <= '힣':
        char_code = ord(syllable) - 44032
        
        # Calculate indices for each component
        choseong_index = char_code // 588
        jungseong_index = (char_code - (choseong_index * 588)) // 28
        jongseong_index = char_code % 28
        
        # Build the list of jamos
        jamos = [CHOSEONG_LIST[choseong_index], JUNGSEONG_LIST[jungseong_index]]
        if jongseong_index > 0:
            jamos.append(JONGSEONG_LIST[jongseong_index])
        return jamos
    else:
        # If it's not a syllable (e.g., a lone 'ㄱ' or 'ㅏ'), return it as is
        return [syllable]

def type_korean_text(text):
    """
    Types out the given Korean text by simulating keyboard presses for each jamo.
    """
    for char in text:
        decomposed_jamos = decompose_hangul(char)
        
        for jamo in decomposed_jamos:
            if jamo in KOR_TO_ENG_MAP:
                keys_to_press = KOR_TO_ENG_MAP[jamo]
                
                # Press the key or key combination for the jamo
                for key in keys_to_press:
                    if 'A' <= key <= 'Z':
                        # Uppercase means Shift + key
                        pyautogui.hotkey('shift', key.lower())
                    else:
                        pyautogui.press(key)
                    time.sleep(0.01) # Tiny delay between component keys
            else:
                # If character is not a jamo (e.g., space, punctuation), type it directly
                pyautogui.typewrite(char, interval=0.01)
        
        time.sleep(0.02) # Slightly longer delay between full characters

def main():
    """
    Main function to run the auto-typer.
    """
    try:
        # 1. Get the Korean text from the user's clipboard
        korean_text = pyperclip.paste()

        if not korean_text:
            print("Your clipboard is empty. Please copy the Korean answer text first.")
            return

        print(f"Text to be typed: '{korean_text}'")
        
        # 2. Give the user time to switch windows and set keyboard layout
        delay_before_typing = 5
        print("---------------------------------------------------------------")
        print("!!! IMPORTANT !!!")
        print("Make sure your keyboard input is set to KOREAN (한) NOW!")
        print(f"The script will start typing in {delay_before_typing} seconds.")
        print("ACTION REQUIRED: Click on the text box in your browser!")
        print("---------------------------------------------------------------")

        for i in range(delay_before_typing, 0, -1):
            print(f"...{i}")
            time.sleep(1)

        print("\nTyping...")
        # 3. Call the function to perform the simulated typing
        type_korean_text(korean_text)

        print("\n✅ Typing complete!")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure you have installed the required libraries with 'pip install pyautogui pyperclip'.")

if __name__ == "__main__":
    main()