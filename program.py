import pyautogui
import pyperclip
import time

# Give yourself 5 seconds to switch to the target window
time.sleep(1)

# Step 1: Click on the icon at (837, 140)
pyautogui.click(837, 140)

time.sleep(1)

# Step 2: Drag to select text from (492, 110 to (633, 668)
pyautogui.moveTo(492, 110)
pyautogui.mouseDown()
pyautogui.moveTo(633, 668, duration=1)
pyautogui.mouseUp()

time.sleep(1)

# Step 3: Copy selected text (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')

time.sleep(1)
pyautogui.click(770, 615)

# Step 4: Get copied text into a variable
copied_text = pyperclip.paste()

print("Copied Text:")
print(copied_text)