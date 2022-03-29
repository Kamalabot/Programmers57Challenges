#Let's convert the temperature...

""" This program asks for the choice of temperature 
unit, and then converts the given numerical temperature
value into your choice of temperature unit 

I am learning DS from Scratch from Joel Grus, he teaches
a lot of Pythonic conventions. I will be using them 
and commenting them explicitly. Pythonic conventions 
help the reader understand exactly what is going on in
 the program, in clean way.
 
 This program will be implemented in the GUI TKinter 
 library as next improvement...
 """

def conv_numbers(num:str) ->int:
    try:
        return int(num)
    except:
        print("Enter numbers only for temperatures")

def conv_temp(num:int,from_scale:str, to_scale:str) -> int:
    """Returns the temperature from any scale to 
    any temperature scale..."""
    if from_scale == 'F' and to_scale == 'C':
        conv = (num - 32)* (5/9)
        return round(conv , 2)
    elif from_scale == 'K' and to_scale == 'C':
        conv =  (num - 273.15)
        return round(conv, 2)
    elif from_scale == 'C' and to_scale == 'F':
        conv =  (num * (9/5)) + 32
        return round(conv, 2)
    elif from_scale == 'K' and to_scale == 'F' :
        conv = (num - 273.15) * (9/5) + 32
        return round(conv, 2)
    elif from_scale == 'C' and to_scale == 'K':
        conv = (num + 273.15)
        return round(conv, 2)
    else: 
        conv = (num - 32)* (5/9) + 273.15
        return round(conv, 2)

print("""Provide the from_scale and to_scale to 
convert the temperatures to the required scale.""")

while True:
    to_scale = input('To which scale (C/F/K) you want to convert: ')
    to_scale = to_scale.upper()
    if to_scale in ['C','K','F']:
        break

while True:
    from_scale = input('From which scale (C/F/K)you want to convert: ')
    from_scale = from_scale.upper()
    if from_scale in ['C','K','F']:
        break

temp = input('Provide the temperature to convert in numbers? : ')
temp = conv_numbers(temp)
    
print(f"""Temperature of {temp} {from_scale} scale is converted to 
{conv_temp(temp,from_scale=from_scale,to_scale=to_scale)} {to_scale} scale""")

print("Thank you for using the service. Visit Again...")   