from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    blue_btn = browser.find_element_by_class_name("btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    num = browser.find_element_by_id("input_value").text
    result = calc(num)
    input_field = browser.find_element_by_id("answer").send_keys(str(result))
    browser.find_element_by_class_name("btn-primary").click()

finally:
    time.sleep(15)
    browser.quit()
