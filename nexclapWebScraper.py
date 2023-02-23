from bs4 import BeautifulSoup
import requests

def getBlogInfo(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    description = soup.find('div', attrs={'class':'text-rich-text w-richtext'})
    
    return description.text

if __name__ == "__main__":
    url = 'https://www.siliconvalley4u.com/blogs/applied-education-how-technology-can-help'
    description = getBlogInfo(url)
    print(description)