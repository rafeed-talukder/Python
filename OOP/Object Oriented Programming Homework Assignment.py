
# coding: utf-8

# # Calculate Volume & Surface Area of a cylinder

# Basic Formula

# In[1]:


class Cylinder(object):
    
    def __init__(self,height=1,radius=1):
        pass
        
    def volume(self):
        pass
    
    def surface_area(self):
        pass


# Mathmaticaly Prove

# In[5]:


class Cylinder(object):
    pi=3.14
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        b=(Cylinder.pi* (self.radius*self.radius) *self.height )
        print(b)
    
    def surface_area(self):
        new=Cylinder.pi* (self.radius*self.radius) *self.height
        return 2*Cylinder.pi*self.radius*self.height + new
    
c= Cylinder(2,3) 


# In[6]:


c.volume()


# In[7]:


c.surface_area()


# In[ ]:


class Cylinder(object):
    pi=3.14
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        return (Cylinder.pi* (self.radius*self.radius) *self.height )
    
    #def surface_area(self):
        #new=Cylinder.pi* (self.radius*self.radius) *self.height
        #return 2*Cylinder.pi*self.radius*self.height + new
class New(Cylinder):
    def __init__(self):
        
c= Cylinder(2,3)   

