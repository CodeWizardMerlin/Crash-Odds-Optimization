from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from LocalStorage import LocalStorage
import requests

driver = webdriver.Firefox()
driver.get("https://pg-stage.rpd.cloud/?partnerId=4&currency=USD&lan=en&gameId=34&mode=fun")

storage = LocalStorage(driver)
string = storage.get("crash_34_userSettings")
string2 = string.replace("null", "263")
print(string2)
storage.set("crash_34_userSettings", string2)
print(storage.get("crash_34_userSettings"))

driver.refresh()
