import pyautogui

def findMousePosition():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print("\nDone")

def pressKey(key,presses=1,interval=0):
    try:
        pyautogui.press(key,presses,interval)
    except KeyboardInterrupt:
        print("\nDone")

if __name__ == '__main__':
    width, height = pyautogui.size()
    #findMousePosition()
    pressKey("F",3)
