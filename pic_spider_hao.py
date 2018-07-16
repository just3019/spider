import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) '
                         'Gecko/20100101 Firefox/47.0'}
# 二维数组
avList = []
# 行号
i = 0
# 列号
j = 0
# resourceId
resourceId = 70


def save_hao_pic(res_url):
    html = BeautifulSoup(requests.get(res_url, headers=headers).text, "lxml")
    for i in html.find_all("img"):
        print(i.get("src"))


def save_hao_urlAndName(res_url):
    r = requests.get(res_url, headers=headers)
    r.encoding = 'utf-8'
    html = BeautifulSoup(r.text, "lxml")
    for i in html.find_all("li"):
        detailName = i.find("a").text
        detailUrl = "http://se.haoa14.com/" + i.find("a").get("href")
        print(detailName)


if __name__ == '__main__':
    save_hao_urlAndName("http://se.haoa14.com/listhtml/2.html")
    # save_hao_pic("http://se.haoa14.com//html/133547.html")

