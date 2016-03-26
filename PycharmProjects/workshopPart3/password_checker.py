
#----jkanekunga-----------
#Password Checker Program with Loops

PASSWORD_MIN_LENGTH = 5
PASSOWRD_MAX_LENGTH = 15
SPECIAL_CHARACTER = "!@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|"

pwd_length_test = False
lCase_test = False
uCase_test = False
sp_char_test = False
digit_test = False
condition_not_met = True
str_heading = """
Please enter a valid password
Your password must be between 5 and 15 characters, and contain:
\t1 or more uppercase characters
\t1 or more lowercase characters
\t1 or more numbers
\tand 1 or more special characters: !@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|
"""
print(str_heading)
while condition_not_met:
    password = input('>')
    if len(password) >= PASSWORD_MIN_LENGTH and len(password) <= PASSOWRD_MAX_LENGTH:
        pwd_length_test = True

    for char in password:
        if char.isdigit():
            digit_test = True

    for letter in password:
        if letter.islower():
            lCase_test = True
        if letter.isupper():
            uCase_test = True

    for char in password:
        if char in SPECIAL_CHARACTER:
            sp_char_test = True

    if pwd_length_test and digit_test and lCase_test and uCase_test and sp_char_test:
        print("Your {} character password is {}".format(len(password), password), sep='')
        condition_not_met = False
    else:
        print('Invalid password!')
        condition_not_met = True
































