# Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle). 
a=int(input("enter the first angle="))
b=int(input("enter the second angle="))
c=int(input("enter the third angle="))
if (a + b + c == 180 and a > 0 and b > 0 and c > 0):
    if (a == 90 or b == 90 or c == 90):
        print(" this is right angle triangle")
    elif a>90 or b>90 or c>90:
        print ("this is obtuse angle traingle")
    else:
        print("this is acute angle traingle")