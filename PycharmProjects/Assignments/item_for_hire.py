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
            display instructions
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

INPUT_FILE = open("c:\\items.csv", "r")
rows = list(INPUT_FILE)
totalrows = len(rows)
print("{} items loaded from items.csv".format(totalrows))
INPUT_FILE.close()

print("Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd an item\n(Q)uit")
choice = input(">>>").upper()

