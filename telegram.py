from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://web.telegram.org/a")


def telegram():
    global driver
    text = input('Enter your txt : ')
    while True:
        try:
            count = int(input('How often do you want to be repeated : '))
            break
        except ValueError:
            print('Please Just Enter Number')
    driver = driver.find_element(By.XPATH,'//*[@id="editable-message-text"]')
    for i in range(count):
        driver.send_keys(text)
        driver.send_keys(Keys.ENTER)
        time.sleep(.2)
    driver.send_keys('CREATOR : ---Mohammad Sajjad Abdinasab---')
    print('Successfully')
    
if __name__ == '__main__':   
    telegram()
    while True:
        ask = input('Run again (y/n) : ')
        if ask.lower() == 'y':
            driver.clear()
            telegram()
        elif ask.lower() == 'n':
            print('Good luck')
            break
        else:
            print('[ y/n ]')
            
            

