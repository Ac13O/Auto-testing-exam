import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# # отображение страницы товара
# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_link_text("My Account").click()
# driver.find_element_by_id("username").send_keys("zil4104@mail.ru")
# driver.find_element_by_id("password").send_keys("Ac!78978977")
# driver.find_element_by_css_selector("input[value='Login']").click()
# driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/shop/']").click()
# driver.find_element_by_css_selector("img[alt='Mastering HTML5 Forms']").click()
# title=driver.find_element_by_css_selector("h1[class='product_title entry-title']")
# if title.text=="HTML5 Forms":
#     print("верная книга")
# else:
#   print("Другая книга")

# # количество товаров в категории
# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_link_text("My Account").click()
# driver.find_element_by_id("username").send_keys("zil4104@mail.ru")
# driver.find_element_by_id("password").send_keys("Ac!78978977")
# driver.find_element_by_css_selector("input[value='Login']").click()
# driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/shop/']").click()
# driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/product-category/html/']").click()
# time.sleep(3)
# count=driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(count)==3:
#     print("3 товара в категории")
# else:
#     print("в категории не 3 товара")


# #сортировка товаров
# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_link_text("My Account").click()
# driver.find_element_by_id("username").send_keys("zil4104@mail.ru")
# driver.find_element_by_id("password").send_keys("Ac!78978977")
# driver.find_element_by_css_selector("input[value='Login']").click()
# driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/shop/']").click()
#
# selector=driver.find_element_by_css_selector("option[value='menu_order']")
# selector_status=selector.get_attribute("selected")
# if selector_status == "true":
#     print("в селекторе выбран вариант сортировки по умолчанию")
# else:
#     print("в селекторе выбран вариант сортировки НЕ по умолчанию")
#
# select=Select(driver.find_element_by_css_selector("select[class='orderby']"))
# select.select_by_visible_text("Sort by price: high to low")
#
# selector=driver.find_element_by_css_selector("option[value='price-desc']")
# selector_status=selector.get_attribute("selected")
# if selector_status == "true":
#     print("в селекторе выбран вариант сортировки от большей цены к меньшей")
# else:
#     print("в селекторе выбран вариант сортировки НЕ от большей цены к меньшей")


#отображение, скидка товара
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("zil4104@mail.ru")
driver.find_element_by_id("password").send_keys("Ac!78978977")
driver.find_element_by_css_selector("input[value='Login']").click()
driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/shop/']").click()
driver.find_element_by_css_selector("img[title='Android Quick Start Guide']").click()
element=driver.find_elements_by_css_selector("p[class='price']")
element_text=element.text
assert element_text=="600"
# assert element_text=="450"
