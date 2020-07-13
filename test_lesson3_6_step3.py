import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

list_numbers = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]


# opens and close browser
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('number', list_numbers)
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.implicitly_wait(5)
    # get URL
    browser.get(link)
    # click on the answer spot and input the answer
    spot = browser.find_element_by_css_selector(
        'textarea[placeholder="Напишите ваш ответ здесь..."]')
    answer = str(math.log(int(time.time())))
    spot.click()
    spot.send_keys(answer)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()
    # checking the message to be correct
    message = browser.find_element_by_class_name("smart-hints__hint").text
    assert message == "Correct!", "Incorrect message"

