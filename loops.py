"""count=0
while count<=5:
    print("hello")
    count+=1"""

#q1. print multiplication table of numner using while loop

"""num= int(input("inter the input"))
i=1
while i<=10:
    print(num*i)
    i+=1"""

#q2. print the element of the following list using loop

"""[1,4,9,16,25,36,49,64,81,100]

num=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(num):
    print(num[i] )
    i+=1"""

#q3. SEARCH FOR A NUMBER X IN THIS TABLE USING WHILE LOOP.

num=[1,4,9,16,25,36,49,64,81,100]
x= int(input("inter the number :"))
i=0
while i<len(num):
    if (num[i]==x):
        print("number found" i)
    else:
        print("finding")
    i+=1


