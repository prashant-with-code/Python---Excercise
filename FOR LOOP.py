#!/usr/bin/env python
# coding: utf-8

# In[2]:


4+0,4+1,4+2,4+3,4+4,4+5,


# In[5]:


for i in range(1,6):
    for j in range(0,6):
        l=i+j
        print(l)     


# In[1]:


#creat a list of 1 to 20 numbers using for loop

for i in range(1,21):
    l=[]
    l.append(i)
print(l)  


# # create a list of 20 to 1 value using for loop

# In[8]:


#create a list of 20 to 1 value using for loop
l=[]
for i in range(20,0,-1):
    l.append(i)
    
 
print(l)


# # cube of odd values between 20 to 40

# In[22]:


# cube of odd values between 20 to 40
l=[]
for i in range (21,41,2):
    cube = i**3
    l.append(cube)
    
print(l)    


# # take 5 freinds name in list and second list is age

# In[30]:


#take 5 freinds name in list and second list is age
names = ["prashant","rohit","om","ram","rohan"]
ages = [23,24,25,26,27]

for i in range(len(ages)):
    print("my name is",names[i],"and my age is",ages[i])


# #Slove using if and for loop and data types methods

# # if statement examples

# In[1]:


string = "Hello World"

if len(string) ==0:
    print("string is empty")
else:
    print("string is not empty")


# In[2]:


n = int(input("enter the number"))

if n%2==0:
    print("number is even")
    
else:
    print("number is odd")


# In[7]:


n=89

if n>100:
    print("number is gratter")
else:
    print("number is less")


# In[9]:


l=[]

if l:
    print("list is empty")
else:
    print("list is not empty")


# In[18]:


variable = 8.16

if isinstance (variable ,int):
    print("variable is integer ")
else:
    print("variable is not integer")


# In[23]:


variable = 3.14

if isinstance (variable,int):
    print("varible is int")
elif isinstance (variable,float):
    print("variable is float")
else:
    print("varible is not int and float")


# In[28]:


l={}

if l:
    print("empty")
else:
    print("not empty")


# In[33]:


n1=100
n2=200
n3=300


if n1 > n3:
    print("grater n1")
elif n2 < n1:
    print("lessthan n2")
elif n3 > n2:
    print("grater n3 not n2")
else:
    print("not grater and not lessthan")


# # for loop examples

# In[34]:


my_list = [1,2,3,4,5,6]
for item in my_list:
    print(item)


# In[38]:


my_string = "helloWorld"
for char in my_string:
    print(char)
    


# In[42]:


my_dict = {"a":1,"b":2 , "c":3}
for key in my_dict.keys():
    print(key)


# In[44]:


my_dict = {"a":1,"b":2 , "c":3}
for value in my_dict.values():
    print(value)


# In[50]:


for n in range(0,30,2):
    print(n)


# In[62]:


for n in range(1,5):
    for j in range(0,5):
        l=n+j
        print(l)


# In[67]:


l = [1,2,3,4,5,6]
count = 0
for item in l:
    if item ==1:
        count+=1
    print("the count of 1 in the list is :{count}")    


# In[73]:


l=[10,5,8,12,3]
max_num = l[0]
for num in l:
    if num>max_num:
        max_num=num
    print(f"the maximum number in the list is:{max_num} ")    


# # write code count length of string
# 

# In[15]:


#write code count length of string

def count_length(string):
    return len(string)

my_string= "Hello, World"
length = count_length(my_string)
print("lenght of the string:",length)


# # given a list write python code to swap first and last element of the list

# In[9]:


#given a list write python code to swap first and last element of the list
def swap_first_least(lst):
    if len(lst) >=2:
        lst[0], lst[-1] = lst[-1], lst[0]
        
my_list = [1,2,3,4,5]

swap_first_least(my_list)
print(my_list)


# # write a python program to get the sum of a only non negative integer

# In[16]:


#write a python program to get the sum of a only non negative integer

def sum_non_negative(numbers):
    result = 0
    for num in numbers:
        if num >= 0:
            result += num
    return result



nums = [1,4,-5,-20,10]
total = sum_non_negative(nums)
print("sum of non-negative numbers:",total)


# # write a code of factorial

# In[17]:


#write a code of factorial

def factorial(n):
    result=1
    for i in range (1,n+1):
        result *=i
    return result



number = 3
factorial_result = factorial(number)
print("factorial of", number,"is",factorial_result)


# In[ ]:




