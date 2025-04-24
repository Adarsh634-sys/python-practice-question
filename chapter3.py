"""marks = [94,98,75,89,90,45]
print(len(marks))
print(marks[0])"""

# wap to find greatest number

a= int(input("enter the value of a:"))
b= int(input("enter the value of b:"))
c= int(input("enter the value of c:"))
if(a>=b and a>=c):
    if(a==b and a==c):
        print("a is equal to b and c")
    elif(a==b):
        print("a is equal to b")
    elif(a==c):
        print("a is equal to c")
    else:
        print("a is greater than b and c")
    # print("a is greater than b ")
elif(b>=a and b>=c):
    if(b==a):
        print("b is equal to a")
    elif(b==c):
        print("b is equal to c")
    else:
        print("b is greater than a and c")
    # print("b is greater than a")
else:
    if(c==a):
        print("c is equal to a")
    elif(c==b):
        print("c is equal to b")
    else:
        print("c is greater than a and b")
    # print("c is greater than a and b")"""

# wap to find odd and even number 

"""a= int(input("enter the value of a:"))
if(a%2==0):""
    print("a is even")
else:
    print("a is odd")
d =0
while True:
    print(d,"hello")
    d+=1
    if(d==100000):
        break"""

#
#wap to find simple intrest 
"""principle= int(input("enter the principle:"))
rate= int(input("enter the rate:"))
time= int(input("enter the time:"))

simple_interest = (principle*rate*time)/100
print("simple interest is:", simple_interest)"""


my_list = [1, 2, 3, 4, "A"]
numeric_values = [x for x in my_list if isinstance(x, (int, float))]
total = sum(numeric_values)
print(total)  # Output: 10

# wap to find the sum of all the numbers in the list            

"""list=[1,2,3,4,5,]
sum = (sum(list))
print(sum)"""

"""list=[1,2,3,4,5,]
list.append (5)
print(list) """

# CALculate the the length of string

list=[1,2,3,6,5,7,7]
list.sort(reverse = True)
print(list)

# insert many element in list

list=[1,2,3,4,7,5,4,9]
list.extend([0,8,9,6,5,4,7])
print(list)

str ="my name is adarsh "
char=str.replace("a","N")
print(char)

# pop method in list

list=[1,2,3,4,5,6,7,8,9]
list.pop(2)
print(list)

# tuple

adarsh=(1,2,3,4,5,6,7,8,9)
print (sum(adarsh));
print(type(adarsh));
print(adarsh[3]);
print(adarsh[3:5]);
print(adarsh.index(4));
print(adarsh.count(5));

#wap to the user to enter the names of their 3 favourite movies and store them in a list
movies1= input("enter the name of your first favourite movies:")
movies2= input("enter the name of your second favourite movies:")
movies3= input("enter the name of your third favourite movies:")

movies=[]
movies.append(movies1)
movies.append(movies2)
movies.append(movies3)
print(movies)

# wap to check if a list contains a plaindrome of elements.(hints:use copy() method
#[1,2,3,2,1] 

list1=[1,2,3]
list2=[1,2,1]

copy_list1 =list1.copy()
copy_list1.reverse()

if(copy_list1==list2):
    print("list is pailndrome")
else:
    print("list is not pailndrome")

    # wap to count the number of student with the "A" grade in the following tuple
    #["c","d","A","A","B","B","A"]
    tuple=("c","d","A","A","B","B","A")
    count=tuple.count("A")
    print(count)

    # wap to store the above values ina list and sort them from "A" to "D"
  
    list=["c","d","A","A","B","B","A"]
    list.sort(reverse=True)
    print(list)
      
