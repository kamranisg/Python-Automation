#GetCursorPosition.py

import pyautogui

try:
    while True:
        x,y=pyautogui.position()
        poss=  'X: ' +str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(poss, end='')
        print('\b' * len(poss), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone')
