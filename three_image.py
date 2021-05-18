from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


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
        print(len(driver.find_elements_by_class_name("fxgdke")))
        ivi_url_count = 0
        for i in driver.find_elements_by_class_name("fxgdke"):
            print(driver.find_element_by_class_name("fxgdke").text)
            if driver.find_element_by_class_name("fxgdke").text == "ivi.ru":
                ivi_url_count += 1
        print(ivi_url_count)
        # Считаем количество картинок с урлом на ivi.ru, убеждаемся, что их не менее 3
        #ivi_url = len(driver.find_element_by_class_name("fxgdke").text("ivi.ru"))
        #ivi_url = len(driver.find_element_by_xpath("//a[@data-hveid='CAEQBQ']"))
        #ivi_url_min = 2
        #assert ivi_url > ivi_url_min
        time.sleep(5)

"""
    def test_wiki_go_to_ivi(self):
        # Указываем путь до chromedriver
        self.driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
        self.driver.implicitly_wait(30)
        driver = self.driver
        # Открываем необходимый урл
        driver.get("https://www.google.com/")
        # Вводим значение ivi в поисковую строку, нажимаем enter
        driver.find_element_by_class_name("gLFyf").send_keys("ivi")
        driver.find_element_by_class_name("gLFyf").send_keys(Keys.ENTER)
        # Ищем статью на википедию на первых 5 страницах
        try:
            assert driver.find_element_by_xpath("//a[@href='https://ru.wikipedia.org/wiki/Ivi.ru']")
        except
        time.sleep(5)
"""
