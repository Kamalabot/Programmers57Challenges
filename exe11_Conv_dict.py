#Calculating Currency conversions

"""This program takes the input of the countries, 
their currencies, and converts it based on the 
conversion rates fixed in the dictionary"""

from math import ceil

#Function to check number
def conv_number(curr):
    """The function checks whether the provided currency is
        in integer format
    """
    try:
        return int(curr)
    except ValueError:
        print('Enter currency value only, no strings')
assert conv_number('5') == 5

#create the dictionary of country and conversion rates
conv_dict = {}
country = ['USA','EUR','GER','RUS','IND','ENG']
conversion = [1.37, 0.01, 0.89, 0.57, 0.75, 1.20]

for index, cnt in enumerate(country):
    conv_dict[country[index]] = conversion[index]

print(f"Here are the countries and their exchange rates {conv_dict}")
#Get the from and to which currency, exchange is required
while True:
    print("Please Select the country in the list")
    cntry_to = input("Which country's currency you want to exchange from? ")
    cntry_from = input("Which country's currency you want to exchange to? ")
    if cntry_to in country and cntry_from in country:
        break 


#Get how much they want to convert
while True:
    curr = input("How much are you exchanging?")
    curr = conv_number(curr)
    if curr:
         break

ex_from = conv_dict[cntry_from]
ex_to = conv_dict[cntry_to]


amount = curr * ex_to / ex_from
amount = round(amount,2) #That was simple

print(f"Converted to {curr} {cntry_from} to {amount} {cntry_to}'s money" )
print("Thank you for using the service. Visit Again")