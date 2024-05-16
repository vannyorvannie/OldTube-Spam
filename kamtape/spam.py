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
# 6.11.2023 
# made by lynth
# 22:43
# KamTAPE Raper.
def generate_random_tag(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
def randomtag(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def randomdesc(length=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
def randomtitle(length=7):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def spam(username, password, tag, title, description):
    driver = webdriver.Firefox()
    # logging in
    driver.get("https://www.kamtape.com/login.php")
    logininusr = driver.find_element(By.NAME, "field_login_username")
    logininusr.send_keys(username)
    logininpasswd = driver.find_element(By.NAME, "field_login_password")
    logininpasswd.send_keys(password)
    loginbuttonlol = driver.find_element(By.XPATH, "//input[@value='Log In']")
    loginbuttonlol.click()
    driver.execute_script("window.open('', '_blank');")
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    # actual spam/ uploading
    driver.get("http://www.kamtape.com/my_videos_upload.php")
    titleshit = driver.find_element(By.NAME, "field_upload_title")
    titleshit.send_keys(title)
    descriptionshit = driver.find_element(By.NAME, "field_upload_description")
    descriptionshit.send_keys(description)
    tageventhothiswilljustbewebsitesname = driver.find_element(By.NAME, "field_upload_tags")
    tageventhothiswilljustbewebsitesname.send_keys(tag)
    one = driver.find_element(By.XPATH, "//input[@name='chlist[]']")
    second = driver.find_element(By.XPATH, "(//input[@name='chlist[]'])[2]")
    third = driver.find_element(By.XPATH, "(//input[@name='chlist[]'])[3]")
    one.click()
    second.click()
    third.click()
    countinuethisshit = driver.find_element(By.NAME, "continue")
    countinuethisshit.click()
    time.sleep(3)
    uploadfilething = driver.find_element(By.NAME, "fileToUpload")
    uploadfilething.send_keys(r"C:\Users\Administrator\Desktop\i dont know at this point lmfao\kamtape\erm.mp4")
    publicizethis = driver.find_element(By.XPATH, "//input[@type='radio' and @name='private' and @value='1']")
    publicizethis.send_keys()
    uplaodbuttonlol = driver.find_element(By.NAME, "upload")
    uplaodbuttonlol.click()
    time.sleep(10)
    driver.quit()
    

def messagespam(username, password, actualsubject, actualdescrip):
    driver = webdriver.Firefox()
    driver.get("https://www.kamtape.com/login.php")
    logininusr = driver.find_element(By.NAME, "field_login_username")
    logininusr.send_keys(username)
    logininpasswd = driver.find_element(By.NAME, "field_login_password")
    logininpasswd.send_keys(password)
    loginbuttonlol = driver.find_element(By.XPATH, "//input[@value='Log In']")
    loginbuttonlol.click()
    driver.execute_script("window.open('', '_blank');")
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    time.sleep(10)
    # actual spam/ uploading
    driver.get("http://www.kamtape.com/outbox.php?user=Stoohp")
    subject = driver.find_element(By.NAME, "title")
    subject.send_keys(actualsubject)
    descr = driver.find_element(By.NAME, "comment")
    descr.send_keys(actualdescrip)
    submitthisshit = driver.find_element(By.NAME, "message")
    submitthisshit.click()
    time.sleep(10)
    driver.quit()
    
if __name__ == "__main__":
    with open("thisisretarded.txt", "r") as accounts:
        lines = accounts.readlines()
    for line in lines:
        for i in range(10): 
            txtusername, txtpassword, txtemail = line.strip().split(":")
            random_tags = [generate_random_tag(8) for _ in range(3)]
            tag_string = ' '.join(random_tags)
            descrandom = randomdesc()
            tagass = randomtag()
            randedtit = randomtitle()
            spam(username=txtusername, password=txtpassword, tag=tag_string, title=randedtit, description=descrandom)
