def cal_sum(a, B):
    sum=a+B
    print(sum)
    return sum

cal_sum(2,3)

# 1. average of three numbers

"""def calc_avg(a,b,c):
    avg=a+b+c/3
    print(avg)
    return(avg)

calc_avg(23,45,67)"""

 # 3. default argument

"""def cal_product(a=2,b=3):
    product=a*b
    print(product)
    return product
cal_product()"""

# Q3. write a function to print the length of a list 

"""cities=['bangalore','chennai','mumbai','delhi','kolkata']

def print_len( cities):
   print(cities)
   return cities"""


#Q.4

"""cities=['bangalore','chennai','mumbai','delhi','kolkata']
heroes=['superman','batman','spiderman','ironman','captain america']
def print_len(list):
    print(len(list))
    return len(list)
print_len(cities)
print_len(heroes)"""




#.q.5 write a function to convert USD to INR

"""def converter(usd):
    inr=usd*83.5
    print(inr)
    return inr
converter(100)"""

# Q.6write a function to find the factorial of n (n is parameter)


def calc_fac(n=7):
    
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
calc_fac()

# q.7 write a function odd number then print in string this is odd number otherwise print this is even number

"""def check_odd_even(n):
    ifn%2==0:
        print("this is even number") 
    else:
"""


