from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest

class TestPython(unittest.TestCase):
 def test_three_image_go_to_ivi(self):
  driver = webdriver.Chrome()
  driver = self.driver
  driver.get("https://www.google.com/")
  driver.find_element_by_id("gbqfq").send_keys("ivi")
