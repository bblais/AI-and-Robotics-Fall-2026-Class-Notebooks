#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mplturtle import *


# In[2]:


reset()
forward(50)
right(45)
forward(100)


# # Draw a square

# In[3]:


reset()

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)



# In[4]:


reset()

forward(50)
right(90)

forward(50)
right(90)

pencolor("red")

forward(50)
right(90)

forward(50)
right(90)



# In[5]:


reset()

forward(60)
right(90)

forward(60)
right(90)

pencolor("red")

forward(50)
right(90)

forward(60)
right(90)



# In[9]:


reset()

size=60

forward(size)
right(90)

forward(size)
right(90)

forward(size)
right(90)

forward(size)
right(90)

size=120

forward(size)
right(90)

forward(size)
right(90)

forward(size)
right(90)

forward(size)
right(90)


# ## loop

# In[13]:


reset()
size=60

print("here")

for i in range(4):
    forward(size)
    right(90)
    print("i is ",i)

print("there")


# In[17]:


reset()
size=60

print("here")

for i in range(4):
    forward(size)

right(90)
print("i is ",i)

print("there")

forward(100)


# # Functions

# In[19]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)
        print("i is ",i)


# In[20]:


reset()
print("here")
square(80)
print("there")


# In[21]:


reset()
print("here")
square(20)
forward(60)
square(20)
print("there")


# In[22]:


reset()
print("here")
square(20)

penup()
forward(60)
pendown()

square(20)
print("there")


# In[23]:


def penup_forward(length):
    penup()
    forward(length)
    pendown()


# In[25]:


reset()
square(20)

penup_forward(60)

square(20)


# In[ ]:




