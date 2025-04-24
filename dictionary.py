# Dictionary

info={
    "key":"value",
    "name":"Adarsh",
    "class":"Bca4th",
    "subject":["python","java","c++"],
    "topics":["list","tuple","dictionary","set"],
    "is_adult":True,
    "marks":[90,80,70,],


    }
print(info)

info ["name"]="luckyshandilya"
print(info)

#null dictionary

info={}
info["name"]="Adarsh"
print(info)

#nested diictionary
student={
    "name":"Adarsh",
    "class:":"Bca4th",
    "subject":["python","java","c++"],
    "score":{
        "python":90,
        "java":80,
        "c++":70,
        }
    }

print(student)

Adarsh={
    "name":"lucky",
    "class":"Bca4th",
    "brother":["Aditya","Aman","shivasnsh"],
    "father":{
        "id":123,
        "salary":100000,
        "tax":1000,
    }

}
print(Adarsh["father"]["salary"])

#type casting in list

#mydict.keys() return the list of keys in the dictionary

print(list(Adarsh.keys())),
print(tuple(Adarsh.keys())),

# total nummber of keys in adarsh
print(len(Adarsh.keys())),

#mydict.values() return the values in the dictionary

print(list(Adarsh.values())),

#mydict.items() return the key value pair as tuple in the dictionary
print(Adarsh.items),

#mydict.update() update the dictionary with the key value pair of another dictionary

Adarsh.update({"city":"bihar"})
print(Adarsh),


new_dict={"village": "post","dist":"samastipur","name":"sandilyaad"}

Adarsh.update(new_dict)
print(Adarsh),



