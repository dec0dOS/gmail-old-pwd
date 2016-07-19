from random import randint
from time import sleep
from selenium import webdriver
from config import username, password, delay
import logging
# Init logging
logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s',
                    filename='logs.txt', level=logging.INFO)
# Next line is used for displaying logs to stdout
logging.getLogger().addHandler(logging.StreamHandler())
logging.info("File: {}".format(__file__))

url = 'https://accounts.google.com/ServiceLogin?service=accountsettings&passive=1209600&osid=1&continue=https://myaccount.google.com/security/signinoptions/password&followup=https://myaccount.google.com/security/signinoptions/password&emr=1&mrp=security&rart=ANgoxceHpBk99jwXaPPZ17NJZyn3WdtaxRQSP0HIjufJ0CV-hNdEBV2yK4fdJou3dmkPxpRtSLzsX9LL6qhinPYMQo4ABSWc5w&authuser=0'
browser = webdriver.Chrome()


def main(username, password, url):
    browser.get(url)
    logging.info("Successfully opened url")
    browser.find_element_by_id("Email").send_keys(username)
    browser.find_element_by_id("next").click()
    logging.info("Entered username")
    sleep(delay)
    browser.find_element_by_id("Passwd").send_keys(password)
    browser.find_element_by_id("signIn").click()
    logging.info("Successfully logged in")
    sleep(delay + 1)
    x = 0
    while x < 100:
        new_password = str(randint(1000000, 9999999)) + "Zz"
        logging.info("New password: {}".format(new_password))
        browser.find_element_by_xpath(
            '//*[@id="view_container"]/div/div/div[3]/div[1]/div/div[1]/div/div[1]/div/div[1]/input').send_keys(new_password)
        logging.info("Entered new password")
        browser.find_element_by_xpath(
            '//*[@id="view_container"]/div/div/div[3]/div[1]/div/div[3]/div/div[1]/div/div[1]/input').send_keys(new_password)
        logging.info("Entered confirm")
        browser.find_element_by_xpath(
            '//*[@id="view_container"]/div/div/div[3]/div[2]/div/content/span').click()
        logging.info("Pressed confirm button")
        sleep(delay + 1)
        browser.get("https://accounts.google.com/ServiceLogin?service=accountsettings&passive=1209600&osid=1&continue=https://myaccount.google.com/security/signinoptions/password&followup=https://myaccount.google.com/security/signinoptions/password&emr=1&mrp=security&rart=ANgoxcffr2RoEQID0DEcYVPS-AgbMryiK81dcw26wK0uuIwNDR3RU7i-duA7EY5S8B8JttKgUGmvkKFlK9_7fY36QqECnPmgXg&authuser=0")
        browser.find_element_by_id("Passwd").send_keys(new_password)
        browser.find_element_by_id("signIn").click()
        x = x + 1
        sleep(delay)

if __name__ == '__main__':
    try:
        main(username, password, url)
    except Exception as e:
        logging.error("------------------------------------")
        logging.exception('')
        logging.error("------------------------------------")
    logging.info("------------------------------------")
