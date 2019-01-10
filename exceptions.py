##while True:
##    try:
##        num = float(input("Enter a number:"))
##        break
##    except ValueError:
##        print("Something went wrong")
##    except TypeError:
##        print("lol no...")
##print(num)

##for value in (None, "hi"):
##    try:
##        print("attempting to convert", value, "--->",end=" ")
##        print(float(value))
##    except ValueError:
##        print("Something went wrong")
##    except TypeError:
##        print("lol no...")

##try:
##    num = float(input("Enter a number:"))
##except ValueError as e:
##    print("That's not a number! Or as python gives...")
##    print(e)


try:
    num = float(input("Enter a number:"))
except ValueError as e:
    print("That's not a number! Or as python gives...")
    print(e)
else:
    print ("your number was:",num)
