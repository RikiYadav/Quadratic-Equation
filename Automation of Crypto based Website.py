import time
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import getpass

# searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys('hitesh')
options = webdriver.ChromeOptions()
options.add_argument(
    "user-data-dir=C:\\Users\\Rikiy\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(
    executable_path=r'C:\\Users\\Rikiy\\OneDrive\\Desktop\\Programming\\chromedriver_win32\\chromedriver.exe', chrome_options=options)


driver.get("https://earnzads.com/")


def maintask():
    print("Main Task Started !")
    username = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/form/div/center/input")
    username.send_keys('0xbf899B2386F02dc20548bBb38a4ab706047b98C1')
    print("Wallet Number is Given !")

    button = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/form/button")
    button.click()
    print("Submit Button is clicked !")

    next = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/form/button/span")
    next.click()
    print("Button Next is Clicked !")

    # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
    #     (By.NAME, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
    
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    #     (By.XPATH, '//*[@id="solver-button"]'))).click()

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()


    driver.find_element_by_css_selector("#solver-button").click()



    # vbutton =driver.find_element_by_xpṇth("//
    [@id="solver-button"]")
    # vbutton.click()


maintask()
