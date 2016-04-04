""" Items for Hire  - By John Kanekunga
Due Date: 7/04/2016
GitHub: https://github.com/jkanekunga/Assignments.git


Pseudocode:

LOAD_FILE = open("items.csv","r")

function main()
    display welcome message
    display menu
    get choice
    choice to upper()
    while choice is not 'Q'
        if choice is 'L'
            call list_item()
            display menu
        else if choice is 'H'
            call hire_item()
        else if choice is 'R'
             call return_item()
        else if choice is 'A'
            call add_item()
        else
            diaplay error message
        display menu
        get choice
    print farewell message

function list_items()
    open file
    read file
    store in listview
    format and display

function hire_item()
    for every line in file
        if end of line != "*"
            store item available for hire
            display on item menu
            get item choice
            while choice != item number
                display correct error message
                get choice
            display hired confirmation
            marked as hired * on list
        else
            display error message

function return_item()
    for every line in file
        if end of line == "*"
            display on item menu
            get item choice
            while choice != item number
                display correct error message
                get choice
            display returned confirmation
            update item list
        else
            display error message

function add_item()
    get item choice
    for every line in file
        if item not in file
        get item name, description, price per day
        while item name != "" or description != "" price per day != "" or price per day in not numeric
            try
                get item name, description, price per day

            except error
            display error message
        add item
        display item
    else
        display error message
"""

print("Items for Hire - By John Kanekunga")

FILE_PATH = "c:\\items.csv"
read_file = open(FILE_PATH, "r")
rows = list(read_file)
totalrows = len(rows)
print("{} items loaded from items.csv".format(totalrows))
read_file.close()

print("Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd an item\n(Q)uit")

def main():

    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            list_item()
            break
        elif choice == "H":
            hire_item()
            break
        elif choice == "R":
            return_item()
            break
        elif choice == "A":
            add_item()
            break
        else:
            print("Invalid input!")
            print("Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd an item\n(Q)uit")
            choice = input(">>>").upper()

    print("Good Bye!")

def list_item():

    input_file = open(FILE_PATH, "r")
    r = input_file.read()
    print(r)
    input_file.close()#..

def hire_item():
    print("Item hired!")

def return_item():
    print("Item returned!")

def add_item():
    print("Item added")

main()


