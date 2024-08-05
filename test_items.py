from selenium.webdriver.common.by import By
import time

def test_button_add_to_basket(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    print('Selected language:', language)
    browser.get(link)
    time.sleep(10)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").is_displayed(), "Add to basket button is not displayed"