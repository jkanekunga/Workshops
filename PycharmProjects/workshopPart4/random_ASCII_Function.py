
def main():

    get_number("10", "200")
    for i in range(10, 200,11): # make sure we have integers of different 'length'
        print("{} {:>5s}".format(i, chr(i)))

def get_number(lower, upper):
    number = input("Enter a number between ({} - {}):")

    if number < lower or number > upper or number.isdecimal():
        print("Invalid number!")
        number = input("Enter a number between ({} - {}):")
    return int(number)
main()

