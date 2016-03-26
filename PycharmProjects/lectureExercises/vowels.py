import string

name = input("Name: ")

count_vowls = 0
for letter in  name.lower():
    if letter in "aeiou":
        count_vowls += 1

    print("Out of {} letters, {} has {} vowels".format(len(name), name, count_vowls))


