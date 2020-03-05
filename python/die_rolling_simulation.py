#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:29:21 2020

@author: adeela
"""

import numpy as np
import matplotlib.pyplot as plt
import random as r

# rolling a die simulation to see how many time 6 comes
# with large number of trails proportion of times 6 appears settles to a particular number. 

total_trial_num = 1000  # 100
total_6 = 0 
cumm_freq_6 = np.array([])

for n in range(1,total_trial_num):
    trial = r.randint(1,6)
    if trial == 6:
        total_6 += 1   
        x = total_6/n
    cumm_freq_6 = np.append(cumm_freq_6, [x])
       

plt.plot(cumm_freq_6)    
        
