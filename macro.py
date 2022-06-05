from time import sleep
import pyautogui

width, height = pyautogui.size()

#func that print mouse position updating in real time
def findMousePosition():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print("\nDone")

#func to press key
def pressKey(key,presses=1,interval=0.1):
    try:
        pyautogui.press(key,presses,interval)
    except KeyboardInterrupt:
        print("\nDone")

def click(button='PRIMARY',clicks=1,interval=0.1):
    pyautogui.click(button=button,clicks=clicks,interval=interval)

def wait(time=1):
    sleep(time)

if __name__ == '__main__':
    findMousePosition()
    #pressKey("F",3)
