from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

asd = webdriver.Chrome()
link = 'https://www.yclients.com/signin/'
login = str(input())
password = str(input())
link2 = 'https://yclients.com/shared_goods/69994/edit/26055362/'
code = '1.207576359389E'

list_of_goods = [26055362]
salons = []
Flag = False
while Flag != True:
    a = input()
    if a != 'y':
        salons.append(str(a))
    else:
        Flag = True


try:
    asd.get(link)
    asd.maximize_window()
    button = WebDriverWait(asd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))
    logn = asd.find_element(By.CSS_SELECTOR, "[name='email']")
    logn.click()
    logn.send_keys(login)
    paswd = asd.find_element(By.CSS_SELECTOR, '[type="password"]')
    paswd.click()
    paswd.send_keys(password)
    button.click()
    time.sleep(4)
    actions = ActionChains(asd)
    for i in range(len(list_of_goods)):
        link3 = f'https://yclients.com/shared_goods/69994/edit/{list_of_goods[i]}/'
        asd.get(link3)
        salon_chioses = asd.find_element(By.CSS_SELECTOR, '[href="#goods-salons"]')
        salon_chioses.click()
        salons_add = asd.find_elements(By.CLASS_NAME, 'checkbox')
        

        for j in range(len(salons)):
            salons_chekbox = asd.find_element(By.CSS_SELECTOR, f'[value="{salons[j]}"]')

            actions.move_to_element(salons_chekbox).perform()
            time.sleep(0.3)
            print(f'[value="{salons[j]}"]')
            salons_chekbox.click()


    time.sleep(8)

finally:
    asd.quit()