from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time, pathlib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wallet_to_array():
    file = "password.txt"
    arr = []
    with open(file, encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            arr.append(line.strip())
    return arr[0]

def buy_lot(driver, password):
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//button[@class="tw-inline-flex tw-justify-center tw-items-center tw-rounded-md tw-text-white-1 BorderedButton_btn__2Glkn"]'))).click()
    driver.find_element_by_class_name("wallet-adapter-button ").click()
    while True:
        if len(driver.window_handles)>1:
            break
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    try:
        driver.find_element_by_xpath("//button[@class='tw-inline-flex tw-justify-center tw-items-center tw-rounded-md tw-text-white-1 BorderedButton_btn__2Glkn']").click()
        while True:
            if len(driver.window_handles)>1:
                break
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_xpath("//button[@type='submit']").click()
    except Exception:
        pass

    while True:
        try:
            driver.find_element_by_xpath('//button[@class="me-btn d-inline-flex justify-content-center align-items-center gradientBorder"]').click()
            if len(driver.window_handles)>1:
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(.3)
                try:
                    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
                    driver.find_element_by_xpath("//button[@type='submit']").click()
                except Exception:
                    pass
                driver.find_element_by_xpath("//button[@type='submit']").click()
                driver.switch_to.window(driver.window_handles[0])
            break
        except Exception:
            pass
            

def main(password):
    link = input("Введите ссылку на мероприятие: ")
    
    opt = webdriver.ChromeOptions()
    opt.add_argument(f'--user-data-dir={pathlib.Path().resolve()}/chrome_profile')
    #opt.add_argument("--log-level=3")
    opt.add_argument("--no-sandbox")
    #opt.add_argument('--headless')
    opt.add_argument('--start-maximized')
    #opt.add_argument('--disable-dev-shm-usage')
    opt.add_argument('--allow-running-insecure-content')
    opt.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options=opt, executable_path=f"{pathlib.Path().resolve()}/chromedriver")
    driver.get(link)
    buy_lot(driver, password)

main(wallet_to_array())