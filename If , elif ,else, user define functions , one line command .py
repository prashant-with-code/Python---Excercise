#!/usr/bin/env python
# coding: utf-8

# # grade code

# In[8]:



p=50


if p>75:
    print("grade O")
elif 60<p>75:
    print("grade A")
elif 50<p<60:
    print("grade B")
elif 35<p<50:
    print("grade c")
else:
    print("fail")
    


# In[23]:


#nested
p=50


if p>75:
    print("grade O")
elif 60<p>75:
    print("grade A")
elif 50<p<60:
    print("grade B")
elif 35<p<50:
    print("grade c")
else:
    if p<35:
        print("fail")
    
    


# # n divisible by 2 or 3

# In[34]:


#if 
n=7

if n%2==0:
    print("divisible by 2 , not 3")
else:
    print("divisible by 3 , not 2")


# In[35]:


if n%2==1:
    print("divisible by 2 , not 3")
else :
    print("divisible by 3 , not 2")


# In[46]:


#if elif
n=7


if n%2==0:
    print("divisible by 2 , not 3")
elif n%2==1:
    print("divisible by 2,and 3")
else:
    print("not divisible by 2, and 3")
    


# In[49]:


if n%2==0 and n%3==1:
    print("divisible by 2 , not 3")
elif n%2==1 and n%3==0:
    print("divisible by 2,and 3")
else:
    print("not divisible by 2, and 3")
    


# In[54]:


d1={"name": ["rohit","sumit","dhaval"] , "age" :[67,62,34], "hobby":["travelling","reading","cooking"], 
    "Fav.food":["maharastrian","chinese","punjabi"]}
d1


# In[56]:


import pandas as pd
pd.DataFrame(d1)


# In[64]:


d1["Fav.food"]= "chinese"

pd.DataFrame(d1)


# In[65]:


d1={"name": ["rohit","sumit","dhaval"] , "age" :[67,62,34], "hobby":["travelling","reading","cooking"], 
    "Fav.food":["maharastrian","chinese","punjabi"]}
d1


# In[66]:


import pandas as pd
pd.DataFrame(d1)


# In[6]:


for i in range(5):
    for k in range(5):
        for j in range(5):
            print("AIS")
        print("pune")


# In[3]:


5*5*5


# In[9]:


n=7
if n%2==0:
    if x%3==0:
        print("divisible by 2  not 3")
    else:
        print("divisible by 3  not 2")
else:
    if n%3==0:
        print("divisible by 2 and 3")
    else:
        print("not divisible by 2 and 3")
        


# # user define function

# In[37]:


def addition(a,b):
    ans=a+b
    print(ans)


# In[38]:


addition(46,54)


# In[41]:


def addition(p,j):
    l=p+j
    print(l)


# In[43]:


addition(5,6)


# In[44]:


def sub (a,b):
    ans=a-b
    print(ans)


# In[46]:


sub(5,6)


# In[47]:


sub(24031997,31102003)


# In[48]:


def mul(a,b):
    ans = a*b
    print(ans)


# In[49]:


mul(78,87)


# In[50]:


mul(5,5)


# In[56]:


def power(a,b):
    ans=a**b
    print(ans)


# In[57]:


power(2,3)


# In[58]:


power(5,4)


# In[60]:


def cube(n):
    ans=n**3
    print(ans)


# In[61]:


cube(4)


# In[62]:


def cube (n):
    ans=n**3
    print(ans)


# In[63]:


cube(64)


# In[82]:


def mean(a,b,c,d,e):
       ans=(a+b+c+d+e)/5
       print(ans)
   


# In[83]:


mean(12,45,78,96,32)


# In[92]:


def mean(a,b,c,d,e,f,g):
    ans=(a+b+c+d+e+f+g)/5
    print(ans)


# In[93]:


mean(14,45,12,13,14,15,54)


# In[3]:


def arithmetic(a,b):
    ans=(a+b,a-b,a*b,a/b)
    print(ans)


# In[12]:


arithmetic(3,5)


# In[1]:


def variance(*AIS):
    m=sum(AIS)/len(AIS)
    print(m)
    
    
 
    
    
variance(1,2455,65,45,12,5)    


# In[4]:


def factorial (n):
    fact = 1
    
    
    for i in range(1,n+1):
        fact *= i
        
    return fact


# In[5]:


factorial(5)


# In[14]:


def factorial(n):
    fact = 1
    
    
    for i in range(1,n+1):
        fact *= i
        
        
    return fact        
         
        
        


# In[15]:


factorial(6)


# In[16]:


f = lambda x: "even" if x % 2 == 0 else "odd"

f(10)


# In[17]:


def add(n):
    if n % 2:
        print(n)


# In[19]:


add()


# In[10]:


def even(*n):
    even_sum = sum(x for x in n if x % 2 == 0)
    return even_sum


even_sum_result = even(1,2,5,46,4,5,42,45,2)
print(even_sum_result)


# In[2]:


def bodmas(a,b):
    add = a+b
    subtraction = a-b
    multiplication = a*b
    division = a/b
    return add,subtraction,multiplication,division

l=bodmas(10,5)
print(l)


# In[7]:


def even(*n):
    for num in n:
        if num % 2 ==0:
            print(num)
            
even(1,2,5,46,4,5,42,45,2)            


# # one line command

# In[13]:


add = lambda x,y:x+y
l = add(10,20)
print(l)


# In[19]:


sub=lambda x,y:x-y
l= sub(10,20)
print(l)


# In[22]:


multiplication = lambda x ,y,z:x*y*z
l = multiplication(9,8,7)
l


# In[26]:


power= lambda base,exponent:base**exponent
l1=power(2,3)
l2=power(5,4)
print(l1)
print(l2)


# In[30]:


cube = lambda x:x**3
cube(8)


# In[31]:


cube = lambda x :x**3
cube(10)


# In[32]:


mean=lambda a,b,c,d,e:(a+b+c+d+e)/5
mean(71,82,93,45,65)


# In[38]:


arithmatic=lambda x,y:(x+y,x-y,x*y,x/y)
arithmatic(10,10)


# In[ ]:


def var(*x)

