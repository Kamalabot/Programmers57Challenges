#Checking password strength

"""
The program takes the password and informs whether 
it is strong or weak. Complex the password, more difficult
it will be to crack. 

There are 4 types of password, functions are implemented to 
analyse the pass string and return the type of the password 

Flask or TKinter GUI application will be written.

"""

def chk_len(passwd: str) ->bool:
    """Checks whether the password is having more than 
    8 characters or not"""
    if len(passwd) >= 8:
        return True
    else:
        return False

assert chk_len('travl') is False
assert chk_len('travl5658') is True

def has_what(passwd: str) ->str:
    """Checks the password and returns what it contains, 
    number, alphabets or Spl characters"""
    if passwd.isnumeric():
        return 'Only Numbers'
    
    if passwd.isalpha():
        return 'Only Alphabets'

    if passwd.isascii():
        return 'Has mixed Special'

assert has_what('12345') == 'Only Numbers'
assert has_what('abcde') == 'Only Alphabets'
assert has_what('168dth*(&%') == 'Has mixed Special'

pa = input("Please enter your password to check...: ")

if chk_len(pa): 
    if has_what(pa) == 'Only Numbers':
        print(f"The password {pa} is a weak password")

    if has_what(pa) == 'Only Alphabets':
        print(f"The password {pa} is a strong  password")

    if has_what(pa) == 'Has mixed Special':
        print(f"The password {pa} is a very strong password")
else:
    print(f"Print {pa} length is less than 8 characters, so very weak")


def passwordValidator(passwd: str) -> int:
    """Takes in the string and returns values 1 to 4, where
    1 being the very strong and 4 being the very weak"""
    if chk_len(passwd): 
    
        if has_what(passwd) == 'Only Numbers':
            return 3

        if has_what(passwd) == 'Only Alphabets':
            return 2

        if has_what(passwd) == 'Has mixed Special':
            return 1
    
    else:
        return 4
    

assert passwordValidator('122345') == 4
assert passwordValidator('aycesinach') == 2
assert passwordValidator('15790862365') == 3
assert passwordValidator('678&8%osed') == 1