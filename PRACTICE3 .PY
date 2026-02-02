# Write a program to add two numbers entered by the user.
"""num1=int (input("enter the first number"))
num2 = int(input("enter the second number"))
sum= num1+num2
print (sum)"""

# Write a program to find the square and cube of a number
"""n = int (input ("enter the number" ))
square = n*n
cube= n*n*n
print(square, cube)"""

# Write a program to check whether a number is even or odd.
num = int (input("enter a number:"))
if num % 2 == 0:
    print("this is even number")
else:
    print("this is odd number")

#Write a program to find the largest of three numbers.

num1= int (input("enter the first number"))
num2 = int (input ("inter the second number"))
num3 = int (input ("enter the third number"))

if num1>num2 and num1>num3:
    print("num1 is greater ")
elif num2>num1 and num2> num3:
    print ("num2 is greater ")
else:
    print ("num3 greater")

#Write a program to calculate simple interest.
principle= int(input("enter the principle:"))
time = int (input("inter the time:"))
Rate = int (input( "inter the rate"))

si= (principle*time*Rate)/100

print (si)