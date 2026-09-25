#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


# 5 game-specific functions
from breakthrough import *


# In[3]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)

random_agent=Agent(random_move)


# In[4]:


def human_move(state,player):

    moves=valid_moves(state,player)
    print("Locations:")
    state.show_locations()

    print( "Player ", player)
    print("Moves:")
    for i, move in enumerate(moves):
        print(f"\t{i}: {move}")

    valid_move=False
    while not valid_move:
        move_number=int(input('Which move do you want (enter a number)?'))

        if move_number in range(len(moves)):
            valid_move=True
        else:
            print( "Illegal move.")


    return moves[move_number]


human_agent=Agent(human_move)


# In[27]:


from Game.minimax import *


# In[28]:


def minimax_move(state,player,info):

    try:
        display=info.display
    except KeyError:
        display=True

    T=info.T

    if not state in T:
        values,moves=minimax_values(state,player,display=display)
        move=top_choice(moves,values)
        T[state]=move
    else:    
        move=T[state]

    return move


minimax_agent=Agent(minimax_move)
minimax_agent.T=Table()


# In[7]:


g=Game(N=4)
g.run(random_agent,random_agent)


# In[8]:


g=Game(N=4)
g.run(random_agent,minimax_agent)


# In[22]:


g=Game(N=4)
g.number_of_games=100
g.display=False
g.save_states=True
result=g.run(random_agent,random_agent)
print(result)
print([i for i in range(100) if result[i]==2])


# In[23]:


g.games[2]['states']


# In[25]:


state=g.games[2]['states'][-2]
state


# In[26]:


state.board


# In[10]:


g=Game(N=4)
g.number_of_games=100
g.display=False
minimax_agent.display=False
result=g.run(random_agent,minimax_agent)
print(result)


# In[11]:


g=Game(N=4)
g.number_of_games=100
g.display=False
minimax_agent.display=False
result=g.run(minimax_agent,random_agent)
print(result)


# In[15]:


g=Game(N=4)
g.number_of_games=100
g.display=False
g.save_states=True
minimax_agent.display=False
result=g.run(minimax_agent,minimax_agent)
print(result)


# In[16]:


len(g.games)


# In[17]:


D=g.games[0]
D


# In[12]:


g=Game(N=5)
g.number_of_games=10
g.display=False
minimax_agent.display=True
result=g.run(minimax_agent,minimax_agent)
print(result)


# In[14]:


get_ipython().run_line_magic('pinfo', 'g.save_states')


# In[ ]:




