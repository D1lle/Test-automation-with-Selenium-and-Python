from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    # getting a list of places for input
    # and fill them
    elements = browser.find_elements_by_css_selector("input")
    for element in elements:
        element.send_keys("Hell Yeah!")

    # click the bottom in the end
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # copy the answer
    time.sleep(30)
    browser.quit()
