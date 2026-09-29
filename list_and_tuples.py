'''
Docstring for list_and_tuples
#list in python similar to array in other programming languages
student = ["pranita", 21, "cse", 9.5] #list can have multiple data types arrays dont
print(student[0])
print(student[1])
student[0] = "panu" #modifying list element
print(student)

#list slicing(same as string slicing)
print(student[0:2])
print(student[1:])
print(student[:2])
print(student[-2 : -1])

#list methods(functions)

list = [2,1,3]
list.append(4)
list.sort()
print(list)

print(list.sort())#returns none because sort() modifies the original list and does not return anything
print(list.append(5))#returns none but changes are made into the original list
print(list)
list.sort(reverse=True)
print(list)

list2 = ["banana", "litchi", "apple"]
list2.sort()
print(list2)
list2.reverse()
print(list2)
list2.insert(2, "mango")
print(list2)
list2.remove("litchi")
print(list2)
list2.pop(2)
print(list2)

#tuples in python(immutable)

tup = (2, 1, 3 ,6)
print(type(tup))
print(tup)
print(tup[0])
tup1 = () #valid empty tuple
print(tup1)
tup2 = (2,) #valid single element tuple, if we dont seprate it by comma it doesnt defined as tuple, take it as integer
print(tup2)
#slicing in tuple
print(tup[0:2])
#tuple methods
print(tup.index(2)) #returns index of given element
print(tup.count(3)) #returns count of given element in tuple


#WAP to ask user to enter names of their 3 favorite movies & store them in a list
m1 = input("enter name of movie 1: ")
m2 = input("enter name of movie 2: ")
m3 = input("enter name of movie 3: ")
list = []
list.append(m1)
list.append(m2)
list.append(m3)
print(list)
'''

#write a program to check a list is palindrome or not
l = [1, 2, 2]
copy_l = l.copy()
copy_l.reverse()
if(copy_l == l):
    print("list is palindrome")
else:
    print("not palindrome")

#WAP to cout the number of students with "A" grade in the tuple
grades = ("a", "b", "c", "a", "a", "d", "b")
count = grades.count("a")
print("number of students with grade 'a': ", count)  


lis = ["a", "b", "c", "d", "a",]
lis.sort()
print(lis)
