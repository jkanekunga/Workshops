# Combining loops

name = input('Enter name:')
print("(H)ello\n(G)oodbye\n(Q)uit")
print('')
choice = input('')

while choice != "Q":
    if choice == "H":
        print('hello', name)
    elif choice == "G":
        print('goodbye', name)
    else:
        print('invalid choice')

    print("(H)ello\n(G)oodbye\n(Q)uit")
    print('')
    choice = input('')

print('Finished')

