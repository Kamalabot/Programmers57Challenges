# Calculating Currency conversions

"""This program takes conversion data from the 
Open Exchange Rate web API for doing the conversion."""

import coinoxr
from my_functions import conv_numbers

coinoxr.app_id = "ba30b50fbaff41c99cdefbc1b2f4d82c"
# Latest Object is called from the Coinoxr extension
f = coinoxr.Latest()

conv_dict = f.get().body
# This dictionary contains the conversion of each country with respect to USD 
conv_count = conv_dict.get('rates')

assert conv_count['USD'] == 1


print(f"Here are the countries and their exchange rates {conv_count.keys()}")
# Get the from and to which currency, exchange is required
while True:
    print("Please Select the country in the list")
    cntry_to = input("Which country's currency you want to exchange from? ")
    cntry_from = input("Which country's currency you want to exchange to? ")
    if cntry_to in conv_count.keys() and cntry_from in conv_count.keys():
        break

# Get how much they want to convert
while True:
    curr = input("How much are you exchanging?")
    curr = conv_numbers(curr)
    if curr:
        break

ex_from = conv_count[cntry_from]
ex_to = conv_count[cntry_to]


amount = curr * ex_to / ex_from
amount = round(amount, 2)  # That was simple

print(f"Converted to {curr} {cntry_from} to {amount} {cntry_to}'s money" )
print("Thank you for using the service. Visit Again")