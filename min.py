# sir code of minimum number
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if (a<b and a<c):
  print("a is min")
elif (b<c):
  print("b is min")
else:
  print("c is min")