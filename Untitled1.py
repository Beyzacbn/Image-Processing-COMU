#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import numpy as np
import matplotlib.pyplot as plt


# In[32]:


def compare_list_ndarray():
    #https://docs.python.org/3/library/ctypes.html
    #numpy as np
    list_1=[1,"2dfghjk,3",'4',5,6]  #broadcast
    list_2=[2,"2xcvbnmö,3",'1113',15,26]  #broadcast
    
    print(list_1 + list_2)
    
    list_1=[1,2,3,4] #broadcast
    list_2=[1,2,3,4] #"2xcvbnmö,3",'1113',15,26]  #broadcast
    list_1+list_2+[10]  #list1+list2+10  error
    print(list_1+list_2+[10])  
    
    list_3=np.asarray([1,2,3,4])
    list_4=np.asarray([1,2,3,4])
    print(list_3+list_4+10)
    

def get_jpeg_files():
    os.getcwd()
    os.listdir()
    path=os.getcwd()
    jpg_files = [f for f in os.listdir(path) if f.endswith('.jpg')]
    return jpg_files

compare_list_ndarray()
get_jpeg_files()


    


# In[23]:


def display_two_image(im_1,im_2):
    plt.subplot(1,2,1)
    plt.imshow(image_1)
    
    plt.subplot(1,2,2)
    plt.imshow(image_2+30)
    
    plt.show()


def rotate(im_1):
    m,n,k=im_1.shape
    
    new_image=np.zeros((n,m,k),dtype='uint8')
    
    for i in range(m):
        for j in range(n):
            temp=image_1[i,j]
            new_image[j,i]=temp
    
    return new_image


# In[24]:


image_1=plt.imread('istanbul.jpg')
image_2=rotate(image_1)
display_two_image(image_1,image_2)


# In[ ]:




