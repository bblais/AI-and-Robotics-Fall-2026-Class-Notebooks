#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[3]:


def initial_state():
    state=Board(3,3)
    for i in range(3):
        state[i]=1

    for i in range(6,9):
        state[i]=2

    return state    


# In[4]:


state=initial_state()
state


# In[11]:


player=2

if player==1:
    print(state)

else:
    s=""
    rows=list(reversed(list(state.rows())))
    for row in rows:
        for val in row:
            if not state.pieces is None:
                val=state.pieces[val]
                s+="%2s " % (val)
            else:
                s+="%2d " % (val)
        s+="\n"
    print(s)


# In[12]:


loc=Board(*state.shape)
loc.board=list(range(prod(state.shape)))

if player==1:
    print(loc)

else:
    s=""
    rows=list(reversed(list(loc.rows())))
    for row in rows:
        for val in row:
            if not state.pieces is None:
                val=state.pieces[val]
                s+="%2s " % (val)
            else:
                s+="%2d " % (val)
        s+="\n"
    print(s)


# In[13]:


state=initial_state()
state


# In[ ]:


num_rows=3
num_cols=3

def row_from_index(idx):
    return idx%num_cols

def col_from_index(idx):
    return idx//num_cols

def index_from_row_col(row,col):
    return row*num_cols+col

def diagonal_locations(loc):

    r=row_from_index(loc)
    c=col_from_index(loc)

    locations=[]

    if r>0 and c>0:  # upper left
        r2=r-1
        c2=c-1
        locations.append(index_from_row_col(r2,c2))



