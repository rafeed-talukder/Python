
# coding: utf-8

# In[1]:


1+1


# In[2]:


print('1+1')


# In[3]:


print (1+1)


# In[4]:


x=6
print(x)


# In[5]:


s=x+4


# In[6]:


print('s')


# In[7]:


print(s)


# In[8]:


num=30 
name ='rafid'
print ("my name is {}, age is {}".format(num,name))


# In[9]:


num=30
name="juda"

print ("my name is {m},age is {n}".format(m=name,n=num))


# In[10]:


#string------------------------------------------------------

r='abcdefghijklmnopqr'
r[:4]


# In[11]:



from __future__ import print_function

'he1'
'he2'
print('h\t1')
print('h2')


# In[12]:


#listttttttttttttttttttttttttttttttttttttttttt
s=[1,2,3,4,]
s


# In[13]:


print(s)


# In[14]:


s2={1,2,3,4}
s2


# In[15]:


print(s2)


# In[16]:


s3=(1,2,3,4)
print(s3)


# In[16]:


#always use []--------------------------------

lista=['a','b','c']
lista.append('d')


# In[17]:


print(lista)


# In[18]:


s4=[1,2,3]
s4.append(4)


# In[19]:


print(s4)


# In[20]:


lista[:4]


# In[21]:


lista[2]


# In[22]:


lista[1]


# In[23]:


lista[2]


# In[25]:


lista[3]


# In[24]:


lista[0:3]


# In[27]:


listb=[1,2,3,[10,11,12,14,['rafieed','tusher','rahat']]]
print(listb[3][1])


# In[28]:


print(listb[3][4][1])


# In[ ]:





# In[29]:


3/2


# In[30]:


from __future__ import division


# In[31]:


3/2


# In[32]:


a='hello world'


# In[33]:


print(a)


# In[34]:


len(a)


# In[35]:


a[0]


# In[36]:


a[0:3]


# In[37]:


a[1]


# In[38]:


a[-1]


# In[39]:


a[10:]


# In[40]:


a[5]


# In[41]:


a[:-6]


# In[42]:


a[::-2]


# In[43]:


a


# In[44]:


cb= a+ ' with me'


# In[45]:


cb


# In[46]:


a


# In[47]:


b=a + ' rfid'


# In[48]:


b


# In[49]:


a.capitalize()


# In[50]:


a.casefold()


# In[51]:


a.index('o')


# In[52]:


'this is first string %1.2f' %(1.98766)


# In[53]:


print('this is first string %s' %(a))


# In[98]:


print ('using {} we can {}'.format('format1','write'))


# In[99]:


print('first : %s, second :%r, trird %s ' %('a','b','c'))


# In[100]:


list_1=[1,2,3,4,5,6,7,8,9]


# In[101]:


list_1


# In[102]:


list_1=list_1 + ['ami']


# In[103]:


list_1


# In[104]:


list_1


# In[105]:


list_1.append('tumi')


# In[106]:


list_1


# In[107]:


a=[1,2,3,4]


# In[108]:


a


# In[109]:


a[1:3]


# In[110]:


list_1.reverse()


# In[111]:


list_1


# In[112]:


list_2=[1,2,3,4,['ami','tumi','rafeed',[22,33,44,[55,66,77]]]]


# In[113]:


list_2


# In[114]:


list_2[4][3][3][2]


# In[115]:


lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]


# In[116]:


matrix=[lst_1,lst_2,lst_3]


# In[117]:


matrix


# In[118]:


matrix[1][2]


# In[119]:


my_dict1 = {'key1':'value1','key2':'value2'}


# In[120]:


print(my_dict1)


# In[121]:


dict2=1
dict1=2


# In[122]:


my_dict2={1 : dict1 ,2:dict2}


# In[123]:


my_dict2


# In[124]:


my_dict = {'key1':123,1:[12,23,33],'key3':['item0','item1','item2']}


# In[125]:


my_dict[1][2]


# In[126]:


my_dict.keys()


# In[127]:


my_dict['key1'] = -123
my_dict['key1']


# In[128]:


my_dict={}
my_dict['key1'] = 123
my_dict['key2'] = [12,23,33]


# In[129]:


my_dict['key2'][2]


# In[130]:


t = (1,2,3)


# In[131]:


t


# In[132]:


t


# In[133]:


pwd


# In[134]:


get_ipython().run_cell_magic('writefile', 'test.txt', 'hello i am hare')


# In[135]:


f=open('test.txt')


# In[136]:


f.read()


# In[137]:


f1=open( 'a.txt' )


# In[138]:


pwd


# In[139]:


f1.read()


# In[141]:


get_ipython().run_cell_magic('writefile', 'test1.txt', 'hi i am rafeed')


# In[142]:


f2=open('test1.txt')


# In[143]:


f2.read()


# In[144]:


f2.read()


# In[145]:


f2.seek(0)


# In[146]:


f2.read()


# In[147]:


f2.read()


# In[148]:


f2.seek(1)


# In[149]:


f2.read()


# In[151]:


f2.seek(2)


# In[152]:


f2.read()


# In[153]:


f2.read()


# In[154]:


f2.readable()


# In[155]:


f2.readline()


# In[156]:


f2.readlines()


# In[157]:


f2.seek(0)


# In[158]:


f2.readlines


# In[159]:


f2.readline()


# In[160]:


f2.readlines()


# In[161]:


f2.seek(0)


# In[163]:


f2.readlines()


# In[164]:


f2.seek(0)


# In[29]:


get_ipython().run_cell_magic('writefile', 'text2.txt', 'i am here\ni am there\ni do ')


# In[7]:



             # mock text----------


l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

l_one[2][0] <= l_two[2]['k1']


# In[23]:


w= [1,2,[3,4,'hello']]


# In[24]:


w


# In[26]:


w[2][2]


# In[27]:


w[2][2]='goodbye'


# In[28]:


w


# In[14]:


s='rafid a bbb ggg'
print(s.split('rafid'))


# In[13]:


a='http://localhost:8888/notebooks/practice%201/Files.ipynb'
print(a.split('http://'))

