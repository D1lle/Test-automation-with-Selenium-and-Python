from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)
    # Finding numbers and getting them sum
    a = browser.find_element_by_id("num1").text
    b = browser.find_element_by_id("num2").text
    answer = str(int(a) + int(b))
    # Finding the sum in dropdown
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(answer)
    # Clicking the button
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # copy the answer
    time.sleep(10)
    browser.quit()
