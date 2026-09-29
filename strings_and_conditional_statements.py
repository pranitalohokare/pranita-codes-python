'''
#sring can be written in three types of quotes
str1 = "my name is pranita"
str2 = 'my name is pranita'
str3 = """my name is pranita"""

print(str1)
print(str2)
print(str2)
print(len(str3)) #length of string
print(str1[0]) #first character # we only can access the characters using indexing cannot modify(manipulate)them  
print(str1 + " " + str2) #string concatenation
print(str1[0:6]) #slicing from index 0 to 5 because ending index is not included
print(str1[7:9]) #from index 7 to 8
print(str1[3:]) #from index 3 to end
print(str1[:6]) #from start to index 5
print(str1[-3 : -1]) #slicing using negative indexing
print(str1[-1]) #last character

#escape sequence characters
str4 = "hello world \n welcome to python programming" 
str5 = "hello world \t welcome to python programming" 

# more string functionsZ
print(str1.endswith("ita")) # checks if string ends with given substring
print(str1.capitalize()) # capitalizes first character of string (no change in original string)
print(str1)
str1 = str1.capitalize() # capitalizes first character of string (changes original string)
print(str1)
print(str1)
print(str1.replace("a", "A")) # replace all occurrences of 'a' with 'A' 
print(str1.find("pranita")) # returns starting index of substring if found else -1 
print(str1.count("a")) # counts occurrences of given substring in string


#conditional statements

light = "0"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")  
elif(light == "yellow"):
    print("look")  
else:
    print("light is broken") 

#grade students based on marks

marks = 89
if(marks >= 90):
    print("grade A")
elif(marks >= 80 and marks < 90):
    print("grade B")
elif(marks >= 70 and marks < 80):
    print("grade C")
elif(marks >= 60 and marks < 70):
    print("grade D")
else:
    print("Fail")  

#nesting
age = 89
if(age >= 18):
    if(age >= 80):
        print("cannot drive due to age")
    else:
        print("can drive")   
else:
    print("cannot drive")  

#check even or odd
num = int(input("enter the number: "))
if(num % 2 == 0):
    print("number is even")
else:
    print("number is odd")

#find greatest among three nubers entered by user
a = int(input("A=: "))
b = int(input("B=: "))
c = int(input("C=: "))
if(a>b and a>c):
    print("A is greater number",a)
elif(b>a and b>c):
    print("B is greater number",b)
else:
    print("C is greater number",c)   
'''
#check if number is multiple of 7
num = int(input("enter the number: "))
if(num % 7 == 0):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")    