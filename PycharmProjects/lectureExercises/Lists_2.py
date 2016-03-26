

subjects = []

subject = input("Subjects:")

while subject != '':
    subjects.append(subject)
    subject = input("Subjects:")

    print("You are doing ", end='')

    print(", ".join(subjects))

    #for subject in subjects[:-1]:
        #print(subject, ",", sep='', end='')


