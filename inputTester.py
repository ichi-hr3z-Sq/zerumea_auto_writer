#[sShot.py][comparison.py]を含む実行プログラム
#[sShot.py]はobsの配信画面からスクリーンショットを保存する
#[comparison.py]は取得したスクショのトリミングと比較をする
#input tester
#used py files
#   check\\sShot.py
#       getting ScreenShot
#   check\\sShotPng\\comparison.py
#       trimming SS and comparison
#-------------------------------------------------------#


#[comparison.py]から得られた結果を元に、
#webページを操作するのでseleniumをインポートする
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#使用するドライバーのpath
#driver pass
driver_path = "msedgedriver.exe"
#make web driver 
driver = webdriver.Edge(executable_path = driver_path)

#ゼルメアシートの起動
#zerumea open
driver.get("https://miakoron.net/zerumea/")

#以下、ゼルメアシートの動作を確認する
#=================================================================
#fill in unexplored
i = 16
while i<20 :
    driver.find_element(By.ID, "box"+str(i)).click()
    driver.find_element(By.ID, "mitansaku").click()
    i += 1

#fill in 12 mass
driver.find_element(By.ID, "box22").click()
i = 0
while i<12 :
    #ボタンクリック
    zone = "dropzone" + str(i)
    driver.find_element(By.ID, zone).click()
    i += 1

#5s wait
time.sleep(5)
#close browser
driver.quit() 

#動作確認ここまで
#=================================================================

#sShot.py とcomparison.pyの読み込み
#get ScreenShot
import sShot

#trimming by SS
import comparison

#comparison.pyの結果から、対応するマスを対応する画像に変更
#webページへ入力（の予定）
print('#success- inputTester.py')

