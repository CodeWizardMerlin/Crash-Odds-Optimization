from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from LocalStorageEditor import LocalStorage
import requests
from time import sleep

driver = webdriver.Firefox()
driver.get("https://pg-stage.rpd.cloud/?partnerId=4&currency=USD&lan=en&gameId=34&mode=fun")

# when opened, the crash website has a confirm button that needs to be bypassed to read the data from the html
# the website usues local storage to skip the popup when reloading the page, this code edits the local storage to bypass the button
storage = LocalStorage(driver)
initial_storage = storage.get("crash_34_userSettings")
modified_storage = initial_storage.replace("null", "263") # 263 is the value normally assigned after clicking continue
storage.set("crash_34_userSettings", modified_storage)
driver.refresh()

sleep(3)
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "#game-frame"))
messy_data = driver.find_element(By.CLASS_NAME, "scrollable-container").text