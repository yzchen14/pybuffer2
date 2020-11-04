from pyautogui import locateAllOnScreen, click, moveTo
from time import sleep
print("Code running")
while(True):
    moveTo(20,20)
    sleep(0.1)
    button7location = locateAllOnScreen('001.png', confidence=.9)
    for pos in button7location:
        print(pos)
        moveTo(pos)
        click()
        print("Click")
        sleep(0.2)
    print("wait")
    sleep(5)