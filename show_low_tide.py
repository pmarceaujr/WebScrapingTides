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
for table in tide_table.find_all('table'):
    # print(table)
    for trows in table:
        columns = trows.find_all('td')
       # print(columns)
        if (columns != [] and columns[0].text.strip() == 'Low Tide'):
            what_tide = columns[0].text.strip()
            print(columns[0].text.strip(),
                  columns[1].text.strip(), columns[2].text.strip())
