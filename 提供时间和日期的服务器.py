"""
2023/04/29   python 3.11
使用tcp套接字实现
"""
from  socket import socket,SOCK_STREAM,AF_INET
from datetime import datetime
def main():
    server = socket(family=AF_INET,type=SOCK_STREAM)
    server.bind(("192.168.88.172",6789))
    server.listen(512)
    print("服务器启动开始监听")
    while True:
        client ,addr = server.accept()
        print(f"{str(addr)}连接到了服务器")
        client.send(str(datetime.now()).encode("utf-8"))
        client.close()

if __name__ == "__main__":
    main()
