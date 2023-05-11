import pyautogui as pt
import time


pt.hotkey("win",'r')
pt.write("notepad")
pt.press("enter")
pt.typewrite(f"{chr(104)}{chr(101)}{chr(108)}{chr(108)}{chr(111)}", interval=0.01)
