import requests

def main():
    res = requests.get("https://apis.tianapi.com/toutiaohot/index?key=9ac86da7904dcf88b189952dba834809")
    datas = res.json()
    for data in datas["result"]["list"]:
        print(data["word"])
if __name__ == "__main__":
    main()