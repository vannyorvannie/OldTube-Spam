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

def accgen(usrshit2, emailshit, passwdshitlol):
    driver = webdriver.Firefox()
    driver.get("https://byteview.org/sign_up") #yonked
    time.sleep(1)
    usrshit = driver.find_element(By.NAME, "username")
    usrshit.send_keys(usrshit2)
    passwdlol = driver.find_element(By.NAME, "password")
    passwdlol.send_keys(passwdshitlol)
    emailshet = driver.find_element(By.NAME, "email")
    emailshet.send_keys(emailshit)
    valuesignup = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    valuesignup.click()
    with open("byteviewpaste.txt", "a") as file:
        file.write(f"{usrshit2}:{passwdshitlol}:{emailshit}\n")
    driver.quit()
if __name__ == "__main__":
    ass = int(input("How many accs:"))
    for i in range(ass):
        genpasswd = generate_password()
        genusrname = generate_username()
        genmail = generate_random_email()
        accgen(usrshit2=genusrname, emailshit=genmail, passwdshitlol=genpasswd)