from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/" \
       "coders-at-work_207/"


def test_finding_add_to_basket_button(browser):
    browser.get(link)
    # 15 second to look, that language was changed
    # time.sleep(15)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket"))
    )
    # If such button is available, we won't see an exception
    assert button, "No such button"
