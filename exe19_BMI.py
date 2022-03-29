#Lets calculate the BMI of the person

"""Will incorporate GUI with sliders for the Height
and weight as an improvement and learning"""

def conv_numbers(num:str) ->int:
    try:
        return int(num)
    except:
        print("enter only numbers in this option")

def bmiCalc(height:int,weight:int)->float:
    bmi = (weight / (height * height)) * 703
    return round(bmi,1)

assert bmiCalc(height=72,weight=180) == 24.4

print("Provide your height and weight")
while True:
    height = conv_numbers(input('Provide height in inches : '))
    weight = conv_numbers(input('Provide weight in pounds : '))
    if height and weight:
        break

your_bmi = bmiCalc(height=height, weight=weight)

if your_bmi < 18.5:
    print(f"Your BMI is {your_bmi}")
    print('You are under weight, eat more')

elif your_bmi >= 18.5 and your_bmi <= 25:
    print(f"Your BMI is {your_bmi}")
    print('You are having optimal BMI, go have a donut')

else:
    print(f"Your BMI is {your_bmi}")
    print('You are over weight, how much do you eat???')


