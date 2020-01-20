
# coding: utf-8

# In[ ]:


D = {'Composer': 'Brahms', 'period': 'Romantic', 'Symphony': 1}


# In[ ]:


D['Composer']


# In[ ]:


D['Symphony'] += 3
D


# In[ ]:


D = {}
D['Composer'] = 'Beethoven'
D['Period'] = 'Classic'
D['Symphony'] = 9
 
D


# In[ ]:


print (D['Composer'])


# In[ ]:


D = {'Composer': {'first': 'Johannes', 'last' : 'Brahms'},
         'Period': 'Romantic',
         'Piece' : ['Piano Concerto No. 1', 'Piano Concerto No. 2',
            'Symphony No. 1', 'Symphony No. 2',
            'Violin Concerto in D Major',
            'Hungarian Dances'] }
D
D['Composer']


# In[ ]:


D['Composer']['last']


# In[ ]:


D['Piece']


# In[ ]:


D['Piece'][-1]


# In[ ]:


D = {'a': 97, 'b': 98, 'c': 99}
D


# In[ ]:


for k in sorted(D):
    print (k, '=>', D[k])


# In[ ]:


odd = [1, 3, 5]

# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])

#Output: ["re", "re", "re"]
print(["re"] * 3)

