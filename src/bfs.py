#!/usr/bin/env python
# coding: utf-8

# In[85]:


# R:0 ,L:1, D:2,U:3 

from copy import deepcopy
from queue import Queue
import os
import time


ACTION_LIST = ['R', 'L', 'D', 'U']



    
    
def isgoal(state):
    goal_state=[[0,1,2],[3,4,5],[6,7,8]]
    if state == goal_state:
        return True
    else:
        return False
    
    

def state_to_string(var1):
    str2=""
    for i in var1:
        for j in i:
            str2+=str(j)
            
    return str2   


def string_to_state(str3):
    state=[]
    index = 0
    for i in range(3):
        state.append([])
        for j in range(3):
            state[i].append(int(str3[index]))
            index += 1
    return state        
            
                
    
    


      
def actions(initial_state):    
    
    c=[x for y in initial_state for x in y]
    elezero = c.index(0)
    div= elezero//3
    mod= elezero%3
    z=(div,mod)
    # print(z)
    n,m=deepcopy(z)
    if div==0 and mod==0:
        check_list = [1, 3]
        #right()
        #down()
    elif div==0 and mod==1:
        check_list = [0,1,3]
        #left()
        #right()
        #down()
    elif div==0 and mod==2:    
        check_list = [0,3]
        #left()
        #down()
    elif div==1 and mod==0:
        check_list = [1,2,3]
        #up()
        #right()
        #down()
    elif div==1 and mod==1:
        check_list = [0,1,2,3]
        #left()
        #right()
        #up()
        #down()
    elif div==1 and mod==2:
        check_list = [0,2,3]
        #up()
        #left()
        #down()
    elif div==2 and mod==0:
        check_list = [1,2]
        #up()
        #right()
    elif div==2 and mod==1:
        check_list = [0,1,2]
        #left()
        #up()
        #right()
    elif div==2 and mod==2:    
        check_list = [0,2]
        #up()
        #left()
    return check_list
    
def swap(initial_state, action):
    c=[x for y in initial_state for x in y]
    elezero = c.index(0)
    div= elezero//3
    mod= elezero%3
    z=(div,mod)
    # print(z)
    n,m=z
    initial_state = deepcopy(initial_state)
        
    if action==0:
        initial_state[n][m], initial_state[n][m-1]=initial_state[n][m-1], initial_state[n][m]    
    elif action==1:
        initial_state[n][m], initial_state[n][m+1]=initial_state[n][m+1], initial_state[n][m]
    elif action==2:
        initial_state[n][m], initial_state[n-1][m]=initial_state[n-1][m], initial_state[n][m]
    elif action==3:
        initial_state[n][m], initial_state[n+1][m]=initial_state[n+1][m], initial_state[n][m]
    return initial_state
    

    
class Node:
    def __init__(self, current, parent, p_action):
        self.current=current
        self.parent=parent
        self.p_action = p_action


def bfs(init_state):
    queue=Queue()
    initial_node=Node(state_to_string(init_state), None, None)
    queue.put(initial_node)
    visited={}
    visited.update({initial_node.current: initial_node})
    
    while True:
        curnode=queue.get()
        current=string_to_state(curnode.current)
        if isgoal(current):
            break
        for check_list in actions(current):
            newstate=state_to_string(swap(current, check_list))
            if not(newstate in visited):
                node=Node(newstate, curnode, check_list)
                queue.put(node)
                visited.update({newstate: node})
        if queue.empty():
            break
    actions1=[]
    states = []
    while True:
        curr_action=curnode.p_action
        states.append(curnode.current)
        if curr_action==None:
            break
        actions1.append(curr_action)
        curnode=curnode.parent
    actions1.reverse()
    print([ACTION_LIST[a] for a in actions1])
    print("Steps:", len(actions1))
    #print_states(states[::-1])
    #print(sum([int(s[1]) for s in actions1]))

o_start=time.time()

def print_states(states):
    for state in states:
        print("")
        for i in range(3):
            for j in range(3):
                print(state[i*3+j], end='\t')
            print("")
    
# bfs([[1,2,3],[4,5,6],[7,0,8]])

#open a file
#f=open('C:\\Users\\Admin\\Desktop\\AI\\examples\\easy\\3x3_1',"r")
#print(f.read())
folders = ['examples/easy/', 'examples/moderate/', 'examples/difficult/']    
overall_start = time.time()

file_count = 1
for folder in folders:
    level_start = time.time()
    files = os.listdir(folder)
    for file in files:
        test_path = folder+file
        print(f"\n{file_count}) File: {test_path}:")
        f=open(test_path, "r")
        init_state=[]
        a=f.read()
        s=a.splitlines()
        j=init_state.append(s)
        rep=os.listdir("examples/easy")
        jem = [x.split(" ") for x in s[1:4]]
        for i in range(3):
            for j in range(3):
                jem[i][j] = int(jem[i][j])
        time0=time.time()        
        bfs(jem)
        print(s[-1])
        print("Searching Time:", time.time()-time0)
        file_count += 1
    print("\nLEVEL TIME:", time.time() - level_start)
print("Overall Time:", time.time() - overall_start)
                