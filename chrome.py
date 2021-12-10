import pyautogui as pg
import time
import pyperclip

target = input("検索したい言葉を入力してください：")

# Windowsボタンを押す
pg.hotkey("win")
time.sleep(5)

# クリップボードにGoogleのサイトを入れて、貼り付け
pyperclip.copy("https://www.google.com/")
pg.hotkey("ctrl", "v")
time.sleep(5)

# Enterで決定
pg.hotkey("Enter")
time.sleep(10)

# クリップボードにtargetを入れて、貼り付け
pyperclip.copy(target)
pg.hotkey("ctrl", "v")
time.sleep(3)

# Enterで検索
pg.hotkey("Enter")
time.sleep(10)