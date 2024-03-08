#Important calculation that will save you money
import math
from my_functions import conv_numbers


def get_months(apr: float, b: float, p: float) -> int:
    apr = apr / (100 * 365)
    #print(f"apr is {apr}")
    apr_e = (1 + apr) ** 30
    #print(f"apr_e is {apr_e}")
    B = (b / p)
    #print(f"B is {B}")
    #Learnt the base of 10 has to be provided for log
    temp = math.log((1 + B * (1 - apr_e)),10) / math.log(1 + apr, 10)
    return math.ceil((-1 / 30) * temp)

print(get_months(12, 5000,  100)) 

while True:
    print("Enter appropriate float values")
    b = conv_numbers(input("What is your Balance : "))
    apr = conv_numbers(input("What is APR on the Card : "))
    p = conv_numbers(input("What is your monthly payment : "))

    if b and apr and p:
        break
    
print(f"It will take {get_months(apr, b, p)} months to pay off this card")