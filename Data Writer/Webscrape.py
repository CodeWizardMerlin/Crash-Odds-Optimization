from selenium import webdriver
from selenium.webdriver.common.by import By
from LocalStorageEditor import LocalStorage
from datetime import datetime
from time import sleep
from threading import Thread, Event
import tkinter as tk
import os

stop_event = Event()

root = None

def on_stop():
    global root
    stop_event.set()
    if root:
        root.after(0, root.destroy)

def create_stop_button():
    global root
    root = tk.Tk()
    root.title("Stop Button")

    stop_button = tk.Button(root, text="Stop", command=on_stop)
    stop_button.pack(pady=20)

    root.protocol("WM_DELETE_WINDOW", on_stop)
    root.mainloop()

button_thread = Thread(target=create_stop_button)
button_thread.start()

driver = webdriver.Firefox()
driver.get("https://pg-stage.rpd.cloud/?partnerId=4&currency=USD&lan=en&gameId=34&mode=fun")

# when opened, the crash website has a confirm button that needs to be bypassed to read the data from the html
# the website usues local storage to skip the popup when reloading the page, this code edits the local storage to bypass the button
storage = LocalStorage(driver)
initial_storage = storage.get("crash_34_userSettings")
modified_storage = initial_storage.replace("null", "263") # 263 is the value normally assigned after clicking continue
storage.set("crash_34_userSettings", modified_storage)
driver.refresh()
sleep(4) # wait for the page to load

count = 0
while not stop_event.is_set():
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Start of loop", count, "- At time:", current_time)
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "#game-frame"))
    messy_data = driver.find_element(By.CLASS_NAME, "scrollable-container").text.split("\n")

    multipliers = []
    for data in messy_data:
        if "x" in data:
            multipliers.append(data[1:])

    with open("Raw data.txt", "a") as file:
        if os.path.getsize("Raw data.txt") > 0:
            file.write("\n")
        for multiplier in multipliers:
            file.write(multiplier + " ")
    
    current_time = datetime.now().strftime("%H:%M:%S")
    print("End of loop", count, "- At time:", current_time)
    count = count + 1
    
    stop_event.wait(600)


driver.quit()
print("Program stopped")