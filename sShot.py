#obsからスクリーンショットを取得する
#SS getter
#------------------------------------#

#png move
import os
import shutil
import time

#key input get
import pyautogui as gui
#open some app
import subprocess as app

#本来ならコンソール経由等でobsを指定して起動するのが望ましい
#今回はすでに起動してある状態からショートカットキーを活用してobsをアクティブウィンドウにしている
#open OBS (however when order of tabs VSC > OBS )
gui.hotkey("alt","tab")

#check screen size
#print(gui.size()) >> Display Size (width=1920, height=1080)
#right click width=1170, height=430
gui.click(1170,430, button="right")

#sShot > open directory > close > tab back
for i in range(6):
    gui.press("down")
gui.press("enter")
#open
sShot_path = "取得したスクリーンショットのpath"
sFolder = app.Popen(['start',sShot_path],shell=True)
time.sleep(1)
#close
gui.hotkey("alt","f4")
time.sleep(1)
#tab back
gui.hotkey("alt","tab")
time.sleep(1)

#sShot cut and move
#last, only '.png' files in here
files = []
#get all files in the directory by list
folder = os.listdir(sShot_path)
for i in folder:
    if i.endswith('.png'):
        files.append(i)
#print(files) >>ok

toPath = "取得したスクリーンショットを移動させたいフォルダのpath"
for name in files:
    png_path = sShot_path +"\\"+ name
    shutil.move(png_path,toPath +"\\sShot.png")

sFolder = app.Popen(['start',toPath],shell=True)
print('#success- sShot.py')