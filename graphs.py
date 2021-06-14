from matplotlib import pyplot
import numpy

database = []
male = 0
female = 0
other = 0

age= []    

txtFile = open("database.txt", "r")

for eachLine in txtFile:
    eachLine = eachLine.strip("\n")
    eachLine = eachLine.split(",")

    database.append(eachLine)

def pieChart():
    male = 0
    female = 0
    other = 0
    
    for i in range(len(database)):
        if database[i][3] == "Male":
            male += 1
        elif database[i][3] == "Female":
            female += 1
        elif database[i][3] == "Other":
            other += 1

    
    lables = "Male", "Female", "Other"
    data = [male, female, other]
    pyplot.pie(data, labels=lables, autopct='%1.1f%%')
    pyplot.show()

##def LineGraph():
##    for index in range(len(database)):
##        age.append(database[index][0])
##    age.sort()
##    print(age)
##
##    ageBands = ["0-10", "11-20", "21-30", "32-40", "41-50", "51-60", "70+" ]
##
##    for data in age:
##        if data > 0 and data <= 10:
##            ageBands[0].append(data)
##        elif data > 10 and data <= 20:
##            ageBands[1].append(data)
##        elif data > 20 and data <= 30:
##            ageBands[2].append(data)
##        elif data > 30 and data <= 40:
##            ageBands[3].append(data)
##        elif data > 40 and data <= 50:
##            ageBands[4].append(data)
##        elif data > 50 and data <= 60:
##            ageBands[5].append(data)
##        else:
##            ageBands[6].append(data)
##
##        
##LineGraph()



