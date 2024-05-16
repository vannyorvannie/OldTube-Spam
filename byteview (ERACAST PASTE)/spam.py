from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium_recaptcha_solver import RecaptchaSolver
import random
import string
import requests
import threading
from concurrent import futures
import concurrent
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import urllib


def randomshit(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
def randomtag(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def randomdesc(length=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# <input style="width: 550px;margin-top: 3px;" type="text" name="title" id="upltx" required="required" class="yt-uix-form-input-text upload-inputs">
# <textarea class="yt-uix-form-input-text" style="width: 550px;margin-top: 3px;" placeholder="Video Description" id="upltx2" name="comment"></textarea>
# <input id="tags" class="yt-uix-form-input-text upload-inputs" style="width: 550px;margin-top: 3px;" placeholder="Seperate with commas" type="text" name="tags" row="20">
# <input class="yt-uix-button yt-uix-button-default" type="submit" value="Upload Video">
def spam(username, password):
    cum = rf"D:\random projects\i dont know at this point lmfao\byteview (ERACAST PASTE)\erm.mp4"
    driver = webdriver.Firefox()
    driver.get("https://byteview.org/")
    time.sleep(1)
    fuckyou = driver.find_element(By.ID, "masthead-user-button")
    fuckyou.click()
    time.sleep(1)
    loginusr = driver.find_element(By.NAME, "username")
    loginusr.send_keys(username)
    paswd = driver.find_element(By.NAME, "password")
    paswd.send_keys(password)
    sabmitmate = driver.find_element(By.XPATH, "//input[@value='Login']")
    sabmitmate.click()
    time.sleep(1)
    driver.execute_script("window.open('', '_blank');")
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    driver.get("https://byteview.org/upload_video")
    #videolinkshit = driver.find_element(By.XPATH, "//button[contains(., 'Select files from your computer')]") 
    #videolinkshit.send_keys(cum) #for some shit reason, this is the button
    file_input = driver.find_element(By.ID, "fileToUpload")  
    file_input.send_keys(cum) # THIS is THE UPLOADING thing.
        #videotitlelol = driver.find_element(By.NAME, "title")
    #videotitlelol.send_keys(title)
    saveasschanges = driver.find_element(By.XPATH, "//input[@value='Upload Video']")
    saveasschanges.click()
    time.sleep(10)
    driver.quit()


if __name__ == "__main__":
    with open("byteviewpaste.txt", "r") as accounts:
        lines = accounts.readlines()
    for line in lines:
        txtusername, txtpassword, txtemail = line.strip().split(":")
        descrandom = randomdesc()
        tagass = randomtag()
        spam(username=txtusername, password=txtpassword)