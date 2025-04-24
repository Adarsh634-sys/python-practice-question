# recursive funcion
"""def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
show(5)"""

# factorial using recursion 
"""def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(2))"""

# q. write a function to find the sum of n natural numbers using recursion
"""def sum(n):
    if (n==0):
        return 0
    return sum(n-1)+n
result=sum(5)
print(result)"""

#. Q. write a recursive function to print all el3ements in a list

fruit = ['apple', 'banana', 'cherry', 'orange']
def print_list(list,indx=0):
    if indx==len(list):
        return
    print(list[indx])
    print(list,indx+1)
print_list(fruit)
