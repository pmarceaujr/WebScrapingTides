
import re


def extract_date(date_string):
    match = re.search('\(\w+\W+\d+\W+\w+\)', date_string)
    if match:
        low_tide_date = match.group().replace('(', '').replace(')', '')
        low_tide_time = (date_string.replace(match.group(), ''))
    return low_tide_date, low_tide_time


def string_to_time(sun_rise, sun_set):
    sun_rise_txt, sun_rise_time = sun_rise.replace('AM', ' AM').split(': ', 1)
    sun_set_txt, sun_set_time = sun_set.replace('PM', ' PM').split(': ', 1)
    return sun_rise_txt, sun_rise_time, sun_set_txt, sun_set_time
