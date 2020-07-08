from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/registration1.html"
    # link = "http://suninjuly.github.io/registration2.html"
    # In second link three will NoSuchElementException
    # because of form, that changed
    
    browser.get(link)

    # Filling in the required fields
    input_f_name = browser.find_element_by_css_selector(
        "input[required].first")
    input_f_name.send_keys("Ivan")
    input_l_name = browser.find_element_by_css_selector(
        "input[required].second")
    input_l_name.send_keys("Petrov")
    input_email = browser.find_element_by_css_selector("input[required].third")
    input_email.send_keys("something@nemail.com")

    # Submit the completed form
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Verifying that the registration was successful
    time.sleep(1)

    # Finding the element, that contains text
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # Checking the correct code execution
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # copy the answer
    time.sleep(10)
    browser.quit()
