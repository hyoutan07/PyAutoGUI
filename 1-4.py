import pyautogui as pg
import time

# すべてのwindowを閉じる
pg.hotkey("win","d")
time.sleep(1)

p = pg.locateOnScreen("slack.jpg",grayscale=True, confidence=0.6)
print(p)
x, y = pg.center(p)
pg.moveTo(x,y,duration=1)