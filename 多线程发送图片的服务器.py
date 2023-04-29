"""
2023/04/29  python 3.11
这是一个使用多线程，向客户端发送照片的服务器
"""
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():
    class FileTransferHandler(Thread):
        # def __int__(self, cclient):    # 打错了一个词
        #     super().__init__()
        #     self.cclient = cclient

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict["filename"] = "ball.png"
            my_dict["filedata"] = data          # data 作用范围在main函数内
            json_str = dumps(my_dict)
            self.cclient.send(json_str.encode("utf-8"))
            self.cclient.close()

    serve = socket()
    serve.bind(("192.168.88.172", 6789))
    serve.listen(512)
    print("服务器启动，开始监听")
    with open("images/ball.png","rb") as f:
        data = b64encode(f.read()).decode("utf-8")
    while True:
        client, addr = serve.accept()
        FileTransferHandler(client).start()

if __name__ == "__main__":
    main()