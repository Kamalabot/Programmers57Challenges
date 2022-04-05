#JSON format representation and data access

"""Takes the JSON data and converts into dict and the
uses it to search the product details and print out. 
Struggled quiet a bit with the JSON format, since single 
quoted data is not considered as JSON!!!!

Further there were some challenges in checking the names of the
products in the json. So debugging is done using the print statements. """

import json

#starting the exercise
js_pdt = """{
                "products" : [
                    {"name": "widget", "price": 25.00, "qty":5},
                    {"name": "Thing", "price": 15.00, "qty":5},
                    {"name": "Doodad", "price": 5.00, "qty":10}
                ]
            }
            """

#print(type(js_pdt))

#decoded product data
js_dec = json.loads(js_pdt)

#print(type(js_dec))

#print(js_dec["products"]) #will give me a list of dicts

products = [product["name"].lower() for product in js_dec["products"]]


while True:
    pdt = input("Enter a valid product name: ")
    #print(products)
    if pdt.lower() in products:
        #print('entering if')
        break 
    print("Product not found....")

#print(type(pdt_data))

#print(pdt_data)
#Retriving data from the json...
for product in js_dec["products"]:
    #check the product you want to search in lower case
    if product["name"].lower() == pdt.lower():
        print(f"Name : {product['name']}")
        print(f"Price : {product['price']}")
        print(f"Quantity : {product['qty']}")