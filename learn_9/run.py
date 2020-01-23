from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    result = str(int(num1) + int(num2))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(result)
    btn = browser.find_element_by_class_name("btn-default")
    btn.click()


finally:
    time.sleep(30)
    browser.quit()
