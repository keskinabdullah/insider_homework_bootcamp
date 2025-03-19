from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,timeout= 12)

    def get_current_url(self):
        """Sayfanın geçerli URL'sini döndürür"""
        return self.driver.current_url

    def find(self,*locator):
        return  self.driver.find_element(*locator)


    def click_element(self,*locator):
        self.driver.find_element(*locator).click()

    def take_screenshot(self, file_path):
        """Sayfanın ekran görüntüsünü al"""
        self.driver.save_screenshot(file_path)


    def hover_element(self,*locator):
        element=self.find(*locator)
        hover=ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_element(self, *locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def get_text(self,locator):
        return self.wait_element(locator).text

    def take_screenshot(self, file_path):
        """Sayfanın ekran görüntüsünü al"""
        self.driver.save_screenshot(file_path)
        print(f"Ekran görüntüsü kaydedildi: {file_path}")




