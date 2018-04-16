
# coding: utf-8

# # class
# 

# Structure of Class making
# 

# In[19]:


#Attribute diclare in a Special methods

class Name(object):
    
    def __init__(self,n):
        self.n=n
name1=Name(n='Tanjilur')
name2=Name(n='Talukder')  


# In[21]:


print(name1.n,name2.n)


# In[29]:


#Attribute diclare in class and methods and use it in a special methods variable

class Name(object):
    new='rafeed'
    
    def __init__(self,n):
        self.n=n
name1=Name(n='Tanjilur')
name2=Name(n='Talukder')
print(name1.new ,name2.n)


# # Methods

# Calculate AREA of a Circle using class & Methods

# (pi*r^2)

# In[28]:


class Circle (object):
    
    pi=3.14
    
    def __init__(self,radius=1):
        self.radius=radius
     
    def area (self):                                # calculate area   
        return (self.radius**2)*Circle.pi
    
    def set_radius (self,n_rad):                    #set a new radius value 
        self.radius=n_rad
        
    def get_radius(self):                           #pop the presint value of input radius
        return self.radius
    
       
        
c=Circle(radius=2)
print( 'old redius is', c.radius)


c.set_radius(12)
print( 'after new set radius is', c.radius)

print('Area is',c.area())

print('radius is',c.get_radius())


# CALCULATE SALARY

# In[65]:


class Selary(object):
    count_emp=0
    
    def __init__(self,name,selary):
        self.name=name
        self.selary=selary
        
        Selary.count_emp+=1
    
    def display_employ(self):
        print("Name : ", self.name,  ", Salary: ", self.selary)
    
emp1 = Selary("Zara", 2000)
"This would create second object of Employee class"

emp2 = Selary("Manni", 5000)

emp1.display_employ()
emp2.display_employ()

print ("Total Employee", Selary.count_emp)
    
        


# # INHERITANCE

# "Inheritance is a powerful feature in object oriented programming. It refers to defining a new class with little or no modification to an existing class. The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class."

# In[81]:


# parent class 
class First(object):
    def __init__ (self,name,job):
        self.name=name
        self.job=job
        
    def showname(self):
        print('Name is',self.name)
        
    def showjob(self):
        print('Job name is', self.job)
        
        
# child class


class Child(First):
    language=""
    
    def setlanguage(self,language):
        self.language=language
        
    def printlanguage(self):
        print('Language is',self.language)
        
show1=Child('rafeed','Developer')   
show1.setlanguage('Python')
show1.showname()
show1.showjob()
show1.printlanguage()


# In[7]:


class Animal (object):
    def __init__(self):
        print('dog1 kutta')
        
    def fst (self):
        print('dog2')
        
    def second (self):
        print('dog3')
        
class N_nimal (Animal):
    
    
    def fst (self):
        Animal.__init__(self)
        
        print('hhhh')
        
    def gg (self):
        print('jjjjj')
c= N_nimal () 
c=Animal()
c.fst()
c.second()


# # Special Methods

# The __init__(), __str__(), __len__() and the __del__() methods.

# In[11]:


#Basic code

class Sm (object):
    def __init__(self,tittle,author,pages):
        
        self.tittle=tittle
        self.author=author
        self.pages=pages
        
        print('book is created')
        
v=Sm('python','rafid',34)        


# In[16]:



class Sm (object):
    def __init__(self,tittle,author,pages):
        
        self.tittle=tittle
        self.author=author
        self.pages=pages
        
        print('book is created')
        
    def __str__(self):
        return ('tittle:%s ,author: %s, pages: %s'  % (self.tittle,self.author,self.pages) )
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print ("done")
        
v=Sm('python','rafid',34)  
print(v)
print(len(v))
del(v)

