from selenium import webdriver
from time import sleep

class TestKey(object):
    #初始化关键字驱动类
    def __init__(self,browser_type):
        self.driver = self.open_browser(browser_type)

    def open_browser(self,browser_type):
        if browser_type == 'chrome':
            self.driver=webdriver.Chrome()
        elif browser_type == 'ff':
            self.driver=webdriver.Firefox()
        elif browser_type == 'ie':
            self.driver=webdriver.Ie()
        else:
            self.driver= 'browser_type error'

            return self.driver
    def visit(self,url):
        self.driver.get(url)

    def element_locator(self,locator_type,locator):
        if locator_type == 'id':
            el= self.driver.find_element_by_id(locator)
        elif locator_type == 'xpath':
            el=self.driver.find_element_by_xpath(locator)
        elif locator_type == 'name':
            el=self.driver.find_element_by_name(locator)
        else:
            el='locator error'
        return el


    def input_txt(self,locator_type,locator,txt):
        self.element_locator(locator_type,locator).send_keys(txt)

    def element_click(self,locator_type,locator):
        self.element_locator(locator_type,locator).click

    def quite(self):
        self.driver.quit()

    def wait(self,time):
        sleep(time)

