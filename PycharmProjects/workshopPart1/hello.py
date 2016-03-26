__author__ = 'John'
print('hello world')

def main():

    area = calculate_area()
    print("The are is ", area)

def calculate_area():
    l = int(input("Enter lenght:"))
    w = int(input("Enter width:"))

    return l*w

main()
