from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class TestPython(unittest.TestCase):
    def test_three_image_go_to_ivi(self):
        # Указываем путь до chromedriver
        self.driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
        self.driver.implicitly_wait(30)
        driver = self.driver
        # Открываем необходимый урл
        driver.get("https://www.google.com/")
        # Вводим значение ivi в поисковую строку, нажимаем enter
        driver.find_element_by_class_name("gLFyf").send_keys("ivi")
        driver.find_element_by_class_name("gLFyf").send_keys(Keys.ENTER)
        # Переходим на картинки
        driver.find_element_by_xpath("//a[@data-hveid='CAEQBQ']").click()
        # Считаем количество ссылок на ivi
        img_urls = driver.find_elements_by_class_name("fxgdke")
        ivi_url_count = 0
        for i in img_urls:
            if i.text == "ivi.ru":
                ivi_url_count += 1
        ivi_url_min = 2
        # Проверяем, что их не меньше 3
        assert ivi_url_count > ivi_url_min
