#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:20:58 2020

@author: adeela
"""
'''
Given an array of events where events[i] = [startDayi, endDayi]. 
Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei.
Notice that you can only attend one event at any time d.

'''
from itertools import chain
class Event:

    def maxEvent(List[List[int]]) -> int:
        

A = [[1,2],[1,2],[3,3],[1,5],[1,5]]
1,2 1 1,2   -> 1
1,2 2 1,2   --> 2
1,5 5 1,2,3,4,5  --> 5
1,5 4 1,2,3,4,5 --> 4
3,3 3 1,2,3  -->3

A = [[1,4],[4,4],[2,2],[3,4],[1,1]]
A = [[1,2],[2,3],[3,4]]
A= [[1,2],[2,2],[3,3],[3,4],[3,4]]
1,2 1,2 2 1
2,2 2      2
3,3 3   3  3
3,4 3,4  4  4
3,4 3,4

events= [[1,2],[2,2],[3,3],[3,4],[3,4]]

day_temp = sorted(chain(*events))
days = list(range(day_temp[0], day_temp[-1]+1))

total_events=0
events.sort()
for e in events:
    # pick a day starting from bigger day in range of days event can be attended
    event_days = range(e[0], e[1]+1)
    i = -1
    print(len(event_days) , i, e)
    
    while len(event_days) >= -i:
        if event_days[i] in days:
            print('Attending ', e, ' on ', event_days[i])
            days.remove(event_days[i])
            total_events+=1
            break
        i-=1
        
