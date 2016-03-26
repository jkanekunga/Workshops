finished = False
result = 0
while not finished:
    try:
        nit_val = input("Enter and integer:")
        result = int(nit_val)
    except ValueError:
        print("Please enter a valid integer.")
    print("valid result is", result)
#finished = True