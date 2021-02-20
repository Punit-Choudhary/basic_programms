#!python3
#spam_bot.py - Automatocally sending message again and again to spam.\
# Dev : Punit Choudhary

import pyautogui
import time

time.sleep(5)

while True:
	time.sleep(1)
	pyautogui.typewrite("xx  spam  xx")
	pyautogui.press("enter")
