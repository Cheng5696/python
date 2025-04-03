from bs4 import BeautifulSoup
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
import sqlite3

def web(url):
    """有界面浏览器"""
    browser = webdriver.Chrome()  # 初始化浏览器为chrome浏览器
    browser.get(url)
    # 设置等待时间10s
    wait = WebDriverWait(browser, 10)
    try:
        # 等待初始页面加载完成
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,"search-input-box")))
        while True:
            # 返回当前页面数据
            time.sleep(1)
            yield browser.page_source # 返回页面内容给外部运算

            try:
                # 加载下一页
                next_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"ui-icon-arrow-right")))
                next_btn.click()
                wait.until(EC.staleness_of(next_btn))
            except TimeoutException:
                print("已经最后一页了")
                break
    finally:
        browser.close()


def save(gw,gz,gs,rs,lj,dq):
    try:
        # 1.建立数据库链接->这里改成你的数据库名称
        con = sqlite3.connect("data.db")
        # 2. 创建游标对象
        cursor = con.cursor()
        # 3. 执行SQL插入操作 -> sql语句，和变量名要改
        sql = "INSERT INTO work(岗位,工资,公司,公司人数,详情链接,地区) VALUES(?,?,?,?,?,?)"
        cursor.execute(sql, [gw,gz,gs,rs,lj,dq])
        # 4. 提交数据库事务
        con.commit()
        print("插入数据库成功")
    except sqlite3.Error as e:
        print(f"插入数据库失败:{e}")
        # 回滚数据库事务
        con.rollback()
    finally:
        # 关闭游标
        if cursor:
            cursor.close()
            # 关闭数据库链接
        if con:
            con.close()


def soup(html):
    soup = BeautifulSoup(html, "lxml")
    # print(soup.prettify())  # 查看完整解析
    lis = soup.find_all("li",class_="job-card-wrapper")
    for li in lis:
        # print("------------------------------------------------------------------------")
        # print(li.find("span",class_="job-name").text)# 岗位名字
        # print(li.find("span",class_="salary").text) # 工资
        # print(li.find("h3",class_="company-name").text) # 公司
        # print(li.find("ul",class_="company-tag-list").text)  # 公司tag
        # print(li.find("a",class_="job-card-left").text +"      "+ "https://www.zhipin.com/"+li.find("a",class_="job-card-left").get("href"))  # 公司链接
        # print(li.find("span",class_="job-area").text) # 公司地址
        save(li.find("span",class_="job-name").text,
             li.find("span", class_="salary").text,
             li.find("h3", class_="company-name").text,
             li.find("ul", class_="company-tag-list").text,
             "https://www.zhipin.com" + li.find("a",class_="job-card-left").get("href"),
             li.find("span", class_="job-area").text
             )

if __name__ == "__main__":
    for page_source in web(r"https://www.zhipin.com/web/geek/job?query=python&city=101280600"):
        soup(page_source)




