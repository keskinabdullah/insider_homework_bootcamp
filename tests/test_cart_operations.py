import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class CartOperations(unittest.TestCase):

    def setUp(self):
        """TEST ÖNCESİ SEPETTE OLMALISIN"""
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.home_page.open_amazon()
        self.driver.implicitly_wait(10)
        self.home_page.close_cookie_banner()
        self.home_page.search_product("Samsung")
        self.home_page.go_to_page_and_click(2)
        self.product_page.go_to_product_and_click(3)
        self.product_page.add_to_cart_product()
        self.cart_page.go_to_cart()


    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test_remove_cart(self):
       self.assertTrue(self.cart_page.remove_product_from_cart(), "Ürün sepette silinemedi")

    def test_cart_page_return_home_page(self):
        self.assertTrue(self.cart_page.return_to_home_page(), "Ana sayfaya dönülemedi")

        screenshot_path = r"C:\Users\Abdullah KESKİN\PycharmProjects\PythonProject\OtomasyonBitirmeProjesi\pages\screenshots\cart_test.png"
        base_page.take_screenshot(screenshot_path)

if __name__ == "__main__":
    unittest.main()