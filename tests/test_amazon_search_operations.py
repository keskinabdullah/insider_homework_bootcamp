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

class SearchOperations(unittest.TestCase):

    def setUp(self):
        """TEST ÖNCESİ AMAZON SAYFASINI AÇ, ÇEREZLERİ KAPAT"""
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.home_page.open_amazon()
        self.driver.implicitly_wait(10)
        self.home_page.close_cookie_banner()


    def tearDown(self):
        """Test bitiminde driver'ı kapat"""
        time.sleep(1)
        self.driver.quit()

    def test_home_page(self):
        """AMAZON SAYFASINDA OLDUĞUMUZU DOĞRULA"""
        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://www.amazon.com.tr/", "Amazon Sayfası Bulunamadı")

    def test_go_to_samsung(self):
        """DİNAMİK BİR ŞEKİLDE ÜRÜN ARAMA YAP(BİZ SAMSUNG ARIYORUZ)"""
        self.home_page.search_product("Samsung")
        current_url = self.driver.current_url
        self.assertIn("Samsung", current_url, "Samsung url de yok")

    def test_go_to_product_on_page_2(self):
        """ÜRÜN SAYFASININ İKİNCİ SAYFASINA GEÇİŞ YAP ve DOĞRULA"""
        self.home_page.search_product("Samsung")
        self.home_page.go_to_page_and_click(2)
        current_url = self.driver.current_url
        self.assertIn("Samsung&page=2&", current_url, "Sayfa 2'ye geçilemedi.")
        time.sleep(1)
        screenshot_path = r"C:\Users\Abdullah KESKİN\PycharmProjects\PythonProject\OtomasyonBitirmeProjesi\pages\screenshots\amazon_test.png"
        self.base_page.take_screenshot(screenshot_path)

if __name__ == "__main__":
    unittest.main()