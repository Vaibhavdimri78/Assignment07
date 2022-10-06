"""print("enter the month number")
m=int(input())
if m in (1,3,5,7,8,10,12):
     print("month days are 31")
elif m in (4,6,9,11):
    print("month days are 30")
else:
    print("month days are 28 ")
"""
#1 
"""match m:
    case m if m in (1,3,5,7,8,10,12):
        print("month %d has 31 days"%m)
    case m if m in (4,6,9,11):
        print("month %d has 30 days"%m)
    case 2:
        print("the month has 28 days or 29 days in leap year")"""
#2
"""
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
print("enter what operation you want to perform")
choice=int(input())
print("enter two operands")
a,b=int(input()),int(input())
match choice:
    case 1:
        print("sum of %d and %d is "%(a,b),a+b)
    case 2:
        print("the subtraction of %d and %d is "%(a,b),a-b)
    case 3:
        print("the multiplication of %d and %d is "%(a,b),a*b)
    case 4:
        print("the division of %d and %d is "%(a,b),a/b)
print("Done") 
"""
#3
"""
print("enter your choice for triangle check operation")
print("1 for to check for isoless triangle")
print("2 for to check for right angle triangle")
print("3 for to check for eqilateral triangle")
choice=int(input())
print("enter three sides of triangle")
a,b,c =int(input()),int(input()),int(input())

if(a==b==c):
    print("the triangle is equilateral")
elif(a==b!=c or a==c!=b or c==b!=a):
    print("the triangle is isosceles")                              #using if else checking the triangle 
elif(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2):
    print("this is right angle triangle")
else:
    print("this is scalene triangle")

match choice:
    case 3 if(a==b==c):
        print("the triangle is equilateral")
    case 2 if(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2):
        print("triangle is right angle triangle")
    case 1 if(a==b!=c or a==c!=b or c==b!=a):
        print("the triangle is isoless")

#4

print("enter your age")
age = int(input())
match age:
    case age if age in range(0,11,1):
        print("you are kid")
    case age if age in range(10,21,1):
        print("teen")
    case age if age in range(21,41):
        print("young")
    case age if age in range(41,60):
        print("experienced")
    case age if age in range(61,200000):
        print("elder")
        """

#5
print("enter a number\n")
n=int(input())
if(n>0):
    if(n%2==0):
        print("saurabh Sir")
    else:
        print("Adtiya Choudhary")
else:
    if(n%2!=0):
        print("Parteek Jain")
    