valid_input = False
while not valid_input:
     try:
        age = int(input("Age: "))
        valid_input = True
     except ValueError:  # or just  except:
        print("Invalid (not an integer)")
print("Next year you will be", age + 1)

