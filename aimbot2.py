import pyautogui #benchmark_aimbot
import time
import keyboard
time.sleep(2)

while True:
  aimbot = pyautogui.locateOnScreen('aimbot2.png', confidence=0.5)
  pyautogui.click(aimbot[0],aimbot[1])
