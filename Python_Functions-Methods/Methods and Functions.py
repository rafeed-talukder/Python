
# coding: utf-8

# # methods
# 

# In[ ]:


# help(l.count)


# In[19]:





# In[20]:


l


# # functions

# In[23]:


def a (n1,n2):
    return n1
a(1,2)   


# In[95]:


def sum_function (n1,n2):
    #return n1+n2
    '''
      this is sum function
      
    '''
    print (n1+n2)
    
sum_function(2,2)


# In[94]:


def num (nam):
    print ("hello bro ", nam)
    
num('rafeed')    


# In[64]:


def prime (num):
    for n in range(2,num):
        if num % n == 0:
            print('not')
            break
        else:
            return("ok")
            break


# In[68]:


prime(4)


# 
# 

# In[41]:


num =13
for n in range(2,num):
    if num % n == 0:
        print ("not")
        break
        
    else:
        print ("ok")
        break


# In[99]:



def su (a):
    for n in range (a):
        print(n)


# In[100]:


su(4)


# In[125]:


su=0
def s (c):
    for n in range(c):
        su=c*n
        print(su)
s(10)        


# In[140]:


# Nested Statements and Scope 
c=40
def v (c):
    c=30
    print(c/2)   
    return c
print(v(c))
print(c)

