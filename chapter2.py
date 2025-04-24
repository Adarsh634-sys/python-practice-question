#slice :- acessing part of  string called slicing

str= "sandilyaad"
print (str[5:len(str)])

str= "i am studying python from apna college" 

print(str.endswith("ege"))

# capitalize 1st characters of string
str="i am a student"
print(str.capitalize()) # first leter will be cpital

str= str.capitalize()
print (str)

# replace string old and new also said (replace function)

str= "iam a good boy"
print( str.replace("good","bad"))

# find function in sting

str="i am a good boy"

print(str.find("g"))

# wap to input user's name & print its length
name = input("name:")
print(len(name))

#wap to find the occurence  of '$' in a string.

str=" hii i am$ the $ symbol of us cuurency $"
print(str.count ("$"))

#conditional statements
age =int(input("enter your age:"))
if (age<=18):
    print(" you are eligible of voting")
elif (age>=20):
        print("you are mature your age")
else:
    print("not adult")

light = input("light:")
if(light=="red"):
     print("stop")
elif (light=="yellow"):
     print("wait")
elif (light=="green"):
     print("go")
else:
    print("invalid light")

age = 15

if(age>=18):
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")


marks= int(input("enter your marks:"))
if(marks>=90):
    print("gradeA")
elif(marks>=80):
    print("grade B")
elif(marks>=70):
    print("grade C")

# wap to check if the number enterd by the user is odd or even

num= int (input("enter the nuber:"))
if (num%2==0):
    print("even")
else:
    print("odd")

#wap to find the greatest of 3 numbers enter the user 

a = int(input("enter the 1st number:"))
b = int(input("enter the 2nd number :"))
c = int (input("enter the 3rd number:"))
if(a>=b and a >= c):
    print("first number is greater", a)
    if(b>c):
        print("second number is greater", b)
    else:
        print("third number is greater",c)

# wap to multiple of 7

x= int (input("enter the number"))
if(x%7==0):
    print("multiple of 7")
else:
    print("not a multiple of 7")





 
