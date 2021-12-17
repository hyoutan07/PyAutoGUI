import pyautogui as pg
import time

x=10
y=10

pg.moveTo(x,y,duration=1)
time.sleep(1)

x = x + 1000
pg.moveTo(x,y)
time.sleep(1)

y = y + 1000
pg.moveTo(x,y,duration=3)
time.sleep(1)