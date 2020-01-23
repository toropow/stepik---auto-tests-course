from selenium import webdriver
import time

link_good = "http://suninjuly.github.io/registration1.html"
link_fail = "http://suninjuly.github.io/registration2.html"

link = link_good

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # FirstName
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    # LastName
    input2 = browser.find_element_by_class_name("second")
    input2.send_keys("Petrov")
    # Email
    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("test@test.com")

    # Phone
    input4 = browser.find_element_by_xpath('//input[@placeholder="Input your phone:"]')
    input4.send_keys("+79123211122")

    # Address
    input5 = browser.find_element_by_xpath('//input[@placeholder="Input your address:"]')
    input5.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
