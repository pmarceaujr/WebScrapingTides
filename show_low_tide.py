import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

beach = 'Half-Moon-Bay-California'
tide_url = "https://www.tide-forecast.com/locations/" + beach + "/tides/latest"
print(tide_url)
#page = urlopen(tide_url)
web_page = requests.get(tide_url)

# print(web_page.content)
# print(web_page.status_code)
# print(web_page)
soup = BeautifulSoup(web_page.content, 'html.parser')
# print(soup.prettify())

tide_table = soup.find('div', class_='tide_flex_start')
print(tide_table.prettify())
print("===========================================")
