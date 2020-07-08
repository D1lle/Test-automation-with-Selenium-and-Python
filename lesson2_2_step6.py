from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
# This is complicated previous task by necessity of scrolling the page
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x_el = x_element.text
    y = calc(x_el)

    scrolling = browser.find_element_by_id("input_value")
    browser.execute_script("arguments[0].scrollIntoView();", scrolling)
    scrolling.click()

    input_solution = browser.find_element_by_css_selector("#answer")
    input_solution.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
