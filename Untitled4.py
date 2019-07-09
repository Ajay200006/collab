#!/usr/bin/env python
# coding: utf-8

# # Markdown Basics
# ## Markdown Basics
# ### Markdown Basics
# #### Markdown Basics
# #### Markdown Basics
# ##### Markdown Basics
# 
# * **Point1** (Bold)
# * *Point2* (Itallic)
# * ***Point3*** (Bold and Itallic)
# 
# * Normal Text
#   *Sublist 1
#   *Sublist 2
# 
# > 1. Point1
# > 2. Point2
# 
# * ***Adding links to Markdowm***
# 
# * Google SIte --[1]: http://www.google.com
# * msn         --[2]: http://www.msn.com
# 
# - []Option1
# * Google Site -- [Google][1]
# [1]: http://www.google.com

# ### Python Basics
# * Python verson 3.7
# * Functional Programming
# * Object oriented Programming
# * Scripting Programming
# 

# In[2]:


print("Hello Gitam")
print("Hyderabad")


# In[3]:


print("Hello,gitam",end="|||")
print("Hyderabad",end="|||")
print("Python Programming")


# In[4]:


n1 = 100 # single variable assignment
a = b = c = 20 # Multi Variable Assignment of the same value
a1,b1,c1 = 111,222,333 # Multi Varible Assignment with 
print(n1)
print(a,b,c)
print(a1,b1,c1)


# In[5]:


a = 100;
s1 = "python"
s2 = "p"
f1 = "3.3"
print(a);
print(s1);
print(s2);
print(f1);
print(type(a));
print(type(s1));
print(type(s2));
print(type(f1));


# In[6]:



s1 = "100"
print(type(s1))
a = int(s1)
print(type(a))
f = 1.5
a1 = int(f)
print(type(a1))
print(a1)


# In[7]:


# A number is given 1234
# Digit count
a1 = 1234
print(len(str(a1)))


# In[8]:


s1 = input("Enter your name")
print(s1)
print(type(s1))


# # iterative statement

# In[2]:


# Need print "Gitam" for 5 times
print("Gitam")
print("Gitam")
print("Gitam")
print("Gitam")
print("Gitam")


# In[4]:


x=0
while x<5:
    print("Gitam")
    x=x+1


# In[5]:


# Print N Natural numbers using while loop
n=int(input("enter n "))
x=1
while x<=n:
    print(x,end =" ")
    x=x+1


# In[6]:


# Sum of Even number Series
n=int(input("enter n "))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)


# ###  Relational operators
# - ==
# - !=
# - Greater(>)
# - less than(<)
# - less than or equal to(<=)
# - greater than or equal to(>=)

# In[1]:


