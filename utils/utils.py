
import re
import datetime


def extract_date(date_string):
    match = re.search('\(\w+\W+\d+\W+\w+\)', date_string)
    if match:
        low_tide_date = match.group().replace('(', '').replace(')', '')
        low_tide_time = (date_string.replace(match.group(), ''))
        #low_tide_time = time_converter(low_tide_time)
    return low_tide_date, low_tide_time


def string_to_time(sun_rise, sun_set):
    sun_rise_txt, sun_rise_time = sun_rise.replace('AM', ' AM').split(': ', 1)
    sun_set_txt, sun_set_time = sun_set.replace('PM', ' PM').split(': ', 1)
    #sun_rise_time = time_converter(sun_rise_time)
   # sun_set_time = time_converter(sun_set_time)
    return sun_rise_txt, sun_rise_time, sun_set_txt, sun_set_time


def time_converter(time_string):
    print(time_string + ";")
    print(time_string[-2:])
    time_string = time_string.replace(':', '')
    if time_string[-2:] == 'AM' and time_string[:2] == "12":
        print("here1")
        print(time_string[-4:2] + ':' + time_string[-6:])  # time_hour = '00'
    elif time_string[-2:] == 'AM' and len(time_string[-4:]) < 5:
        print("here2")
        print(time_string[-4:2] + ':' + time_string[-6:])
    elif time_string[-2:] == 'PM' and time_string[:-2] == "12":
        print("here3")
        print(time_string[-4:2] + ':' + time_string[-6:])
    elif time_string[-2:] == 'PM' and len(time_string[-4:]) < 5:
        print("here4")
        print(time_string[-4:2] + ':' + time_string[-6:])
    converted_time = time_string
    return converted_time


'''
                            sun_set_time = datetime.datetime.strptime(
                                sun_set_time.replace(" ", ""), '%I:%M%p').time()
'''
