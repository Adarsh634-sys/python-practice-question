marks =int (input("marks:"))
if(marks >= 90):
    print("A")
elif(marks >= 80 ):
        print("B")
elif(marks >= 70  ):
    print("c")
else:
     print("D")

# conditional statement in single line 
food = input("food:")
eat = "yes" if food== "veg" else "no"
print (eat)

# ternary operator in conditional statement 

food = input("food : ")
print("sweet") if food == "cake" or food =="jalebi"  else print("not sweet")

# clever if / ternary operator

age = int(input("age:"))
vote= ("yes you are eligible for voting","no you are not eligible for voting")[age<18] 
print(vote)

sal= int (input("salary:"))
tax =sal*(0.1 , 0.2)[sal<50000]
print ( tax)

a= int (input("a:"))
b = int(input("b:"))
c = a + b
print(c)

a= float (input("a:"))
b = float(input("b:"))
c = float(input("c:"))
print(a*b*c/100)


# string

str= "sandilyaad"
print (str[4])

# slicing :- acessing part of string

