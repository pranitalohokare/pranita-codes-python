#while loop
'''
count = 1
while count <= 5 :
    print("hello")
    count += 1

# print multiplication table of a number using while loop
n = int(input("enter the number: "))
i = 1
while i <= 10 :
    print(n, "*", i, "=", n*i)
    i += 1

#print element of list using loop
list = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i<= len(list)-1 :
    print(list[i])
    i += 1 

#search an element in  tuple using while loop
tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter the number to find: "))
i = 0 
while i <= len(tup)-1 :
    if(tup[i] == x):
        print("found at index", i)
        break
    i += 1
else:
    print("not found")

i = 1
while i <=10:
    if(i%2 == 0):
        i += 1
        continue #skip
    print(i)
    i += 1

#for loop
# print elements of list using for loop
list = [1,4,9,16,25,36,49,64,81,100]
for element in list :
    print(element)

#search an element in tuple using for loop
tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter the number to find: "))
for index in range(len(tup)) :
    if(tup[index] == x):
        print("found at index", index)
        break   
'''
# range function
for i in range(1,11,2): # 1 to 10 increment by 2
    print(i)

for i in range(1,101,1):
    print(i)

for i in range(100,0,-1):
    print(i)

n = int(input("enter the number: "))
for i in range(1,11):
    print(n, "*", i, "=", n*i)

#pass statement
for i in range(1,11):
    pass  # placeholder for future code
print("some useful work")

num = int(input("enter the number: "))
sum = 0
i = 1
while i <= num :
    sum += i
    i += 1
print("sum is:", sum)

# factorial of a number
num = int(input("enter the number: "))
fact = 1
i = 1
while i <= num :
    fact *= i
    i += 1
print("factorial is:", fact)

# factorial using for loop
num = int(input("enter the number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print("factorial is:", fact)
