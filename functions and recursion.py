#function defination
'''
def calc_sum(a, b): #parameters
   #sum = a + b
    #print(sum)
    return a + b
    
sum = calc_sum(5,9) #function call; arguments
print(sum)

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(99, 88, 67)

nums = [9, 8, 5, 7]

def print_len(list):
    print(len(list))

print_len(nums)

#to print items in one line
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(nums)

#print fact using func

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(10)

#usd to inr
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "usd =", inr_val, "inr")

converter(90)

#even odd using function
def even_odd(n):
    if n%2 == 0:
        print("even")
    else:
        print("odd")

even_odd(2)
'''
'''
# Recursion
def show(n):
    if(n == 0): #base case
        return
    print(n)
    show(n-1)
show(6)

#factorial using recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1) * n
print(fact(9))

#sum of first n natural numbers using recursion
add = int(input("enter a number: "))
def sum (n):
    if n == 0:
        return 0
    return sum(n-1) + n
print(sum(add))
'''
#print list using recursion
def list_print(list,index = 0):
    if index == len(list):
        return 
    print(list[index])
    list_print(list, index + 1)

nums = [10, 20, 30, 40, 50]
list_print(nums)




    

