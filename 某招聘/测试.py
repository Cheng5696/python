
options = webdriver.ChromeOptions()
options.binary_location = r"E:\miniconda\envs\test\Scripts\chrome-win64\chrome.exe"  # 指向具体路径的浏览器程序
"""有界面浏览器"""
 browser = webdriver.Chrome(options=options)  # 初始化浏览器为chrome浏览器
    browser.get(url)