from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
from time import sleep
from LocalStorage import LocalStorage

driver = webdriver.Firefox()
driver.get("https://pg-stage.rpd.cloud/?partnerId=4&currency=USD&lan=en&gameId=34&mode=fun")

storage = LocalStorage(driver)
string = storage.get("crash_34_userSettings")
string2 = string.replace("null", "263")
print(string2)
storage.set("crash_34_userSettings", string2)
print(storage.get("crash_34_userSettings"))

driver.refresh()

#sleep(5) 
#storage.set("crash_34_userSettings", "\"isMusicOn\":false,\"musicVolume\":0,\"isSoundOn\":false,\"soundVolume\":0,\"isDarkModeOn\":false,\"isWinterModeOn\":false,\"isAnimationOn\":true,\"gameThemeConfigs\":{\"themeType\":3,\"isEnabled\":true},\"isHalfCashOutOn\":true,\"selectedGameTypeId\":263,\"isHideHalfCashOut\":false")
#print(driver.find_elements(By.XPATH, "/html/body"))
#buttons = driver.find_elements(By.TAG_NAME,"button")
#driver.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/button").click()
#WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[4]/button"))).click()
#buttons[1].click()
#for button in buttons:
#    print(buttons.index(button), button.text)
#soup = BeautifulSoup(driver.page_source, 'lxml')
#print(soup.prettify())