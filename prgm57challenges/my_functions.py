# This file contains only the helper functions

from random import randint
from typing import List
import sys


def conv_numbers(num: str) -> int:
    try:
        return int(num)

    except Exception as e:
        print("enter only numbers in this option", e)


assert conv_numbers('2') == 2


def bmiCalc(height: int, weight: int)->float:
    bmi = (weight / (height * height)) * 703
    return round(bmi, 1)


assert bmiCalc(height=72, weight=180) == 24.4


def karvonen(age: int, intens: float, restHR: int) -> int:
    temp = ((220 - age) - restHR) * intens + restHR
    return round(temp)


def give_rand(difficul: int) -> int:
    if difficul == 1:
        return randint(1, 10)
    elif difficul == 2:
        return randint(1, 100)
    else:
        return randint(1, 1000)


def get_domain(email_address: str) -> str:
    """Split on @ and return the last piece"""
    return email_address.lower().split('@')[-1]


assert get_domain('kalj879p@gmail.com') == 'gmail.com'
assert get_domain('macdeh@theay.com') == 'theay.com'


def get_data() -> List[List[int]]:
    # get the number of boxes that is going to be entered
    no_of_boxes = int(sys.stdin.readline().strip('\n'))
    # declare container to be returned
    box_data = []
    # enumerate over the num of boxes
    for _ in range(no_of_boxes):
        # get detail about each boxes, and split them
        box_temp = sys.stdin.readline().strip('\n').split(' ')
        # num_figs will be in beginning
        num_figs = int(box_temp[0]) # Find how many action figures
        # create variable for new container
        box_contains = []  # Open a new container
        # the input can contain lot of data seperated by spaces
        for x in box_temp[1:]:  # iterate over the remaning box temp data
            # append the info to the box_contains
            box_contains.append(int(x))  # append the heights to box_contains 
        # add the container to box data
        box_data.append(box_contains)  # append box contains list to box_data
 
    return box_data
