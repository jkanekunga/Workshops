
#name = input("Enter your name:")

#open_file = open("name.txt", "w")
#print(file_name, file= open_file)

#---result
#outFile = open("name.txt", "w")
#name = input("What is your name? ")
#print(name, file="outFile") # or outFile.write(name)
#outFile.close()


#------next program

#open_file = open("name.txt", "r")

#for each_line in open_file:
    #print(each_line, end='')

#open_file.close()

#-------next program

open_file = open("numbers.txt", "r")

result = 0
for each_line in open_file:
    result += int(each_line)

    print(result)


