import time
import os
import random
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException


def option_config():
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--disable-javascript')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # options.add_argument('blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
    # driver.implicitly_wait(3)
    return driver


def screenshot(driver, number, file_directory="pic"):
    try:
        driver.get(f"https://t.17track.net/zh-cn#nums={number}")
        time.sleep(random.randint(4, 7))
        try:
            driver.find_element_by_xpath('//div[@class="introjs-tooltipbuttons"]/a[1]').click()
        except NoSuchElementException:
            prc_filename_bool(number)
            driver.find_element_by_class_name("yqcr-details").screenshot(f"./{file_directory}/{number}.png")
            # driver.get_screenshot_as_file(f"./pic/{number}.png")
        else:
            prc_filename_bool(number)
            driver.find_element_by_class_name("yqcr-details").screenshot(f"./{file_directory}/{number}.png")
            # driver.get_screenshot_as_file(f"./pic/{number}.png")
        time.sleep(random.randint(6, 10))
    except NoSuchElementException:
        return


def prc_filename_bool(name, file_directory="pic"):
    file = f"./{file_directory}/{name}.png"
    if os.path.exists(file):
        os.remove(file)


def creat_file(file_directory="pic"):
    if not os.path.exists(file_directory):
        os.mkdir(file_directory)


if __name__ == '__main__':
    drivers = option_config()
    creat_file()
    lists = []
    with open('pic.csv', 'r', encoding="utf-8") as f:
        data = csv.reader(f)
        for i in data:
            screenshot(drivers, i[0])
            print(f"{i[0]}.png已保存")




