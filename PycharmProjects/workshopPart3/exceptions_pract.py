numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

while denominator == 0:
    print("No 0 denominator!")
    denominator = int(input("Enter the denominator: "))
try:
    fraction = numerator / denominator
except ValueError:
        print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
