import win32api,win32con
import pyautogui
import keyboard
import time

planet_img = "planet_clicking_game_bot\\img_files\\planet.png"
planet_coord_x, planet_coord_y = None, None
getMoreClicks_btn = "planet_clicking_game_bot\\img_files\\getMoreClicks_btn.png"

def find_btn(loc):
    while True:
        try:
            if pyautogui.locateOnScreen(loc, confidence=0.8):
                getMoreClicks_btn_x, getMoreClicks_btn_y = pyautogui.locateCenterOnScreen(loc, confidence=0.6)
                pyautogui.leftClick(getMoreClicks_btn_x, getMoreClicks_btn_y)
        except pyautogui.ImageNotFoundException:
            break

while True:
    try:
        if pyautogui.locateOnScreen(planet_img, confidence=0.6):
            planet_coord_x, planet_coord_y = pyautogui.locateCenterOnScreen(planet_img, confidence=0.6)
            print("Loop is finished")
            break
    except pyautogui.ImageNotFoundException:
        time.sleep(0.15)

while True:
    if keyboard.is_pressed("ctrl"):
        if not keyboard.is_pressed("ctrl"):
            break
        find_btn(getMoreClicks_btn)
        pyautogui.click(planet_coord_x, planet_coord_y)

    if keyboard.is_pressed("esc"):
        break