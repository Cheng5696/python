from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""有界面浏览器"""
browser = webdriver.Chrome()  # 初始化浏览器为chrome浏览器
browser.get(r'https://www.baidu.com/')

# 设置等待时间10s
wait = WebDriverWait(browser, 10)

wait.until(EC.presence_of_element_located((By.ID, "xxx")))
browser.close()  # 关闭浏览器