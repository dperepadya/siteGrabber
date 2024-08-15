import requests
from bs4 import BeautifulSoup

URL = "https://scipost.org/atom/publications/comp-ai"

if __name__ == '__main__':
    source = requests.get(URL)
    # print(source.text)
    soup = BeautifulSoup(source.text, 'xml')
    entries = soup.find_all('entry')
    print('Publications')
    for item in entries:
        title = item.find('title').text
        link = item.find('link')['href']
        updated = item.find('updated').text
        summary = item.find('summary').text
        print(f"Title: {title}\rLink: {link} Updated: {updated} Summary: {summary}")
