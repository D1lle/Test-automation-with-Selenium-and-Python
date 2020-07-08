from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # clicking the button when the price became $100
    button = browser.find_element_by_css_selector("button#book")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button.click()

    # scrolling to equation and solve it
    scrolling = browser.find_element_by_id("input_value")
    browser.execute_script("arguments[0].scrollIntoView();", scrolling)
    scrolling.click()

    x_element = browser.find_element_by_id("input_value").text
    y_element = calc(x_element)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(str(y_element))

    button2 = browser.find_element_by_id("solve").click()

finally:
    time.sleep(15)
    browser.quit()
