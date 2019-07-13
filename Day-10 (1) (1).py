#!/usr/bin/env python
# coding: utf-8

# ### Standard Libraries
# - File I/O
# - Regular Expression
# - Datetime
# - Math (numerical and Mathematical)

# ### File Handling in Python
# - File:= Document containing information on the Permanent storage
# - Different types of files :- txt,doc,pdf,csv and ect...
# - Input -- Keyboard
# - Output -- File
# ### Modes of the File I/O
# - "w" -- This mode is used to file writing
#       -- if the file is not present first it creates the file and write so me data to it 

# In[1]:


# Function to Create a file and write to the file
def createFile(filename):
    f=open(filename,"w")
    for i in range(10):
        f.write("This is %d Line\n"%i)
    print("File is created and data has written")    
    return
createFile("File1.txt")


# In[2]:


ls


# In[1]:


def createFile(filename):
    f=open(filename,"w")
    print("Testing")
    print("File is created and data has written")    
    return
createFile("File1.txt")


# In[2]:


def appendData(filename):
   f=open(filename,'a')
   for i in range(10):
       f.write("this is %d line\n"%i)
   print("file created and succesfully data written")
   return
appendData('file2.txt')


# In[3]:


def appendData(filename):
   f=open(filename,'a')
   f.write("new line 1\n")
   f.write("new line 2\n")
   print("file created and succesfully data written")
   return
appendData('file2.txt')


# In[8]:


#functin to read of the file

def readFileData(filename):
   f=open(filename,'r')
   if f.mode=='r':
       x=f.read()
       print(x)
   f.close   
   return
readFileData('file2.txt')


# In[13]:


# function to read the file

def fileOperations(filename,mode):
   with open(filename,mode) as f:
       if f.mode=='r':
           data=f.read()
           print(data)
       elif f.mode=='a':
           f.write('data of the file')
           print('the data succesfully written')
   f.close
   return
filename=input('enter the file name ')
mode=input('enter the mode of the file ')
fileOperations(filename,mode)


# In[ ]:




