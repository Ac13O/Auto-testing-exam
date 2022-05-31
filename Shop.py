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
# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_link_text("My Account").click()
# driver.find_element_by_id("username").send_keys("zil4104@mail.ru")
# driver.find_element_by_id("password").send_keys("Ac!78978977")
# driver.find_element_by_css_selector("input[value='Login']").click()
# driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/shop/']").click()
# driver.find_element_by_css_selector("img[title='Android Quick Start Guide']").click()
# element=driver.find_element_by_css_selector("p[class='price']>del").text
# assert element=="₹600.00"
# element=driver.find_element_by_css_selector("p[class='price']>ins").text
# assert element=="₹450.00"
# driver.find_element_by_css_selector("img[alt='Android Quick Start Guide']").click()
# close=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[class="pp_close"]')))
# close.click()


#проверка цены в корзине
# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/shop/']").click()
# driver.find_element_by_css_selector("a[data-product_id='182']").click()
# time.sleep(3)
# element=driver.find_element_by_css_selector("span[class='cartcontents']").text
# print(element)
# assert element=="1 Item"
# element=driver.find_element_by_css_selector("span[class='amount']").text
# print(element)
# assert element=="₹180.00"
# driver.find_element_by_css_selector("a[title='View your shopping cart']").click()
#
# WebDriverWait(driver,10 ).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr[class='cart-subtotal']"), "180.00"))
# WebDriverWait(driver,10 ).until(EC.text_to_be_present_in_element((By.TAG_NAME, "strong"), ""))

#работа в корзине
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/shop/']").click()
driver.execute_script("window.scrollBy(0,300);")
driver.find_element_by_css_selector("a[data-product_id='182']").click()
time.sleep(3)
button=driver.find_element_by_css_selector("a[data-product_id='180']")
driver.execute_script("return arguments[0].scrollIntoView(true);",button)
button.click()
time.sleep(4)
driver.find_element_by_css_selector("a[title='View your shopping cart']").click()
time.sleep(2)
driver.find_element_by_css_selector("a[class='remove']").click()
time.sleep(2)
driver.find_element_by_link_text("Undo?"). click()
driver.find_element_by_css_selector("input[name='cart[4c5bde74a8f110656874902f07378009][qty]']").clear()
driver.find_element_by_css_selector("input[name='cart[4c5bde74a8f110656874902f07378009][qty]']").send_keys("3")
time.sleep(1)
driver.find_element_by_css_selector("input[name='update_cart']").click()
qty=driver.find_element_by_css_selector("input[name='cart[4c5bde74a8f110656874902f07378009][qty]']")
value_qty=qty.get_attribute("value")
print(value_qty)
assert value_qty=="3"
time.sleep(1)
driver.find_element_by_css_selector("input[name='apply_coupon']").click()
time.sleep(2)
text=driver.find_element_by_tag_name("body").text
# print(text)
assert "Please enter a coupon code." in text

