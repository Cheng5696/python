"""
2023/04/29  python 3.11
研究一下open打开图片的数据类型是二进制文件，b64转码后的数据类型还是二进制文件，在解码成字符串
decode('utf-8')  将二进制解码成字符串
encode("utf-8")  将字符串编码成二进制
"""

from base64 import b64encode,b64decode

def main():
    with open("images/ball.png","rb") as f :      # f.read -> 二进制
        a = b64encode(f.read()).decode("utf-8")    # b64encode(f.read()) -> b64二进制     b64encode(f.read()).decode("utf-8")  -> 字符串
        s = b64decode(a.encode("utf-8"))            # a.encode("utf-8")  -> b64二进制      b64decode(a.encode("utf-8"))  -> 二进制
        with open("C:/Users/成城/Desktop/1.png","wb") as w :
            w.write(s)
if __name__ == "__main__":
    main()
