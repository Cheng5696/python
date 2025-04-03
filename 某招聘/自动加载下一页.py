import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException

def web(url):
    """有界面浏览器"""
    browser = webdriver.Chrome()  # 初始化浏览器为chrome浏览器
    browser.get(url)
    # 设置等待时间10s
    wait = WebDriverWait(browser, 10)
    try:
        # 等待直到页面上存在该元素，如果超过设定的等待时间仍未找到该元素，会抛出 TimeoutException 异常
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,"search-input-box")))
        while True:
            # 返回当前页面数据
            time.sleep(1)
            yield browser.page_source # 返回页面内容给外部运算

            try:
                # 等待(<10s)元素可见且可被点击时，返回该元素对象
                next_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"ui-icon-arrow-right")))
                next_btn.click()
                # 等待(<10s)元素已从 DOM 中移除或失效
                wait.until(EC.staleness_of(next_btn))
            except TimeoutException:
                print("已经最后一页了")
                break
    finally:
        browser.close()

for page_source in web("xxxxxxxx"):
    print(page_source)