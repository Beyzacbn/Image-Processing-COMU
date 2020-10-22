#!/usr/bin/env python
# coding: utf-8

# In[20]:


import os
os.getcwd()
os.listdir()


# In[21]:


path = os.getcwd() 
jpg_files = [f for f in os.listdir(path) if f.endswith('.jpg')]
jpg_files


# In[23]:


import numpy as np
import matplotlib.pyplot as plt
im_1 = plt.imread(jpg_files[0])


# In[28]:


def get_value_from_triple(temp_1):
    #temp_1 = im_1[0,0,:]
    return int(temp_1[0]/3+ temp_1[1]/3+ temp_1[2]/3)


def get_0_1_from_triple(temp_1):
    #temp_1 = im_1[0,0,:]
    temp = int(temp_1[0]/3+ temp_1[1]/3+ temp_1[2]/3)
    if temp<110:
        return 0
    else:
        return 1


# In[30]:


get_0_1_from_triple(im_1[100,10,:])


# In[31]:


get_value_from_triple(im_1[0,0,:])


# In[32]:


def convert_rgb_to_bw(im_1):    #RGB ( R 0-255 ,G , B), gray(0,.....255), BW(0,1)
    m,n,k = im_1.shape
    new_image = np.zeros((m,n),dtype='uint8')
    for i in range(m):
        for j in range(n):
            s = get_0_1_from_triple(im_1[i,j,:])
            new_image[i,j] = s
    return new_image


def convert_rgb_to_gray(im_1):     #RGB ( R 0-255 ,G , B), gray(0,.....255), BW(0,1)
    m,n,k = im_1.shape
    new_image = np.zeros((m,n),dtype='uint8')
    for i in range(m):
        for j in range(n):
            s = get_value_from_triple(im_1[i,j,:])
            new_image[i,j] = s
    return new_image


# In[33]:


im_1_bw = convert_rgb_to_bw(im_1)


# In[34]:


im_1_gray = convert_rgb_to_gray(im_1)


# In[35]:


plt.subplot(1,3,1)
plt.imshow(im_1)
plt.subplot(1,3,2)
plt.imshow(im_1_gray,cmap='gray')
plt.subplot(1,3,3)
plt.imshow(im_1_bw,cmap="gray")
plt.show()


# In[40]:


plt.imsave('istanbul_gray.jpg',im_1_gray,cmap='gray')


# In[39]:


plt.imsave('istanbul_bw.jpg',im_1_bw,cmap='gray')


# In[ ]:




