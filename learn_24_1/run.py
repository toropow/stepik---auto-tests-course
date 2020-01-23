from selenium import webdriver
from selenium.webdriver.support import expected_conditions  as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    price_value = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), str(100))
    )
    btn = browser.find_element(By.CLASS_NAME, "btn-primary").click()
    num = browser.find_element(By.ID, "input_value").text
    result = calc(num)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(30)
    browser.quit()
