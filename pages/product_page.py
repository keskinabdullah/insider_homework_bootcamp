from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):
    class LocatorsProductPage:
        PRODUCTS_LOCATOR = (By.XPATH, "//div[@role='listitem']")
        THIRD_PRODUCT_LOCATOR = (By.XPATH, "//div[@role='listitem'][3]")
        ADD_TO_CART_LOCATOR = (By.XPATH,'//input[@id="add-to-cart-button"]')
        SUCCESS_MESSAGE_LOCATOR = (By.XPATH, "//h1[contains(text(),'Sepete eklendi')]")


    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)


    def go_to_product_and_click(self, product_no):
        """LİSTELENEN 58 ÜRÜNDEN DİNAMİK OLARAK SEÇ(BİZ ÜÇÜNCÜYÜ SEÇECEĞİZ)"""
        product_locator = f"({self.LocatorsProductPage.PRODUCTS_LOCATOR[1]})[{product_no}]"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, product_locator))
        )
        add_to_button = self.find(By.XPATH, product_locator)
        self.scroll_to_element(add_to_button)
        add_to_button.click()


    def add_to_cart_product(self):
        """SEPETE EKLE VE EKLENDİĞİNİ DOĞRULA"""
        add_product=self.find(*self.LocatorsProductPage.ADD_TO_CART_LOCATOR)
        self.scroll_to_element(add_product)
        add_product.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LocatorsProductPage.SUCCESS_MESSAGE_LOCATOR)
        )

        success_message = self.find(*self.LocatorsProductPage.SUCCESS_MESSAGE_LOCATOR).text
        assert success_message == "Sepete eklendi", f"Beklenen mesaj değil. Gelen mesaj: {success_message}"




