#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:28:19 2020

@author: adeela
"""
'''
Red Black Trees
'''

class Node:

    def __init__(self, key, c):
        self.left   = None
        self.right  = None
        self.color = c
        self.val = key