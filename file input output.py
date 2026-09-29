'''
f = open("C:\\Users\\Pranita Lohokare\\OneDrive\\Desktop\\demo.txt", "r")
#read entire file
data  = f.read()
print(data)
print(type(data))

#read line by line
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)

#write data into file
f = open("C:\\Users\\Pranita Lohokare\\OneDrive\\Desktop\\demo.txt", "w")
f.write("i want to learn data structures and algorithms")

#append data into file
f = open("C:\\Users\\Pranita Lohokare\\OneDrive\\Desktop\\demo.txt", "a")
f.write("\n then i will crack the interview")

#r+
f = open("samp.txt", "r+")
f.write("abc")
print(f.read())
f.close()

#with syntax(it automatically closes file afer operation completion)
with open("samp.txt", "a") as f:
    data = f.write("\n welcome pranita")
    print(data)

import os
os.remove("samp.txt")

#create a new file "practice.txt" using python. add the following data in it:

with open("practice.txt", "w") as f:
    f.write("hi everyone\nwe are learning file i/o\nusing java\ni like programming in java")

#write a program that replace  all occurances of "java" with "python" in above file.
with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

#find the word exist in file or not
def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("found")
        else:
            print("not found")
check_for_word()

#check word present in which line
def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
check_for_line()

#data in a file is numbers seprated by comma. print the count of even numbers:
with open("practice2.txt", "w") as f:
    f.write("1,2,3,4,5,6,7,8,9")

#basic way
with open("practice2.txt", "r") as f:
    data = f.read()
    print(data)
  
    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
'''
#better way
count = 0
with open("practice2.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)

    
    
    

    


