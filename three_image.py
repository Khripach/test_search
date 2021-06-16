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
        assert ivi_url_count > ivi_url_min, 'Количество картинок, ведущих на ivi меньше 3'

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
        # Ищем статью на википедию про ivi на первых 5 страницах
        for i in range(5):
            try:
                driver.find_element_by_xpath("//a[@href='https://ru.wikipedia.org/wiki/Ivi.ru']").click()
                if driver.current_url == 'https://ru.wikipedia.org/wiki/Ivi.ru':
                    break
            except:
                print('Не нашли ссылку на википедию про ivi на странице', i+1)
            # Кликаем на следующую страницу в поисковом запросе
            driver.find_element_by_css_selector('[aria-label="Page '+str(i+2)+'"]').click()
        # Проверяем, что нашли статью на википедию про ivi и перешли на неё
        assert driver.current_url == 'https://ru.wikipedia.org/wiki/Ivi.ru', \
            'Не нашли ссылку на википедию про ivi на первых 5 страницах'
        # Проверяем, что в статье википедии про ivi есть ссылка на официальный сайт ivi
        assert driver.find_element_by_xpath("//a[@href='http://ivi.ru']"), 'Не нашли ссылку на ivi в статье википедии'