# Given number is prime or not
def isprime(n):
    flag=True
    for i in range(2,n//2+1):
        if n% i == 0:
            flag = false
            return flag
        return flag
isprime(11)


# In[9]:


# Function to find the prime numbers count from 1 to n

def primecount(n):
    cnt=0
    for a in range(2,n+1):
        k=0
        for i in range(2,a//2+1):
            if a % i == 0:
                k = k+1
        if (k<=0):
            cnt=cnt+1
    return cnt
Primecount(10)


# In[1]:


# individual digit factorial sum is same as original number 
# example :-
# 145 -- Yes (5! + 4! + 1! = 145)
# 123 -- No (3! + 2! + 1!)
def factorial(n):
    fact = 1
    return fact
def digitfactsum(n):
    sum = 0
    buffer = n
    whilen ! = 0 :
        r - n % 10
        sum +- factorial(r)
        n - n // 10
        if sum -- buffer:
            return " Yes"
        else:
            return "No"
        return
    print(digifactsum(145))
    print(digitfactsum(123))


# In[ ]:


# Function to return the count of palindrome number two limits
# Input : 1 10
# Output : 9(1,2,3,4,5,6,7,8,9)


# Onput : 11 100
# Output: 9(11,22,33,44......,99)
def ispalindrome(n):
   rev = 0
   buffer = n
   while n!= 0:
       r = n % 10
       rev = rev * 10 + r
       n = n // 10
   if rev == buffer:
       return True
   else:
       return False
   return
def countpalindrome(lb,ub):
   cnt = 0
   while lb !=ub:
       # Implement
       if ispalindrome(lb) == True:
           cnt = cnt + 1
       lb = lb + 1
   return cnt
countpalindrome(1,10)


# In[2]:



# ASCII
# A-Z : 65-90
# a-z : 97-122
# 0-9 : 48-57
# space: 32
def printupper(x):
   for i in range(len(x)):
       if ord(x[i]) >= 65 and ord(x[i]) <= 90:
           print(x[i])
   return 
printupper("pYThon")
("")
# Function to print "samecount" if the count of
# upper and lower case is same
# print "programming" if not same
# example : pyTHon -- 2 TH (uppercase) -- samecount
                  -- 4 pyon (lower case)
         : PyThoN -- 3 PTN (uppercase)
                  -- 3 yho (lowercase)
m
# Function to print "Python" if the count of
# Upper and lower case is same
# Print "Programming" if not same
# ex: PyThOn ---3 P T O (upper case)
#              3 y h n (lower case)
#PytHon --P H (2)
#       --y t o n(4) -Programming


def findCount(str):
   cntUpper =0
   cntLower =0
   for x in range(len(str)):
       if ord(str[x]) >=65 and ord(str[x])<=90:
           cntUpper=cntUpper+1
       elif ord(str[x]) >=97 and ord(str[x])<=122:
           cntLower=cntLower+1
   if cntUpper == cntLower:
       return "SameCount"
   else:
    return "Programming"
   return
print(findCount('PyThOn'))  #SameCount
print(findCount('PYTHon'))  #Programming


# In[3]:



# Extract digits from given string
def extractdigits(str):
    for x in range(len(str)):
        if ord(str[x])>=48 and ord(str[x])<=57:
            print(str[x],end=" ")
    return 
extractdigits("appli1cat8ion89")    


# In[4]:




#function to return the sum of the digits
def sumofdigits(str):
    sum=0
    for x in range(len(str)):
        if ord(str[x])>=48 and ord(str[x])<=57:
            sum=sum+(ord(str[x])-48)
    return sum
sumofdigits("appli1cat8ion89")


# In[5]:




def sumofdigits(str):
    sum=0
    for x in range(len(str)):
        if ord(str[x])>=48 and ord(str[x])<=57:
            if (ord(str[x])-48)%2==0:
                sum=sum+(ord(str[x])-48)
                
    return sum
sumofdigits("appli1cat8ion89")


# # Function of the list
# lst1
# print(min(lst1))
# print(max(lst1)) Day objectives
# Python data structures
# Lists
# Tuples
# Dictionaries
# Basic Program sets on data structures
# advanced problem set
# contact application(dictionary object)
# Data structures
# To store ,search and Sort the data
# pyhton data structures
# lists
# It is one of the common data structures supports by python,the list items are separated by comma operator and enclosed in square brackets
# example:
# list1 = [1,6,2,18,9]
# list2 = ["gitam",12,12,15.5,"hyderabad"]
# print(sum(lst1))
# print(sum(lst1)//len(lst1))
# print(sum(lst1[1::2])/len(lst1[1::2]))

# In[7]:


lst = [1,8,16,9,2]
print(lst)
print(lst[0])
print(lst[1])
print(lst[-1])
print(lst[-2])
print(lst[2])
print(lst[1:])


# In[8]:


# Update the list item values using index(Direct referencing)
li = ["Gitam","Python",1989,2002]
print(li)
li[2] = 2019
print(li)


# In[9]:



# basic list opertaions
lst1 = [1,9,6,18,2]
print(len(lst1))
print(lst1*2)
print(len(lst1))
print(9 in lst1)
print(15 in lst1)
for x in range(len(lst1)):
    print(lst1[x],end=' ')


# In[15]:


# check a year is leap year or not
year=int(input("enter a year"))
if year%400== 0 or (year%100 !=0 and year %4 ==0):
    print("leap year")
else:
    print("not leap year")


# In[14]:


# Find the large number from the given numbers
a1=int(input("enter number 1 "))
a2=int(input("enter number 2 "))
a3=int(input("enter number 3 "))
if a1>a2 and a1>a3:
    print(a1,"is the largest number")
elif a2>a1 and a2>a3:
    print(a2,"is the largest number")
elif a3>a1 and a3>a2:
    print(a3,"is the largest number")


# In[16]:



li = [1,9,8,2,6,3]
print(li[-1::-2])


# In[17]:


li = [1,9,8,2,6,3]
print(li[-1:2:-2])


# In[18]:


li = [1,9,8,2,6,3]
print(li[-1:0:-2])


# In[19]:


li = [1,9,8,2,6,3]
print(li[-1:2:-2])


# In[20]:


# Function to find the second large item from the list
# input :   [1,19,6,2,8,18,3]
# output :  18
def secondlarge(li):
   li.sort()
   return li[-2]
def genericlarge(li,n):
   li.sort()
   return li[-n]
li= [1,19,6,2,8,18,3]
genericlarge(li,4)


# # Linear search
# Linear search algorithm can be applied on duplicate and unique list
# Unique list : All items of the list are appeared as only one
# Duplicate list : The items of the list can be appeared more than one
# Linear search algorithm can be applied on sorted list or unsorted list

# In[1]:


# Function to search the data in a list
# Search is found then return the index if not return -1
def linearsearch1(li,taritem):
   for x in range(len(li)):
       if li[x] == taritem:
           return x
       return -1
li = [1,19,6,2,8,18,3]
linearsearch1(li,225)


# In[2]:


# Function
# Input : [1,5,9,6,5,15,1,2,5],key=5 # Duplicate
# Output : 1 4 8
def linearsearch2(li,taritem):
   for x in range(len(li)):
       if li[x] == taritem:
           print(x,end=" ")
   return 

li = [1,5,9,6,5,15,1,2,5]
linearsearch2(li,5)   


# In[3]:


# Function
# i/p : list
#o/p : seq of characters
# Test case
# [1,5,9,6,5,15,1,2,5],tar=5 --!! !!!!! !!!!!!!!!

def linearSearch3(li,tarItem):
   # Implement the logic
   for x in range(len(li)):
       if li[x] == tarItem:
           j=0
           while j!=x+1:
               print("!",end=" ")
               j=j+1
           print(end=" ")
   return
li = [1,5,9,6,5,15,1,2,5]
linearSearch3(li,5)


# In[4]:


# Function
# i/p: List
# o/p: Formatted
# Test case:
# [12,2,45,9,18,15,36] --60
#A list item which is perfectly multiple of 3 and 5

def linearSearch4(li):
   sum=0
   for x in range(len(li)):
       if li[x] %3 ==0 and li[x] % 5==0 :
           sum += li[x] #sum=sum + li[x]
   return sum
li= [12,2,45,9,18,15,36]
linearSearch4(li)


# In[ ]:




