#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:11:34 2020

@author: adeela
"""

'''
Depth-first search (DFS)

Visual Link --> 
https://www.cs.usfca.edu/~galles/visualization/DFS.html
https://visualgo.net/en/dfsbfs

Psuedocode:
    
DFS(u)

for each neighbor v of u

  if v is unvisited, tree edge, DFS(v)

  else if v is explored, bidirectional/back edge

  else if v is visited, forward/cross edge
  
'''

from collections import defaultdict

#Given a node traverse the longest path 
def dfs(node, time):
    #print(node, time, G[node])

    dist[node] = time  # time it took to reach here from the starting vertex    

    if G[node] == []: # the node has no neighbors
        return time
    
    for node in G[node]:  # traverse each neighbor of given vertex 
        dfs(node[0], time+node[1])



graph_with_weights = [[2,1,1],[2,3,1],[3,4,1]]

# Represent graph as an adjacency list. each item of list is a tuple(vertex, weight)
# If an element is not present in the dictionary default dict does not throw error
G = defaultdict(list)  
for u,v,w in graph_with_weights:
    G[u].append((v,w))
N = 4 #number of nodes
dist = {node: 0 for node in range(1, N+1)}

    
dfs(2,0)
max(dist.values())
