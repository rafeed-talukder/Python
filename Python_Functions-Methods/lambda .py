
# coding: utf-8

# # lambda
# 

# In[ ]:


# addition 
c=lambda n : n+1


# In[4]:


c(2)


# In[28]:


# grabe the first value using append
v=[]
c = lambda n:n[0]
v.append(c('rafeed')) 
v.


# In[36]:


# find even numbers
b=lambda n : n % 2 == 0
b(4)
print('even')


# In[42]:


# riverse string
v=[]
c = lambda n:n[::-1]
v.append(c('rafeed')) 
v


# In[44]:


# addition
b=lambda n,m : n+m
b(1,2)


# In[45]:


# find even numbers
b=lambda n: 'even' if n%2 == 0 else 'odd'


# In[46]:


b(4)

map()
filter()
reduce()
# In[67]:


b= lambda n : len(n)


# In[69]:


b('rfd')

