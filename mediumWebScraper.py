from bs4 import BeautifulSoup
import requests


def getHTML(link):
    result = requests.get(url, timeout=5)
    return result


def findText(html):
    content = []
    document = BeautifulSoup(html.content, "html.parser")

    for docs in document.find_all("p"):
        content.append(docs.text)
    return content


if __name__ == "__main__":
    url = 'https://medium.com/@siliconvalley4u/how-to-develop-your-own-application-1d3ca7becbb9'
    html = getHTML(url)
    text = findText(html) 
    print(text)
