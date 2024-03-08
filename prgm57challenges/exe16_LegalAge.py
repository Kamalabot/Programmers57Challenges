#Legal Driving Age

def conv_num(num):
    try:
        return int(num)
    except:
        print("The age has to be number")

age = conv_num(input("Please enter age ? :"))

if age > 15:
    print("You are old enough to drive")
else:
    print("You are not old enough, don't drive.")