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
import winsound
def generate_username(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_password(length=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
def generate_random_email(username_length=8):
    username = ''.join(random.choice(string.ascii_letters) for _ in range(username_length))
    email = f"{username}@gmail.com"
    return email
def randomshit(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def randomdesc(length=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def randomvideoname(length=5):
    ass = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    withshit = f"{ass}.mp4"
    return withshit
import cv2
import numpy as np
import os

def generate_random_frame(width, height):
    # Generate a random frame with random pixel values
    frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    return frame

def create_random_video(output_path, width, height, fps, duration):
    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Generate random frames and write them to the video file
    num_frames = int(fps * duration)
    for _ in range(num_frames):
        frame = generate_random_frame(width, height)
        video_writer.write(frame)

    # Release the VideoWriter object
    video_writer.release()

def accountgen(defemail, defusername, defpassword):
    driver = webdriver.Firefox()
    driver.get("https://www.bitview.net/signup")
    time.sleep(6)
    try:
        fuckyoucookies = driver.find_element(By.CLASS_NAME, "fc-button")
        fuckyoucookies.click()
    except: # sometimes, it doesnt come up?
        pass
    email = driver.find_element(By.ID, "signUpEmail")
    email.send_keys(defemail)
    password = driver.find_element(By.ID, "signUpPassword1") # retype password shit
    password2 = driver.find_element(By.ID, "signUpPassword2")
    password.send_keys(defpassword)
    password2.send_keys(defpassword)
    username = driver.find_element(By.ID, "username")
    username.send_keys(defusername)
    print("Do the captcha you monkey")
    winsound.Beep(1000, 500)  # Frequency: 1000Hz, Duration: 500ms
    input("Press enter when youre done: ")
    termsandshit = driver.find_element(By.ID, "terms")
    termsandshit.click()
    time.sleep(3)
    gennedtheacc = driver.find_element(By.NAME, "signIn")
    gennedtheacc.click()
    print("[!] Generated Successfully?")
    print(f"[!] {defusername}")
    print(f"[!] {defpassword}")
    print(f"[!] {defemail}")
    driver.quit()
    with open("ProjectFemBitView.txt", "a") as file:
        file.write(f"{defusername}:{defpassword}:{defemail}\n")

def accountgenthenspam(defemail, defusername, defpassword, numberofvideos, title, description, tags, video):
    driver = webdriver.Firefox()
    driver.get("https://www.bitview.net/signup")
    time.sleep(6)
    try:
        fuckyoucookies = driver.find_element(By.CLASS_NAME, "fc-button")
        fuckyoucookies.click()
    except: # sometimes, it doesnt come up?
        pass
    email = driver.find_element(By.ID, "signUpEmail")
    email.send_keys(defemail)
    password = driver.find_element(By.ID, "signUpPassword1") # retype password shit
    password2 = driver.find_element(By.ID, "signUpPassword2")
    password.send_keys(defpassword)
    password2.send_keys(defpassword)
    username = driver.find_element(By.ID, "username")
    username.send_keys(defusername)
    print("Do the captcha you monkey")
    input("Press enter when youre done: ")
    termsandshit = driver.find_element(By.ID, "terms")
    termsandshit.click()
    time.sleep(3)
    gennedtheacc = driver.find_element(By.NAME, "signIn")
    gennedtheacc.click()
    print("[!] Generated Successfully?")
    print(f"[!] {defusername}")
    print(f"[!] {defpassword}")
    print(f"[!] {defemail}")
    #driver.quit()
    with open("ProjectFemBitView.txt", "a") as file:
        file.write(f"{defusername}:{defpassword}:{defemail}\n")
    for i in range(10): # you can only do 10 videos per account 
        driver.execute_script("window.open('', '_blank');")
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        driver.get("https://www.bitview.net/my_videos_upload")
        actualtitletoedit = driver.find_element(By.NAME, "title")
        actualtitletoedit.send_keys(title)
        descriptionlol = driver.find_element(By.NAME, "description")
        #descriptionlol.send_keys(description) 
        driver.execute_script("arguments[0].value = arguments[1];", descriptionlol, description)
        tagshit = driver.find_element(By.NAME, "tags")
        tagshit.send_keys(tags)
        shituploadbutton = driver.find_element(By.NAME, "upload_video")
        shituploadbutton.click()
        # video uploading 
        nigger = driver.find_element(By.ID, "video_file")
        nigger.send_keys(rf"C:\Users\Administrator\Desktop\i dont know at this point lmfao\bitview spam\{video}") # stupid turkish windows, makes me think "Masaüstü" is actually the Desktop Folder.
        time.sleep(1)
        uploadbuttonfinal = driver.find_element(By.ID, "upload_video2")
        uploadbuttonfinal.click()
        time.sleep(20)
    driver.quit()
def mainshit():
    #howmanyaccounts = input("How many accounts do you want: ")
    #for i in range(int(howmanyaccounts)):
        genusername = generate_username()
        emailunverify = generate_random_email()
        passwdlol = generate_password()
        randomizedtitle = randomshit()
        randomizeddescription = randomdesc()
        output_path = randomvideoname()
        width = 10
        height = 10
        fps = 1
        duration = 1  # in seconds

        # Create a random video
        create_random_video(output_path, width, height, fps, duration)

        #accountgen(defemail=emailunverify, defusername=genusername, defpassword=passwdlol)
        accountgenthenspam(defemail=emailunverify, defusername=genusername, defpassword=passwdlol, numberofvideos="2", title=randomizedtitle, description=randomizeddescription, tags="bitview", video=output_path)

if __name__ == "__main__":
    mainshit()