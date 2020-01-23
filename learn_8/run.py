from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    text_block_question = browser.find_element_by_id("treasure").get_attribute("valuex")
    result = calc(text_block_question)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(result)
    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()
    radio_btn = browser.find_element_by_id("robotsRule")
    radio_btn.click()
    btn_submit = browser.find_element_by_class_name("btn-default")
    btn_submit.click()

finally:
    time.sleep(30)
    browser.quit()
