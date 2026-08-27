try:
    number = 10 / 0
except:
    print("Someting went wrong")


try:
    number = int(input("Ener number"))
    result = 100 / number
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("number can not be zero")
else:
    print("number input successful")
finally:
    print("Finished")
