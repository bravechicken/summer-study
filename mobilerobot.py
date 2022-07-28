from appium.webdriver.common.appiumby import AppiumBy 
# https://zhuanlan.zhihu.com/p/144737398
import unittest
import selenium
import time
from appium import webdriver
 
class MyTestCase(unittest.TestCase):

    def setUp(self):
        # super().setUp()
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11.0.0'
        desired_caps['deviceName'] = '21091116C'
        # desired_caps['appPackage'] = "com.sankuai.meituan"
        # desired_caps['appActivity'] = "com.meituan.android.pt.homepage.activity.MainActivity"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
 
    def testWaimai(self):

        el1 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"时钟\"]")
        el1.click()
    def tearDown(self):
        self.driver.quit()
 
# python test_meituan.py 
if __name__ == '__main__':
    unittest.main()