import pyautogui
from PIL import ImageGrab

syl_x = None
syl_y = None
ws_x = None
ws_y = None
pixel_init = None
language = None
    
def calibration():
    global syllable_x, syllable_y, write_x, write_y, pixel_col, lang
    syllable_x = None
    syllable_y = None
    write_x = None
    write_y = None
    pixel_col = None
    
    while True:
        print("Place your cursor on the syllable without clicking")
        input("Press Enter when it's done")
        syllable_x, syllable_y = pyautogui.position()
        print(f"Syllable position: ({syllable_x}, {syllable_y})\n")
        break

    while True:
        print("Place your cursor on the writing space without clicking")
        input("Press Enter when it's done")
        write_x, write_y = pyautogui.position()
        print(f"Writing space position: ({write_x}, {write_y})\n")
        screenshot = ImageGrab.grab()
        pixel_col = screenshot.getpixel((write_x, write_y))
        break
    
    lang = input("Language fr or en ?")

    return syllable_x, syllable_y, write_x, write_y, pixel_col, lang

syl_x, syl_y, ws_x, ws_y, pixel_init, language = calibration()

with open("calibration_data.py", "w") as f:
    f.write(f"syl_x = {syl_x}\n")
    f.write(f"syl_y = {syl_y}\n")
    f.write(f"ws_x = {ws_x}\n")
    f.write(f"ws_y = {ws_y}\n")
    f.write(f"pixel_init = {pixel_init}\n")
    f.write(f"language = \"{language}\"\n")
    
    
