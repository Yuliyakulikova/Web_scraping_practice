import requests
from fake_headers import Headers
from bs4 import BeautifulSoup

headers = Headers(browser='firfox', os='win')

html_data = requests.get('https://www.myip.com', headers=headers.generate()).text


soup = BeautifulSoup(html_data, 'lxml')

tag_span = soup.find('span', id='ip')
text_ip = tag_span.text

print(text_ip)