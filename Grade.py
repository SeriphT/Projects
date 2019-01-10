##gradeList= []
##def getGrade(gradeList):
##    maxGrade = 100
##    while True:
##        grade = input("Enter in a grade. To exit press space bar")
##        if grade == " ":
##            break
##        else:
##            x = float(grade)
##            if grade.isdigit() and x <= maxGrade:
##                grade = float(grade)
##                gradeList.append(grade)
##            elif x >= maxGrade:
##                q = input("Are you sure this"+grade+" is a good grade? y/n")
##                if q == "y":
##                    grade = float(grade)
##                    gradeList.append(grade)
##            else:
##                print("Invalid Grade, please enter an integer")
##
##getGrade(gradeList)
##print(gradeList)
##
##def avgFunction(gradeList):
##    sumgrade = 0
##    for grade in gradeList:
##        sumgrade  += grade
##    avg =  sumgrade/len(gradeList)
##    return avg
##
##def main(gradeList):
##    getGrade(gradeList)
##    avg = avgFunction(gradeList)
##    print("Your grade is ",avg)
##
##main(gradeList)
start = 5
stop =1000
stepvalue = 5

numbers = ""
for i in range(0,5):
    numbers += str(i)
print(numbers)
