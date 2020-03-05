#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:11:12 2020

@author: adeela
"""

'''

BFS(G, s)
for each v ∈ G: color[v] = WHITE; d[v] = ∞ color[s] ← GRAY; d[s] ← 0
Q←∅
ENQUEUE(Q, s)
while Q ≠ ∅
u ← DEQUEUE(Q)
for each v ∈ Adj[u]
if color[v] = WHITE then color[v] ← GRAY d[v] ← d[u] + 1
ENQUEUE(Q, v) color[u] ← BLACK

'''