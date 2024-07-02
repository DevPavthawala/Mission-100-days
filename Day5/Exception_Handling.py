
a = 4
b = 0



try:
    print("resorse open")
    print(a/b)

except ZeroDivisionError:
    print("zero division error")

try:
    x = int(input("Enter a no. :"))
    print(x)


except ValueError:
    print("Value error")


# Exception is use for all the exception available
 # e for getting the resorn of error
except Exception as e:
    print("Somthing goes wrong......",e)


finally:
    print("Resorse close")


print("Bye")


