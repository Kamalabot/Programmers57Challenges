from stdiomask import getpass

# password validation in python

password = "we23newb"

pass_dict = {'user1': 'local1',
             'user2': 'local8'}

username = input('Enter your username : ')
yourpass = getpass("enter your password  here  :")

if yourpass == pass_dict[username]:
    print('Welcome')

else:
    print("I dont know you....")