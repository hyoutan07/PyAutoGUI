import pyautogui as pg
import time

for i in range(10):
    position = pg.position()
    print(position)
    time.sleep(0.5)
    
# print(type(position))
# print(position.x)
# print(position.y)