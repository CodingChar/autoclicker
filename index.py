import pyautogui
import time

print('El programa va ejecutarse en un lapso de 5s.')
while True:
    time.sleep(5)
    print('Click!')
    pyautogui.click()
