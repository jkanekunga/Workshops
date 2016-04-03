
age = int(input("Enter person age:"))

if age >= 18:
    enrolment = input("Is he/she enrolled? (Y/N):")
    if enrolment == 'Y':
        print("You are eligible to vote")
    else:
        print("Please enrol to vote!")
else:
    print('You must be 18 years or over to vote!')

