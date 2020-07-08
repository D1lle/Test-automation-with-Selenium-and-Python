from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    # finding the x-value in treasure and calculating
    treasure = browser.find_element_by_id("treasure")
    treasure_x = treasure.get_attribute("valuex")
    y = calc(int(treasure_x))
    # input the result
    input_solution = browser.find_element_by_css_selector("#answer")
    input_solution.send_keys(y)
    # Clicking on checkbox and radiobutton
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    # Clicking on the button
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # copy the answer
    time.sleep(10)
    browser.quit()
