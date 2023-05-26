import time
import yaml
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

with open('C:/Users/alexa/OneDrive/Рабочий стол/Selenium/Seminar/testdata.yaml') as f:
    testdata = yaml.safe_load(f)

service = Service(testdata['driver_path'])
options = webdriver.FirefoxOptions()

class Site:
    def __init__(self, address):
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata['sleep_time'])