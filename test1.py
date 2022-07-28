# An highlighted block
from appium import webdriver
import time
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'#mumu模拟器-设置-关于平板电脑-Android版本
desired_caps['deviceName'] = '127.0.0.1:7555'#设备号
desired_caps['appPackage'] = 'com.android.settings'#包名
desired_caps['appActivity'] = 'com.android.settings.Settings'#界面名
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#4723为appium设置的端口号
time.sleep(5)
driver.quit()