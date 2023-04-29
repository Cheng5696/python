from socket import socket
from  json import loads
from base64 import b64decode

def main():

    client = socket()
    client.connect(("192.168.88.172", 6789))

    in_data = bytes()

    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)

    my_dict = loads(in_data.decode("utf-8"))     # 将传输过来的二进制转换成字符串(json是纯文本)
    filename = my_dict["filename"]
    filedata = my_dict["filedata"].encode("utf-8")   # 图片是而二进制，所以将json里的字符串转换成二进制
    with open("C:/Users/成城/Desktop/" + filename,"wb") as f:
        f.write(b64decode(filedata))
    print("照片已保存")

if __name__ == "__main__":
    main()
