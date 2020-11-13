#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()
os.listdir()


# In[2]:


path=r"C:\Users\Beyza"
file_name_with_path=path+"\Cameraman.jpg"


# In[3]:


file_name_with_path


# In[4]:


import matplotlib.pyplot as plt
import numpy as np


# In[6]:


def convert_rgb_to_gray_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[0]
    im_2=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            im_2[i,j]=get_distance(im_1[i,j,:])
    return im_2

def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    d=((a**2)*w1 +
    (b**2)*w2+
    (c**2)*w3)**.5
    return d


# In[16]:


img_0=plt.imread(file_name_with_path) 
get_ipython().run_line_magic('matplotlib', 'inline')
plt.imshow(img_0) 
plt.show()


# In[17]:


img_0.ndim,img_0.shape


# In[18]:


img_1.ndim,img_1.shape


# In[19]:


np.min(img_2),np.max(img_2)


# In[20]:


def my_f_1(a,b):
    assert a>=0; "intensity pozitive", "error intensity not positive"
    if(a<=255-b):
        return a+b
    else:
        return 255


# In[21]:


img_0+10


# In[22]:


img_1=convert_rgb_to_gray_level(img_0)
plt.imshow(img_1,cmap='gray')
plt.show()


# In[23]:


m,n=img_1.shape
img_2=np.zeros((m,n),dtype="uint8")


# In[25]:


def my_f_2(a):
    return int(255-a)
my_f_2(243)


# In[26]:


for i in range(m):
    for j in range(n):
        
        ### increment=50
        ### print(intensity)
        intensity=img_1[i,j]
        img_2[i,j]=my_f_2(intensity)


# In[27]:


plt.imshow(img_2,cmap='gray')
plt.show()


# In[28]:


plt.subplot(2,2,1),plt.imshow(img_0,cmap='gray')
plt.subplot(2,2,2),plt.imshow(img_1,cmap='gray')
plt.subplot(2,2,3),plt.imshow(img_2,cmap='gray')
plt.show()


# In[29]:


x=np.array(list(range(100)))
#y=np.array(list(range(100)))
#y=np.sin(np.array(list(range(100))))
#y=1/(1+np.exp(x))
y1=np.power(x/float(np.max(x)),1)
y2=np.power(x/float(np.max(x)),10)
y3=np.power(x/float(np.max(x)),1/10)


plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)


# In[30]:


x=img_0
img_100=np.power(x/float(np.max(x)),10)
plt.imshow(img_100)
plt.show()


# In[ ]:




