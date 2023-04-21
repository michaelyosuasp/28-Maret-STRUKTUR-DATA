#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


# In[12]:


twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)


# In[14]:


newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
print(newTwoDArray)


# In[15]:


print(len(twoDArray))


# In[18]:


newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)


# In[19]:


print(len(newTwoDArray))


# In[20]:


print(len(newTwoDArray[0]))


# In[24]:


def  accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])


# In[28]:


accessElements(newTwoDArray, 1, 2)


# In[32]:


def traverseTDArray(array):
    for i in range(len(array)):
        for j in range (len(array[0])):
            print(array[i][j])


# In[33]:


traverseTDArray(twoDArray)


# In[41]:


def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
        return 'The element no found'


# In[42]:


print(twoDArray)


# In[43]:


print(searchTDArray(twoDArray, 8))


# In[44]:


newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)


# In[45]:


shoppingList = ['Milk', 'Cheese', 'Butter']


# In[46]:


for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])
    empty = []
    for i in empty:
        print("I am empty")


# In[53]:


myList = [1,2,3,4,5,6,7]
print(myList)


# In[54]:


myList.insert(4,15)
print(myList)


# In[55]:


myList.append(55)
print(myList)


# In[56]:


newList = [11,12,13,14]
myList.extend(newList)
print(myList)


# In[58]:


myList.insert(4,15)

myList.append(55)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)


# In[62]:


myList = [10,20,30,40,50,60,70,80,90]

def searchList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
        return 'The value does not exist in the list'
print(search(myList, 100))


# In[ ]:


total = 0
count = 0
while (True):
 inp = input('Enter a number: ')
if inp =='done': break
    value = float(inp)
    numlist

