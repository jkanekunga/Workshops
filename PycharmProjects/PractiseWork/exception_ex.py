

try:

    length = int(input("Enter Length:"))
    width = int(input("Enter width:"))

    area = length * width
except ValueError:
    print("Invalid entry!")
