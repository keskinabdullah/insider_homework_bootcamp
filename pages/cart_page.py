from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class CartPage(BasePage):
    class LocatorsCartPage:
        GO_TO_CART = (By.XPATH,"//a[@id='nav-cart']") #//span[@id='sw-gtc'] ,xpath = "//a[@id='nav-cart']"////span[@id="sw-gtc"]
        CART_HEADER_LOCATOR = (By.XPATH,'//*[@id="sc-active-items-header"]')#doğru ürün mü?
        TRUE_PRODUCT=(By.XPATH,'//h2[@id="sc-active-items-header"]')#Alışveriş başlığı
        REMOVE_BUTTON=(By.XPATH,"//button[@data-action='a-stepper-decrement']")#sepet silme
        SPAN_CART_TEXT=(By.XPATH,'//span[@id="sc-subtotal-label-activecart"]')
        SPAN_LOCATOR=(By.XPATH,'//span[@id="sc-subtotal-label-activecart"]')
        HOME_PAGE_AMAZON=(By.XPATH,'//span[@class="nav-sprite nav-logo-base"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)


    def go_to_cart(self):
        """SEPETE GİT"""
        cart = self.wait.until(EC.element_to_be_clickable(self.LocatorsCartPage.GO_TO_CART))
        cart.click()


    def verify_cart_page(self):
        """SEPET DE OLDUĞUNU DOĞRULA"""
        cart_title_element = self.wait.until(EC.visibility_of_element_located(self.LocatorsCartPage.TRUE_PRODUCT))
        cart_title_text = cart_title_element.text.strip()
        if "Alışveriş Sepeti" in cart_title_text:
            return True
        return False


    def verify_product_in_cart(self):
        """DOĞRU ÜRÜN KONTROLÜ SEPETDE OLUP OLMADIĞI ÜRÜN DEĞİTİĞİ İÇİN SADECE SAMSUNG İLE DOĞRULAMA YAPTIM"""
        product_name_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='a-truncate sc-grid-item-product-title a-size-base-plus']/span[contains(text(),'Samsung')]")))
        product_name = product_name_element.text.strip()
        expected_product_name = "Samsung"
        return expected_product_name in product_name


    def remove_product_from_cart(self):
       """SEPETİ SİL VE 0 ÜRÜN KALDIĞINI DOĞRULA"""
       remove_button = self.wait.until(EC.visibility_of_element_located(*self.LocatorsCartPage.REMOVE_BUTTON))
       remove_button.click()
       time.sleep(1)
       cart_empty_message = self.wait.until(EC.visibility_of_element_located(*self.LocatorsCartPage.SPAN_CART_TEXT))
       return "Ara toplam (0 ürün)" in cart_empty_message.text

    def return_to_home_page(self):
      """AMAZON LOGOSUNU TIKLA VE ANA SAYFAYA DÖN"""
      home_button = self.wait.until(EC.visibility_of_element_located(self.LocatorsCartPage.HOME_PAGE_AMAZON))
      home_button.click()
      self.wait.until(EC.title_contains("Amazon"))
      return "Amazon" in self.driver.title