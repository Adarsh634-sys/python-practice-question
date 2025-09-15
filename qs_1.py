#Write a Python program to check whether a number is even or odd.

"""number= int(input("inter the number "))
if number %2 == 0:
    print("even")
else:
    print("odd")"""

# Take a string input and count how many vowels it has.

text = input('Enter the string :')
vowels = "aeiouAEIOU";
count = 0;
for char in text:
    if char in vowels:
        count += 1
print("number of vowels" ,count);

