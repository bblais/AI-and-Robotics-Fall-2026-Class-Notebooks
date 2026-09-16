#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


state=Board(6,6)
state.show_locations()


# In[5]:


state[19]=1
state[14]=2
state


# In[4]:


def update_state(state,player,move):
    new_state=state
    start,end=move
    mid=(start+end)//2

    state[start]=0
    state[end]=player
    state[mid]=0

    return new_state


# In[6]:


update_state(state,1,[19,9])


# In[ ]:




