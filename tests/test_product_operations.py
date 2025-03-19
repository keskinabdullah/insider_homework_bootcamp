import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class ProductOperations(unittest.TestCase):


    def setUp(self):
        """SAMSUNG İKİNCİ SAYFASINDA OLMAK ÖN KOŞUL"""
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



    def tearDown(self):
        time.sleep(1)
        self.driver.quit()


    def test_products_on_page_2_product_selection(self):
        """SEÇİLEN ÜRÜNÜ SEPETE EKLE"""
        self.product_page.go_to_product_and_click(3)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.product_page.LocatorsProductPage.ADD_TO_CART_LOCATOR))
        self.product_page.add_to_cart_product()
        print("Ürün başarıyla sepete eklendi.")


    def test_go_to_cart(self):
        """SEPETE GİT"""
        self.product_page.go_to_product_and_click(3)
        #ÜRÜNÜ SEPETE EKLE
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.product_page.LocatorsProductPage.ADD_TO_CART_LOCATOR))
        self.product_page.add_to_cart_product()
        #SEPETE GİT
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cart_page.LocatorsCartPage.GO_TO_CART))
        self.cart_page.go_to_cart()
        self.assertTrue(self.cart_page.verify_cart_page(), "Sepet sayfasına gidilemedi")
        self.assertTrue(self.cart_page.verify_cart_page(), "Sepet sayfasına gidilemedi")
        screenshot_path = r"C:\Users\Abdullah KESKİN\PycharmProjects\PythonProject\OtomasyonBitirmeProjesi\pages\screenshots\product_test.png"
        self.base_page.take_screenshot(screenshot_path)
















if __name__ == "__main__":
    unittest.main()