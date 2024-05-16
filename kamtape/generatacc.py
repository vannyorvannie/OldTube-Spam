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


def generateaccount(email1, username2, password1):
    driver = webdriver.Firefox()
    driver.get("http://www.kamtape.com/signup.php")
    time.sleep(3)
    emailshit = driver.find_element(By.NAME, "field_signup_email")
    emailshit.send_keys(email1)
    username = driver.find_element(By.NAME, "field_signup_username")
    username.send_keys(username2)
    passwd = driver.find_element(By.NAME, "field_signup_password_1")
    # again, retype shit.
    passwd.send_keys(password1)
    passwd2 = driver.find_element(By.NAME, "field_signup_password_2")
    passwd2.send_keys(password1)
    gennedlol = driver.find_element(By.NAME, "signup_button")
    gennedlol.click()
    with open("thisisretarded.txt", "a") as file:
        file.write(f"{username2}:{password1}:{email1}\n")
    driver.quit()

if __name__ == "__main__":
    randedpasswd = generate_password()
    randedusrname = generate_username()
    randedemail = generate_random_email()
    generateaccount(email1=randedemail, username2=randedusrname, password1=randedpasswd)
