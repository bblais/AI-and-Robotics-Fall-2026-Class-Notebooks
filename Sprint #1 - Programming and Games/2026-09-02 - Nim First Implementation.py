#!/usr/bin/env python
# coding: utf-8

# # Nim (21 Sticks Variant)
# 
# ## Setup
# - Start with **21 sticks** (or counters, stones, matches, etc.).  
# - Two players take turns.  
# 
# ---
# 
# ## Rules
# 1. On your turn, you must take **1, 2, or 3 sticks** from the pile.  
# 2. Players alternate turns.  
# 3. **The player forced to take the last stick loses.**  
# 
# ---
# 
# ## Example Play
# - Start: 21 sticks.  
# - Player A takes 2 → 19 left.  
# - Player B takes 3 → 16 left.  
# - Player A takes 1 → 15 left.  
# - … and so on, until one player is forced to take the last stick and loses.  
# 
# 

# In[1]:


from Game import *


# # Game functions

# In[2]:


def initial_state():
    return 21


# In[3]:


def show_state(state,player):
    # show the current state
    print("Player",player)
    print("Number of sticks is:",state)


# In[4]:


show_state(16,2)


# - if the state is, say, 16 the valid moves [1,2,3]
# - if state is 2 the valid moves: [1,2]

# In[5]:


def valid_moves(state,player):
    # return a **list** of moves that are valid
    if state==1:
        return [1]
    elif state==2:
        return [1,2]
    else:
        return [1,2,3]


# In[6]:


valid_moves(16,1)


# In[7]:


valid_moves(2,1)


# In[8]:


valid_moves(1,1)


# In[9]:


valid_moves(0,1)


# In[10]:


valid_moves(-5,1)


# In[11]:


def update_state(state,player,move):
    # return the new state after the move
    new_state=state-move
    return new_state


# In[12]:


update_state(16,1,3)


# In[13]:


update_state(16,1,15)


# In[14]:


def win_status(state,player):
    # called after update_state
    # returns "win" if this new state is a win for this player
    # returns "lose" if this new state is a loss for this player
    # returns "stalemate" if this new state is a tie for this player
    # return None if this is a mid-game state

    if player==1:
        other_player=2
    else:
        other_player=1

    if state==0:
        return "lose"
    else:
        return None


# In[15]:


win_status(0,2)


# # Agents

# In[16]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)

random_agent=Agent(random_move)


# In[17]:


def human_move(state,player):
    moves=valid_moves(state,player)
    print("Valid moves are: ",moves)
    move=int(input("Enter your move:"))
    while move not in moves:
        print("Invalid move...try again")
        move=int(input("Enter your move:"))

    return move

human_agent=Agent(human_move)    


# In[18]:


human_move(16,2)


# In[31]:


human_move(2,2)


# # Running the Game

# In[19]:


g=Game()
g.run(random_agent,random_agent)


# In[20]:


def lower_move(state,player):
    moves=valid_moves(state,player)
    moves=sorted(moves)

    new_moves=[]
    count=10
    for move in moves:
        new_moves.extend([move]*count)
        count-=3
        if count<=0:
            count=1

    print(moves)
    print(new_moves)

    return random.choice(new_moves)

lower_move(21,1)


# In[ ]:




