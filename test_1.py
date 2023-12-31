import pytest
from selenium import webdriver
from selenium.webdriver.common.by  import By 
from selenium.webdriver.common.action_chains import ActionChains
import time


def setup_function():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach',True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://lms.ehunar.org/")
    driver.maximize_window()

def teardown_function():
    driver.quit()

def test_login():
    email = 'thehafizsaqib@gmail.com'
    password = 'saqib1122'
    driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(email)
    time.sleep(.5)
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    time.sleep(4)
    # button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/form/button')
    # action = ActionChains(driver)
    # action.move_to_element(button)
    # action.perform()
    
    driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/form/button'))
    # button.click()
    time.sleep(5)
    dashboard = 'https://lms.ehunar.org/dashboard/student_panel'
    loginpanel = driver.current_url
    assert loginpanel == dashboard, "Error"