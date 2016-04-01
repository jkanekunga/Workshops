
lower = 10
upper = 100

#print("Enter a number (" + str(lower) + "-­‐" + str(upper) + "):")
min_number = int(input("Enter starting number ({} - {}):".format(lower, upper).strip()))
max_number = int(input("Enter ending number ({} - {}):".format(lower, upper).strip()))
step_numb = int(input("Enter number to step ({} - {}):".format(lower, upper).strip()))


for i in range(min_number, max_number,step_numb): # make sure we have integers of different 'length'
    print("{} {:>5s}".format(i, chr(i)))

#def get_number(lower, upper):
