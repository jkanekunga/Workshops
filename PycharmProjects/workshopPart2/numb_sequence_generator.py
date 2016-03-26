x = int(input("Enter first integer:"))
y = int(input("Enter ending integer:"))

if x < y:

    print("Choose:\n(1)Show EVEN numbers from", x, "to", y, " \
    \n(2)Show ODD numbers from", x, "to", y, "\n(3)Show the SQUARES from", x, "to", y)

    choice = input('')

    while choice == '1' or choice == '2' or choice == '3':
        if choice == '1':
            if x % 2 == 0:
                for i in range(x, y, 2):
                    print(i, end=' ')
                print()
            else:
                for i in range(x-1, y, 2):
                    print(i, end=' ')
                print()

        elif choice == '2':
            if x % 2 != 0:
                for i in range(x, y, 2):
                    print(i, end=' ')
                print()
            else:
                for i in range(x+1, y, 2):
                    print(i, end=' ')
                print()

        elif choice == '3':
            for i in range(x, y, 1):
                print(i**2, end=' ')
            print()

        choice = input('')
    print('Wrong choice!')

else:
    print('Starting number must be less than end number!')
