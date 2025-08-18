# Read three integers and print their maximum.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if(a>b>c):
    print("first number is maximum number")
elif(b>a>c):
    print("second number is the maximum number")
else:
    print("third number is the mmaximum number")