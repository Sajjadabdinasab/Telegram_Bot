# Test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://web.telegram.org/a")

runner = 0
def telegram():
    global driver
    def sender():
        global driver
        text = input('Enter your txt : ')
        count = int(input('How often do you want to be repeated : '))
        driver = driver.find_element(By.XPATH,'//*[@id="editable-message-text"]')
        for i in range(count):
            driver.send_keys(text)
            driver.send_keys(Keys.ENTER)
            time.sleep(.2)
        driver.send_keys('CREATOR : ---Mohammad Sajjad Abdinasab---')
        print('Successfully')
    if runner == 0:
        user_name = input('Enter username : ')
        driver = driver.find_element(By.ID,'telegram-search-input')
        driver.send_keys('{}'.format(user_name))
        time.sleep(1)
        driver.send_keys(Keys.ENTER)
        sender()
    else:
        sender()
   
if __name__ == '__main__':   
    telegram()
    runner = 1
    while True:
        ask = input('Run again (y/n) : ')
        if ask == 'y':
            telegram()
        elif ask == 'n':
            print('Good luck')
            break
        else:
            print('[ y/n ]')
            
            

