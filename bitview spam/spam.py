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
from fake_useragent import UserAgent
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from colorama import Fore
def randomshit(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def randomdesc(length=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
# I'll do proxy shit later
def bitviewspam(title, description, tags, username, password, numberofvideos):
    driver = webdriver.Firefox()
    # login in 
    driver.get("https://www.bitview.net/login")
    time.sleep(8)
    try:
        fuckyoucookies = driver.find_element(By.CLASS_NAME, "fc-button")
        fuckyoucookies.click()
    except: # sometimes, it doesnt come up?
        pass
    logininusr = driver.find_element(By.NAME, "username")
    logininusr.send_keys(username)
    logininpasswd = driver.find_element(By.ID, "password") # THE ID AND THE NAME IS PASSWORD LOL THIS IS THE EASIEST THING TO BOT!
    logininpasswd.send_keys(password)
    logininez = driver.find_element(By.NAME, "signIn")
    logininez.click()
    # the actual posting
    for i in range(int(numberofvideos)): 
        driver.execute_script("window.open('', '_blank');")
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        driver.get("https://www.bitview.net/my_videos_upload")
        actualtitletoedit = driver.find_element(By.NAME, "title")
        actualtitletoedit.send_keys(title)
        descriptionlol = driver.find_element(By.NAME, "description")
        #descriptionlol.send_keys(description) woops this doesnt work for some reason lol
        driver.execute_script("arguments[0].value = arguments[1];", descriptionlol, description)
        tagshit = driver.find_element(By.NAME, "tags")
        tagshit.send_keys(tags)
        shituploadbutton = driver.find_element(By.NAME, "upload_video")
        shituploadbutton.click()
        # video uploading 
        nigger = driver.find_element(By.ID, "video_file")
        nigger.send_keys(rf"C:\Users\Administrator\Desktop\i dont know at this point lmfao\bitview spam\moonman.mp4") # stupid turkish windows, makes me think "Masaüstü" is actually the Desktop Folder.
        time.sleep(1)
        uploadbuttonfinal = driver.find_element(By.ID, "upload_video2")
        uploadbuttonfinal.click()
        time.sleep(10)
        driver.quit()
    driver.quit()

def commentspamiguess(username, password, comment):
    # Plan:
    # Comment spam the "message for kamtape spammer"
    # ngl hes pretty funny..
    # ALEX IS DOING THIS SHIT LOL 
    # ez fucking reaction LOL
    driver = webdriver.Firefox()
    # login in 
    # https://www.bitview.net/watch?v=YQ3vtMJr1a5
    
    driver.get("https://www.bitview.net/login")
    time.sleep(8)
    try:
        fuckyoucookies = driver.find_element(By.CLASS_NAME, "fc-button")
        fuckyoucookies.click()
    except: # sometimes, it doesnt come up?
        pass
    logininusr = driver.find_element(By.NAME, "username")
    logininusr.send_keys(username)
    logininpasswd = driver.find_element(By.ID, "password") 
    logininpasswd.send_keys(password)
    logininez = driver.find_element(By.NAME, "signIn")
    logininez.click()
    # the actual posting
    driver.execute_script("window.open('', '_blank');")
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    driver.get("https://www.bitview.net/watch?v=YQ3vtMJr1a5")
    RAPEALEX = driver.find_element(By.ID, "comment_text")
    RAPEALEX.clear()
    RAPEALEX.send_keys(comment)
    RAPEALEXSUBMUT = driver.find_element(By.ID, "comment_submit")
    RAPEALEXSUBMUT.click()
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    with open("ProjectFemBitView.txt", "r") as accounts_file:
        lines = accounts_file.readlines()
    print("[Y] Randomized? ")
    print("[N] Not Randomized.")
    print("[R] RAPE ALEX?")
    answer = input("Answer: ")
    if answer == "Y":
        for line in lines:
            txtusername, txtpassword, txtemail = line.strip().split(":")
            randomizedtitle = randomshit()
            randomizeddescription = randomdesc()
            numberofvideostospam = input("How many videos do you want to spam: ")
            bitviewspam(title=randomizedtitle, description=randomizeddescription, tags="bitview", username=txtusername, password=txtpassword, numberofvideos=numberofvideostospam)
    if answer == "N":
        for line in lines:
            txtusername, txtpassword, txtemail = line.strip().split(":")
            randomizedtitle = input("Title: ")
            randomizeddescription = input("Description: ")
            numberofvideostospam = input("How many videos do you want to spam: ")
            bitviewspam(title=randomizedtitle, description=randomizeddescription, tags="bitview", username=txtusername, password=txtpassword, numberofvideos=numberofvideostospam)
    if answer == "R":
        for line in lines:
            nigger = input("How many comments do you want to spam? : ")
            for i in range(int(nigger)):
                txtusername, txtpassword, txtemail = line.strip().split(":")
                randomizeddescription = randomdesc()
                commentspamiguess(username=txtusername, password=txtpassword, comment=randomizeddescription)