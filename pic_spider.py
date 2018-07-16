import requests
from bs4 import BeautifulSoup

index = 0
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) '
                         'Gecko/20100101 Firefox/47.0'}


def save_pics(res_url):
    global index
    html = BeautifulSoup(requests.get(res_url, headers=headers).text, "lxml")
    for aText in html.find_all('a', {'class': 'alink'}):
        imgUrl = aText.get("href")
        imgUrlHtml = BeautifulSoup(requests.get(imgUrl, headers=headers).text, "lxml")
        realUrl = imgUrlHtml.find("img").get("src")
        print(realUrl)
        with open("images/" + str(index) + ".jpg", "wb") as jpg:
            jpg.write(requests.get(realUrl).content)
        index += 1


if __name__ == '__main__':
    url = "http://588ku.com/moban/0-pxnum-1-11-0-0-0-0-1/"
    for i in range(0, 5):
        save_pics(url)
        url = BeautifulSoup(requests.get(url, headers=headers).text, "lxml").find("a", {"class": "downPage"}).get(
            "href")
