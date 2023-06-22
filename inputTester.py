#input tester
#used py files
#   check\\sShot.py
#       getting ScreenShot
#   check\\sShotPng\\comparison.py
#       trimming SS and comparison
#-------------------------------------------------------#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#driver pass
driver_pass = "msedgedriver.exe"
#make web driver 
driver = webdriver.Edge(executable_path = driver_pass)

#zerumea open
driver.get("https://miakoron.net/zerumea/")

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

#get ScreenShot
from check import sShot

#trimming by SS
from check.sShotPng import comparison

print('#success- inputTester.py')

