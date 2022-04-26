import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from utils import utils

first_low_tide, first_tide_height, second_low_tide, second_tide_height = None, None, None, None
first_tide = 0

beach = 'Half-Moon-Bay-California'
tide_url = "https://www.tide-forecast.com/locations/" + beach + "/tides/latest"
print(tide_url)
#page = urlopen(tide_url)
web_page = requests.get(tide_url)

soup = BeautifulSoup(web_page.content, 'html.parser')
# print(soup.prettify())

tide_table = soup.find('div', class_='tide_flex_start')
# print(tide_table.prettify())
print("===========================================")
for table in tide_table.find_all('table'):
    # print(table)
    for trows in table:
        columns = trows.find_all('td')
       # print(columns)
        if (columns != [] and columns[0].text.strip() == 'Low Tide'):
            what_tide = columns[0].text.strip()
            if first_tide == 0:
                low_tide_date, first_low_tide = utils.extract_date(
                    columns[1].text.strip())
                first_tide_height = columns[2].text.strip()
                first_tide += 1
            else:
                low_tide_date, second_low_tide = utils.extract_date(
                    columns[1].text.strip())
                second_tide_height = columns[2].text.strip()
        elif (columns != [] and columns[0].text.strip() != 'High Tide'):
            sun_rise_txt, sun_rise_time, sun_set_txt, sun_set_time = utils.string_to_time(
                columns[0].text.strip(), columns[1].text.strip())
            if sun_rise_time < first_low_tide < sun_set_time:
                print(sun_rise_txt, sun_rise_time, sun_set_txt, sun_set_time, what_tide, low_tide_date, first_low_tide,
                      first_tide_height)
            elif sun_rise_time < second_low_tide < sun_set_time:
                print(sun_rise_txt, sun_rise_time, sun_set_txt, sun_set_time,
                      what_tide, low_tide_date, second_low_tide, second_tide_height)
            first_low_tide, first_tide_height, second_low_tide, second_tide_height = '', '', '', ''
            first_tide = 0
