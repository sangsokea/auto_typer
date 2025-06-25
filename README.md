# Auto-Typer Scripts (Korean & English)

This repository contains two Python scripts designed to simulate keyboard typing. Their primary purpose is to bypass copy-paste restrictions often found on secure websites or applications, allowing users to input text by simulating individual key presses.

## `korean_typer_v1.py` - Advanced Korean Typing Simulator

This script provides a sophisticated method for typing Korean text by simulating the actual key presses required to form Hangul characters on a Dubeolsik (2-Set) Korean keyboard layout. It decomposes complete Hangul syllables into their fundamental components (choseong, jungseong, jongseong - collectively known as jamos) and then presses the corresponding English keyboard keys.

### How it Works

1.  **Hangul Decomposition**: A given Korean syllable (e.g., '한') is first broken down into its constituent jamos (e.g., 'ㅎ', 'ㅏ', 'ㄴ').
2.  **Jamo to Key Mapping**: Each jamo is mapped to its corresponding English keyboard key(s) based on the standard Dubeolsik layout. For example, 'ㅎ' maps to 'g', 'ㅏ' maps to 'k', and 'ㄴ' maps to 's'. Compound jamos (like 'ㅘ' or 'ㄳ') are mapped to sequences of keys (e.g., 'ㅘ' maps to 'hk').
3.  **Simulated Key Presses**: The `pyautogui` library is used to simulate pressing these keys in sequence, including handling `Shift` for uppercase keys (which correspond to double consonants or specific vowels in the Dubeolsik layout).
4.  **Bypassing Restrictions**: By simulating individual key presses with small, human-like delays, this script can often bypass systems that block direct copy-pasting of text.

### Usage

1.  **Install Dependencies**:
    ```bash
    pip install pyautogui pyperclip
    ```
2.  **Copy Korean Text**: Copy the desired Korean text to your system's clipboard.
3.  **Run the Script**: Execute `korean_typer_v1.py` from your terminal:
    ```bash
    python korean_typer_v1.py
    ```
4.  **Switch Keyboard Layout**: **Crucially**, ensure your system's keyboard input method is set to **Korean (한)** before the countdown finishes. The script simulates English key presses, but your operating system interprets these as Korean characters based on the active input method.
5.  **Focus Target Application**: During the 5-second countdown displayed in the console, quickly switch to the application or text field where you want the text typed and click on it to give it focus.
6.  **Typing Begins**: The script will then automatically type the text character by character.

### Important Notes for `korean_typer_v1.py`

*   **Keyboard Layout**: This script *requires* your system's input method to be set to Korean (Dubeolsik) for it to function correctly.
*   **Timing**: Small delays are introduced between key presses and between full characters to simulate human typing and improve reliability.
*   **Error Handling**: Basic error handling for an empty clipboard and missing libraries is included.

## `english_typer.py` - Simple English Typing Simulator

This script provides a straightforward way to type English text by simulating character-by-character key presses. It's simpler than the Korean typer as it doesn't involve complex character decomposition.

### How it Works

1.  **Text Source**: As provided, the script currently uses a hardcoded string (`"sadfsdfsdfdsf"`) for typing. It includes commented-out code (`# korean_text = pyperclip.paste()`) that can be uncommented to enable reading text directly from the system clipboard.
2.  **Character-by-Character Typing**: It uses `pyautogui.write()` to type the text, introducing a small delay (`interval=0.1`) between each character to simulate human typing.

### Usage

1.  **Install Dependencies**:
    ```bash
    pip install pyautogui pyperclip
    ```
2.  **Modify (Optional)**: If you wish to type text from your clipboard instead of the hardcoded string, open `english_typer.py` and:
    *   Uncomment the line: `korean_text = pyperclip.paste()`
    *   Comment out or remove the line: `korean_text = "sadfsdfsdfdsf"`
3.  **Copy English Text (if modified)**: If you modified the script to use the clipboard, copy the desired English text to your clipboard.
4.  **Run the Script**: Execute `english_typer.py` from your terminal:
    ```bash
    python english_typer.py
    ```
5.  **Focus Target Application**: During the 5-second countdown, quickly switch to the application or text field where you want the text typed and click on it to give it focus.
6.  **Typing Begins**: The script will then automatically type the text.

### Important Notes for `english_typer.py`

*   **Hardcoded Text**: By default, it types a fixed string. Remember to modify the script if you intend to use clipboard content.
*   **Simplicity**: This script is designed for simple, direct typing of English characters.

## General Installation

Both scripts require the `pyautogui` and `pyperclip` libraries. You can install them using pip:

```bash
pip install pyautogui pyperclip
```