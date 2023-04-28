"""
爬虫提取豆瓣前250的书https://book.douban.com/top250
时间 ： 2023/04/18
"""
import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

for start_num in range(0,250,25):

    response = requests.get(f"https://book.douban.com/top250?start={start_num}",headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    all_titles = soup.findAll("div",attrs={"class":"pl2"})
    for item in all_titles:
        titles = item.findAll("a")
        for title in titles :
            print(title.attrs["title"])

"""
总结
response = requests.get("https://book.douban.com/top250",headers=headers)  返回了一个 Response实例，就是服务器给我们的包
html = response.text       Response包的text属性是一个字符串表示html正文
soup =BeautifulSoup(html,"html.parser")   可以将这个字符串，转换成BeautifulSoup对象
all_titles =soup.findAll("div",attrs={"class":"pl2"})  这个BeautifulSoup对象可以将特定的标签对象组合成一个列表返回
for item in all_titles:  将all_titles列表遍历，得到item的标签Tag对象    
    Tag对象.name  --> 标签的名字
    Tag对象.attrs --> 标签属性的字典
    Tag对象["title"]  --> 取标签某个属性
"""
