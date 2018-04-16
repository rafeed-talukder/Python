
# coding: utf-8

# In[1]:


x = 25

def printer(x):
    x = 50
    return x
print (printer(x))
print (x)




# In[29]:


c=40
def v (c):
    c=30
    print(c/2)   
    return c
print(v(c))
print(c)


# In[38]:


# local variable
x=5
def v (x):
    x=4
    return x

print(x)
print(v(x))


# In[51]:


# global variable
x=5
def v ():
    x=4
    b=3
    c=x+b
    return c
v()
print(v())
print(x)


# In[37]:


v=('rafeed')
v[1:3]


# In[62]:


x = 50

def func():
    
    print ('This function is now using the global x!')
    global x
    print ('Because of global x is: ', x)
    x = 2
    print ('Ran func(), changed global x to', x)
    return 0

print ('Before calling func(), x is: ', x)
func()
print ( 'Value of x (outside of func()) is: ', x)


# In[123]:


x = {10}
su1=su=0
def sum1 ():
    
    global su,x,su1
    print('global variable sum')
    
    for n in x:
        su1=su1+n
       # print(su1)
    print(su1)
    
    print("total sum in to function")
    x=range(10)
    for n in x:
        su=su+n
        #print(su)
    return su1,su
         
sum1()
print(su)

