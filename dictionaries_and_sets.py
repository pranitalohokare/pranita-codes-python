#dictionaries are used to store key-value pairs in Python. they are unordered, mutable, and indexed by keys.
'''
info = {
    "name": "pranita",
    "age": 21,
    "gender": "female",
    "is_adult": True,
    "subjects": ["maths", "python", "java", "dbms", "os"]
    }
print(info)
print(info["age"])
info["name"] = "adf"
print(info)

#nested dictionary
student = {
    "name" : "atharv",
    "subjects" : {
        "phy" : 40,
        "chem" : 39,
        "maths" : 41
    }
}
print(student)  
print(student["subjects"]) 
print(student["subjects"]["maths"])

#dictionary functions
print(student.keys()) #prints all keys in dictionary
print(student.values()) #prints all values in dictionary
print(student.items()) #prints all key-value pairs as tuples in a list
student["age"] = 21 #adding new key-value pair
print(student)
del student["age"] #deleting key-value pair
print(student)
print(list(student.values())) #converting dictionary keys to list
print(list(student.keys())) #converting dictionary values to list
print(student.items()) #prints all key-value pairs as tuples in a list
print(student.get("name")) #accessing value using get() method
student.update({"city" : "pune"})
print(student)
new_dict = {"country" : "india"}
student.update(new_dict)
print(student)


#set in python 
collection = {1, 2, 3, 4, 5} #sets do not allow duplicate values
collection2 = {4, 5, 6, 7, 8}
print(collection)
print(len(collection)) #length of set
coll = set() #empty set

#methods in set
collection.add(6) #adding element to set
collection.add(3) #adding duplicate element (will not be added)
collection.add("pranita") #adding string element to set
print(collection)
collection.remove(2) #removing element from set
print(collection)
print(collection.union(collection2))
print(collection.intersection(collection2))
'''
#WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary and add one by one. use subject name as key and marks as value.
'''
marks_dict = {}

sub1 = input("enter name of first subject: ")
marks1 = int(input("enter the marks of first subject: "))

sub2 = input("enter name of second subject: ")
marks2 = int(input("enter the marks of second subject: "))

sub3 = input("enter name of third subject: ")
marks3 = int(input("enter the marks of third subject: "))

marks_dict.update({sub1: marks1})
marks_dict.update({sub2: marks2})
marks_dict.update({sub3: marks3})

print(marks_dict)
'''
#store 9 and 9.0 as seprate values in the set
val = {9, "9.0"}
print(val)
