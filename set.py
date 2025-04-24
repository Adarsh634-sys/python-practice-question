# set Definition:- set is the collection of the unordered items, each element in the set must be unique & immutab,e
collection = {1,2,3,"Adarsh","Aditya","Aman","Shivansh"}
print(collection)
print(type(collection))
print(len(collection))

# empty set  create

empty_set=set()
print (type(collection))

collection.add(4)
print(empty_set)

collection.remove(2)
print(collection)

"""collection.clear()
print(collection)"""

collection.add((1,2,3))
print(collection)

#pop method in set

collection.pop()
print(collection)


# set method

"""set.union(set2)# combinees both set values and returns new
set.intersection(set2)"""# combines common values and returns new

set1={1,2,3,4,5}
set2={2,3,4,7,8}
print(set1.union(set2))

print(set1.intersection(set2))


# practice question

# wap to store the following word meanings in a python dictonary
"""Table:"a piece of furniture ", list of facts and figures"
Cat:"a small animals"""

dictionary={
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal",
}
print(dictionary)

# Q. you are given list of students assume one classroom is required for 1 subject. how many classrooms are needed by all student

set1={"python","java","c++","python","javascript","java","python","java","c++","c"}

print(len(set1))


#Q. wap to enter the marks of 3 subject from the user and store them in a dictionary . start with an empty dictionary & add one by one . use subject as key & marks as value . 
marks={}

subject= int(input("enter the math:"))
subject= int(input("enter the chemistry:"))
subject=int(input("enter the biology:"))
marks.update({"math":subject})
marks.update({"chemistry":subject})
marks.update({"biology":subject})

print(marks)

#Q. wap to figure out a way to store 9&9.0 as seprate values in the set .(you can take help of built-in data types)
values= {9,"9.0"}
print(values)







