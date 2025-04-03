import re

from bs4 import BeautifulSoup
import requests


class novel ():
   def __init__(self,url,root,reText):
      self.url = url
      self.root = root
      self.mulu = []
      self.reText = reText
      self.title = ""
      self.content = []

   """解析出主域名"""
   def getbase_url(self):
      pattern = r"^(https?://[^/]+)"
      match = re.match(pattern, self.url)

      if match:
         base_url = match.group(1)
         print("匹配到的基 URL:", base_url)
         return base_url
      else:
         print("未匹配到基 URL")

   """获取正文"""
   def getContent(self,list):
      """获取requests，soup对象"""
      headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
      }
      response = requests.get(list[1],headers=headers)
      html = response.content
      soup = BeautifulSoup(html, "lxml")
      #print(soup.prettify()) # 测试
      content = soup.find("div",id="chaptercontent")
      self.content.append(list[0] + "\n")
      self.content.append(content.get_text(separator="\n"))
      #print(self.content)
      print(f"py读取了{list[0]}")


   def start(self):
      """获取requests，soup对象"""
      headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
      }
      response = requests.get(self.url,headers=headers)
      html = response.content
      soup = BeautifulSoup(html, "lxml")
      #print(soup.prettify()) # 测试

      """获取包含章节目录的列表"""
      pattern = re.compile(self.reText)
      lists = soup.find_all("a", text=pattern)
      print(lists)

      """将章节名和url封装到列表"""
      base_url = self.getbase_url()
      for l in lists:
         self.mulu.append([l.text,base_url+l["href"]])  # 小列表放到大列表
      # print(self.mulu)

      """获取标题"""
      self.title = soup.find("h1").text

      """获取全本小说"""
      for i in self.mulu:
         self.getContent(i)
      # print(self.content)

      """写入文件"""
      print("正在写入文件")
      with open(self.root +"\\"+self.title + ".txt", "a", encoding="UTF-8") as f:
         f.write(self.title + "\n")
         for i in self.content:
            print("写入完成")
            f.write(i)

if __name__ == "__main__":
   n = novel("https://www.biqu05.cc/html/224844/",
             r"C:\Users\成城\Desktop\练习项目\笔趣阁小说下载",
             r"第.{0,6}章.{0,20}")
   # n.getContent(["ss","https://www.biqu03.cc/read/44149/1.html"])
   n.start()




