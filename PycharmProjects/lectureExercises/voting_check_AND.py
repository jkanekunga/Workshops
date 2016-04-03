
age = int(input("Enter person age:"))
enrolment = input("Is he/she enrolled? (Y/N):")
if age >= 18 and enrolment == 'Y':
    print('You are eligible to vote!')
elif age >= 18 and enrolment == 'N':
    print('Please enroll to vote!')
else:
    print("You are not eligible!")
