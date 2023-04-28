"""
请求http协议，并且判断
获取http://books.toscrape.com/ 所有的价格和书名
"""
import requests
from bs4 import BeautifulSoup


head = {"User-Agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64)"}
response =requests.get("http://books.toscrape.com/",headers=head) # 返回Response格式的实例 , 可以额外传入一个headers的参数用来设置request库
if response.ok:
    soup = BeautifulSoup(response.text,"html.parser")   # html.parser指定解析器
    all_prices = soup.findAll("p",attrs={"class":"price_color"})  # 返回一个可以for循环的对象，包含所有CLASS=price_color的p标签
    all_titles = soup.findAll("h3")
    for prices in all_prices:
        print(prices.string[2:])
    for title in all_titles:
        all_links = title.findAll("a")
        for link in all_links:
            print(link)
            print(link.string)
else:
    print("请求失败")

"""
response =requests.get("http://books.toscrape.com/") 
if response.status_code >= 200 and response.status_code < 400:
    print("获取响应体内容")
if response.status_code >= 400 and response.status_code < 500:
    print("请求失败，客户端错误")
if response.status_code >= 500:
    print("请求失败，服务器错误")
"""


