#导入webdriver
from selenium import webdriver
import time
#使用Chrome
driver = webdriver.Chrome()
#打开site
driver.get("https://www.bing.com")
#最大化窗口
driver.maximize_window()
#停留3秒
time.sleep(3)
#退出
driver.quit()