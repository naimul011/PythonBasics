
# coding: utf-8

# In[1]:


mystring = "The quick brown fox." 
print(len(mystring)) 
print(type(mystring))


# In[2]:


stringlist = mystring.split()
stringlist


# In[6]:


mystring2 = "Thequickbrownfox." 
stringlist2 = mystring2.split()
print(stringlist2)
type(stringlist2)


# In[8]:


str = 'hello world'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])


# In[9]:


str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)


# In[10]:


count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')


# In[11]:


str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))

