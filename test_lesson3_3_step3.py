from selenium import webdriver
import time
import pytest


def test_abs1():
    browser = webdriver.Chrome()
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        input_f_name = browser.find_element_by_css_selector(
            "input[required].first")
        input_f_name.send_keys("Ivan")
        input_l_name = browser.find_element_by_css_selector(
            "input[required].second")
        input_l_name.send_keys("Petrov")
        input_email = browser.find_element_by_css_selector(
            "input[required].third")
        input_email.send_keys("something@nemail.com")
        time.sleep(1)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        expected_w_text = "Congratulations! You have successfully registered!"
        assert expected_w_text == welcome_text, "Not contain this text"
    finally:
        browser.quit()


def test_abs2():
    browser = webdriver.Chrome()
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        input_f_name = browser.find_element_by_css_selector(
            "input[required].first")
        input_f_name.send_keys("Ivan")
        input_l_name = browser.find_element_by_css_selector(
            "input[required].second")
        input_l_name.send_keys("Petrov")
        input_email = browser.find_element_by_css_selector(
            "input[required].third")
        input_email.send_keys("something@nemail.com")
        time.sleep(1)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        expected_w_text = "Congratulations! You have successfully registered!"
        assert expected_w_text == welcome_text, "Not contain this text"
    finally:
        browser.quit()
