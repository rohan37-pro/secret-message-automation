import pyautogui as pt
import time


pt.hotkey("win",'r')
pt.write("notepad")
pt.press("enter")
pt.typewrite(f" ", interval=0.01)
