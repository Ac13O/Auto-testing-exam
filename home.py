import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

#2
driver.execute_script("window.scrollBy(0,600);")

#3
driver.find_element_by_css_selector("img[title='Selenium Ruby']").click()

#4
driver.find_element_by_css_selector("a[href='#tab-reviews']").click()

#5
driver.find_element_by_css_selector("a[class='star-5']").click()

#6
driver.find_element_by_id("comment").send_keys("Nice ")

#7
driver.find_element_by_id("author").send_keys("Ivanov")

#8
driver.find_element_by_id("email").send_keys("Ivanov@m.ru")

#9
driver.find_element_by_id("submit").click()


