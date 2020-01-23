from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
current_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_path, 'example.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name("firstname").send_keys("Test")
    browser.find_element_by_name("lastname").send_keys("Testov")
    browser.find_element_by_name("email").send_keys("test@test.com")
    browser.find_element_by_name("file").send_keys(file_path)
    browser.find_element_by_class_name("btn-primary").click()

finally:
    time.sleep(30)
    browser.quit()
