import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class HomePage(BasePage):
    class LocatorsHomePage:
        SEARCH_BOX_LOCATOR = (By.XPATH, '//input[@id="twotabsearchtextbox"]')
        SEARCH_BUTTON_LOCATOR = (By.XPATH, "//input[@id='nav-search-submit-button']")
        CLOSE_COOKIE_BANNER_LOCATOR = (By.CSS_SELECTOR,'span[id="a-autoid-1"]')
        PAGES_LOCATOR= (By.XPATH, '//li[@class="s-list-item-margin-right-adjustment"]')



    def __init__(self, driver):
        super().__init__(driver)


    def open_amazon(self):
        """AMAZON SAYFASINA GİT"""
        self.driver.get('https://www.amazon.com.tr')
        self.wait_element(*self.LocatorsHomePage.SEARCH_BOX_LOCATOR)


    def close_cookie_banner(self):
        """SAYFADA ÇIKAN ÇEREZİ KAPAT"""
        self.click_element(*self.LocatorsHomePage.CLOSE_COOKIE_BANNER_LOCATOR)


    def search_product(self, product_name):
        """ARAMA KUTUSUNA ÜRÜN GİR VE ARAMA YAP"""
        self.wait_element(*self.LocatorsHomePage.SEARCH_BOX_LOCATOR)
        search_box = self.find(*self.LocatorsHomePage.SEARCH_BOX_LOCATOR)
        search_box.send_keys(product_name)
        self.click_element(*self.LocatorsHomePage.SEARCH_BUTTON_LOCATOR)


    def go_to_page_and_click(self,page_no):
        """SAYFALAR BUTAONUNA KAYDIR VE 2. SAYFAYA TIKLA"""
        page_locator = f"({self.LocatorsHomePage.PAGES_LOCATOR[1]})[{page_no}]"
        WebDriverWait(self.driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, page_locator))
        )
        page_button = self.find(By.XPATH, page_locator)
        self.scroll_to_element(page_button)
        page_button.click()






