#画面上のマウスが置かれている位置を取得
#Enterで取得、Ctrl+C で終了
#Points geter
#----------------------------------------------------#

import pyautogui as gui
import sys

#introduction
print('exit by Ctrl+C')

#get pointer X,Y by Enter
try:
    while True:
        x=input("setting cursor and Enter\n")
        print(gui.position())

#while exit by Ctrl+C
except KeyboardInterrupt:
    print('\nend')
    sys.exit()