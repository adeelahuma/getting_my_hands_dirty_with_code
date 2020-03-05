#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:48:54 2020

@author: adeela
"""

# =============================================================================
#       Random Function
# =============================================================================
    
# =============================================================================
#       Sum of digits in 'n'    
# =============================================================================
sum_digits = 0 
n = 4223

while n != 0:
    sum_digits += n%10
    n = int(n/10)
    
    
    
# =============================================================================
#     DPS from Leetcode
# =============================================================================
from collections import defaultdict

times = [[2,1,1],[2,3,1],[3,4,1]]
N=4
K=2
graph = defaultdict(list)
for u, v, w in times:
    graph[u].append((w, v))

dist = {node: float('inf') for node in range(1, N+1)}

def dfs(node, elapsed):
    print(node, elapsed)
    if elapsed >= dist[node]: return
    dist[node] = elapsed
    for time, nei in sorted(graph[node]):
        dfs(nei, elapsed + time)

dfs(K, 0)
ans = max(dist.values())
return ans if ans < float('inf') else -1


count = defaultdict()
 1 in count
 count[1]+= 5

len(A)

import math