import pytz
from datetime import datetime

import django
import os
from django.conf import settings

import config
import aes

from django.contrib.auth.hashers import make_password

timezone = pytz.timezone('Europe/Moscow')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MilkFarm.config.settings")
django.setup()

from users.models import User


def prepare_user_info(profile):
    user = User(
        name=profile[0],
        address=profile[1],
        email=profile[2],
        last_login=profile[4],
        date_joined=profile[4],
        date_of_birth=profile[5],
        about=profile[6],
        phone_number=profile[7],
        company=profile[8],
        amount=profile[10]
    )
    user.card_number = aes.make_str_from_dict(aes.encrypt(profile[9], config.PASSWORD))
    user.password = make_password(profile[3], hasher='sha1')
    return user


def get_sorted_data():
    data1 = read_first_file()
    data2 = read_second_file()
    data3 = read_third_file()

    result = []

    for i in range(len(data1)):
        result.append(data1[i] + data2[i][2:] + data3[i][2:])

    return result


def make_correct_date(line):
    """ Переводит сырую дату в коректную форму"""
    line = line.split(' ')
    line = line[1:4]

    if line[0] == 'Jan':
        line[0] = '1'
    elif line[0] == 'Feb':
        line[0] = '2'
    elif line[0] == 'Mar':
        line[0] = '3'
    elif line[0] == 'Apr':
        line[0] = '4'
    elif line[0] == 'May':
        line[0] = '5'
    elif line[0] == 'Jun':
        line[0] = '6'
    elif line[0] == 'Jul':
        line[0] = '7'
    elif line[0] == 'Aug':
        line[0] = '8'
    elif line[0] == 'Sep':
        line[0] = '9'
    elif line[0] == 'Oct':
        line[0] = '10'
    elif line[0] == 'Nov':
        line[0] = '11'
    elif line[0] == 'Dec':
        line[0] = '12'

    line = [int(i) for i in line]

    date = datetime(line[2], line[0], line[1], 0, 0, 0)
    date = timezone.localize(date)
    return date


def read_first_file():
    file1 = open('tables/table1', 'r')
    data1 = []
    for line in file1:
        data_line = line.split(',')
        try:
            data_line[3] = data_line[3]
            data_line[4] = make_correct_date(data_line[4])
            data1.append(data_line)
        except IndexError:
            pass
    return sorted(data1)


def read_second_file():
    file2 = open('tables/table2', 'r')
    data2 = []
    for line in file2:
        data_line = line.split(',')
        try:
            data_line[2] = make_correct_date(data_line[2])
            data_line[5] = data_line[5].strip()
            if len(data_line) == 7:
                data_line.pop()
            data2.append(data_line)
        except Exception:
            pass
    return sorted(data2)


def read_third_file():
    file3 = open('tables/table3', 'r')
    data3 = []
    for line in file3:
        data_line = line.split(',')
        if len(data_line) == 4:
            data_line[3] = float(data_line[3].strip())
            data3.append(data_line)
    return sorted(data3)
