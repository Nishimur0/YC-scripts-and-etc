from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

asd = webdriver.Chrome()
link = 'https://www.yclients.com/signin/'
login = str(input())
password = str(input())
goods = []
Flag = True
while Flag == True:
    good_link = input()
    if good_link.lower() not in ('y', 'н'):
        goods.append(good_link)
    else:
        Flag = False

try:
    asd.get(link)
    asd.maximize_window()
    button = WebDriverWait(asd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))
    logn = asd.find_element(By.CSS_SELECTOR, "[name='email']")
    logn.click()
    logn.send_keys(login)
    paswd = asd.find_element(By.CSS_SELECTOR, '[type="password"]')
    paswd.click()
    paswd.send_keys(password)
    button.click()
    time.sleep(4)
    for good_li in goods:
        asd.get(good_li)
        button = WebDriverWait(asd, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/form/div[17]/div/button')))
        button.click()
        try:
            WebDriverWait(asd, 1).until(EC.alert_is_present())
            alert = asd.switch_to.alert
            alert.dismiss()
        except TimeoutException:
            print("Alert не появился")
        time.sleep(3)
finally:
    asd.quit()