#This file contains only the helper functions

from random import randint

def conv_numbers(num:str) ->int:
    try:
        return int(num)
    except:
        print("enter only numbers in this option")

assert conv_numbers('2') == 2

def bmiCalc(height:int,weight:int)->float:
    bmi = (weight / (height * height)) * 703
    return round(bmi,1)

assert bmiCalc(height=72,weight=180) == 24.4

def karvonen(age: int, intens: float, restHR: int) -> int:
    temp = ((220 - age) - restHR) * intens + restHR
    return round(temp)

def give_rand(difficul: int)->int:
    if difficul == 1:
        return randint(1, 10)
    elif difficul == 2:
        return randint(1, 100)
    else:
        return randint(1, 1000)