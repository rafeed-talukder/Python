
# coding: utf-8

# Write a function that computes the volume of a sphere given its radius.

# In[ ]:


def find_volume (r):
    x=(4/3)*(3.1416)*(r*3)
    print( 'output', x)
    
find_volume(5)   


# Write a function that checks whether a number is in a given range (Inclusive of high and low)

# In[ ]:


def num_check(n,low,high):
    for num in range(low,high+1):
        if n == num:
            
            print("Yes this: %s" %n,"is in range", "number is:", n) 
            break
    else:
        print("Sorry this: %s" %n,"is not in range", "number is:", n)
        return n 
    
num_check(4,1,4) 


# In[ ]:


s='Hello Mr. Rogers, how are you this fine Tuesday?'
v=s.split()
 


# In[ ]:


def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print( "Original String : ", s)
    print ("No. of Upper case characters : ", d["upper"])
    print ("No. of Lower case Characters : ", d["lower"])
up_low(s)    
s={'Hello Mr. Rogers, how are you this fine Tuesday?'}


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# 
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# In[ ]:


S=[1,1,1,1,2,2,3,3,3,3,4,5]
set(S)


# In[ ]:


#how??
S=[1,1,1,1,2,2,3,3,3,3,4,5]
def check_number ():
    global S
    v=S.set()
    print(v)
    
check_number() 


# In[ ]:


S=[1,1,1,1,2,2,3,3,3,3,4,5]
def check_number ():
    global S
    a=[]
    for n in S:
        if n not in a:
            a.append(n)     
    return a

    print(a)
              
check_number ()


# Write a Python function to multiply all the numbers in a list.

# In[ ]:


def mul (num):
    m=1
    for n in num:
        m=n*m
    return m
mul([1,2,3,-4]) # list akare dhukate hobe vitore


# Write a Python function that checks whether a passed string is palindrome or not.

# In[ ]:


def v (s):
    if (s == s[::-1]):
        print('this is  palindrome',s)
    else:
        print('this is not palindrome',s)
v('ab') 

