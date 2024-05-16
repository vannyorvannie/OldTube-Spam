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
import urllib
def generate_username(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_password(length=12): # ah yes i must include numbers in my passwd
    letters = ''.join(random.choice(string.ascii_letters) for _ in range(length - 5))
    numbers = ''.join(random.choice(string.digits) for _ in range(5))
    password = letters + numbers
    return password
def generate_random_email(username_length=8):
    username = ''.join(random.choice(string.ascii_letters) for _ in range(username_length))
    email = f"{username}@gmail.com"
    return email
def randomshit(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
def randomtag(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def randomdesc(length=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def spam(): # i will add this shit back dw
    with open("raperacastdotcc1.txt", "a") as file:
        file.write(f"{username}:{password}:{email}\n")
    time.sleep(10)
    driver.execute_script("window.open('', '_blank');")
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    # actual spam/ uploading
    driver.get("https://www.eracast.cc/upload_video")
    videolinkshit = driver.find_element(By.XPATH, "//button[contains(., 'Select files from your computer')]") 
    videolinkshit.send_keys(rf"C:\Users\Administrator\Downloads\am.mp4") #for some shit reason, this is the button
    file_input = driver.find_element(By.ID, "video-file")  
    file_input.send_keys(r"C:\Users\Administrator\Downloads\am.mp4") # THIS is THE UPLOADING thing.
    time.sleep(5)
    #videotitlelol = driver.find_element(By.NAME, "title")
    #videotitlelol.send_keys(title)
    descriptionlol = driver.find_element(By.NAME, "description")
    #descriptionlol.send_keys(description) woops this doesnt work for some reason lol
    driver.execute_script("arguments[0].value = arguments[1];", descriptionlol, description)
    tagrape = driver.find_element(By.ID, "tags")
    tagrape.send_keys(tag)
    time.sleep(30)
    saveasschanges = driver.find_element(By.ID, "save")
    saveasschanges.click()
    driver.quit()
def accgen(username, password, tag, description):
    driver = webdriver.Firefox()
    driver.get("https://emailnator.com/")
    time.sleep(2)
    try:
        fuckyoucookies = driver.find_element(By.CLASS_NAME, "fc-button")
        fuckyoucookies.click()
    except: # sometimes, it doesnt come up?
        pass
    domain_checkbox = driver.find_element(By.XPATH, "//input[@id='custom-switch-domain']")
    driver.execute_script("arguments[0].scrollIntoView();", domain_checkbox)
    time.sleep(2)
    domain_checkbox.click()
    google_mail_checkbox = driver.find_element(By.ID, "custom-switch-googleMail")
    google_mail_checkbox.click()
    generate_button = driver.find_element(By.XPATH, '//button[contains(text(), "Generate New")]')
    generate_button.click()
    time.sleep(2)
    go_button = driver.find_element(By.XPATH, '//button[@name="goBtn" and contains(text(), "Go !")]')
    driver.execute_script("arguments[0].scrollIntoView();", go_button)
    time.sleep(2)
    go_button.click()
    url = driver.current_url
    parsed_url = urllib.parse.urlparse(url)
    email_address = parsed_url.fragment.lstrip('#')
    driver.switch_to.window(driver.window_handles[0])
    driver.execute_script("window.open('', '_blank');")
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    driver.get("https://www.eracast.cc/sign_up")
    usernameass = driver.find_element(By.NAME, "username")
    usernameass.send_keys(username)
    passwordass = driver.find_element(By.ID, "password") # name and id for password is the same.
    passwordass.send_keys(password)
    emailuh = driver.find_element(By.NAME, "email")
    emailuh.send_keys(email_address)
    submitthiscrap = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    submitthiscrap.click()
    # made the account, switching back to emailnator.
    driver.switch_to.window(driver.window_handles[0])
    try:
        print("Closing this stupid fucking add")
        killyourselfads = driver.find_element(By.ID, "dismiss-button")
        #killyourselfads.click()
        all_iframes = driver.find_elements(By.TAG_NAME, "iframe")
        driver.execute_script("""
        var elems = document.getElementsByTagName("iframe"); 
        for(var i = 0, max = elems.length; i < max; i++)
             {
                 elems[i].hidden=true;
             }
                          """)
    except:
        print("No add found?")
    time.sleep(3)
    reload_button = driver.find_element(By.XPATH, '//button[@type="button" and @name="reload"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", reload_button)
    #time.sleep(7)
    reload_button.click()
    time.sleep(3)
    emailbutton = driver.find_element(By.XPATH, "//div[@id='root']/div/section/div/div/div[3]/div/div[2]/div[2]/div/table/tbody/tr[2]/td/a/table/tbody/tr/td[2]")
    emailbutton.click()
    time.sleep(1)
    thelinkactual = driver.find_element(By.XPATH, "//a[contains(text(),'here')]")
    thelinkactual.click()
if __name__ == "__main__":
    #while True:
        usernamerand = generate_username()
        passwdrand = generate_password()
        #titlerand = randomshit()
        descrandom = randomdesc()
        tagass = randomtag()
        accgen(username=usernamerand, password=passwdrand, tag=tagass, description=descrandom)