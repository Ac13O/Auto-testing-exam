import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

#Регистрация аккаунта
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click() #2
driver.find_element_by_id("reg_email").send_keys("zil4104@mail.ru") #3
driver.find_element_by_id("reg_password").send_keys("Ac!78978977") #4
driver.find_element_by_css_selector("input[name='register']").click() #5


# логин в систему
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("zil4104@mail.ru")
driver.find_element_by_id("password").send_keys("Ac!78978977")
driver.find_element_by_css_selector("input[value='Login']").click() #5
element=driver.find_element_by_tag_name("html") #6
checking=element.text #6
assert "Logout" in checking #6
1
