#!/usr/bin/env python
# coding: utf-8

# # if - else 

# In[9]:


people = 50
cats =30
dogs = 15

if people < cats:
    print("Too many cats!")
if people > cats:
    print("Not many cats!")


# In[10]:


people = input("Enter the no of people")
cars = input("enter the no of cars")
trucks = input("enter the no of trucks") 

if cars < people:
    print("We should take the cars.")
elif cars > people :
    print("We should not take the cars.")
else:
    print("We can't decide")


# # Loops and List

# In[16]:


the_count = [1,2,3,4,5]

for num in the_count:
    print(f"This is the count {num}")


# In[17]:


for num in the_count:
    print('this is the count' , num)


# In[19]:


l = ['a','b','c',4,5]
for n in l:
    print(f" Your element is: {n}")


# In[24]:


elements = []
count = 0
for i in range(0,6):
    print(f"adding {i} to the list")
    elements.append(i)
    count += 1
    if count < 6:
        print("The updated list is",elements)
        
    
print(f"\nThe Final list is {elements}")


# # While 

# In[29]:


i = 0
num = []
while i<6:
    print(f"At the top i is {i}")
    num.append(i)
    i+=1
    print("Numbers now:",num)
    print(f"At the bottom i is {i}")
    
print("The numbers: ")
for n in num:
    print(n , end = ' ')


# In[30]:


for a in num:
    print(a1)


# # Function

# In[36]:


def greet(name,lan):
    if lan == "english":
        print(f"Hello {name} , Good morning")
    elif lan == "spanish":
        
        print(f"Ola {name} ")
    elif lan == 'german':
              print(f"Hallo {name} , Guten Morgen")


greet('chetan','german')


# In[39]:


def add_num(x,y):
    add = x+y
    return(add)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
add_num(x,y)


# In[42]:


def myfun(x,y = 50):
    print('x : ',x)
    print('y : ',y)
    print('x+y=',x+y)
    
myfun(2,6)


# In[44]:


def myfun1(*argv):
    for arg in argv:
        print(f"{arg}")

myfun1("what",'is','your','name')
        


# In[55]:


def myfun2(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} ==> {value}")
myfun2( first = "Geeks", mid = "for" , last = "Geeks")


# In[51]:



def add_2(x,y):
    add = x+y
    return(add)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
add_num(x,y)


# In[61]:


add_two = lambda a,b : a+b
print(add_two(2,5))


# In[73]:


def name(x):
    w = [1,2,3,4]
    
    print(" w = [1,2,3,4]")
    z = 0
    for i in range(0,4):
        z += x[i]*w[i]
    return z
x = []
i = 0
for i in range(0,4):
    a = int(input("Enter the value:"))
    x.append(a)
            
print(x)    
name(x)
        
        


# In[64]:


import numpy as np

w = [1,2,3,4]
w1 = np.array(w)

def nn(x_vec):
    a= np.transpose(w1)
    z = np.dot(a,x_vec)
    return(z)
x=[1,3,5,7]
y = nn(x)
print(y)


# In[67]:


x = int(input('Enter the number: ')
fac = 1
for i in range(1,x+1):
        fac *= i
        
print(fac)
        


# In[74]:


def fact(num):
    factorial = 1
    if num < 0:
        print("sorry")
    elif num == 0:
        print("1")
    else:
        for i in range(1,num+1):
            factorial *= i
    return factorial

fact


# In[78]:





# In[76]:





# In[ ]:




