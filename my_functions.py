#This file contains only the helper functions

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
