#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 08:52:10 2020

@author: adeela
"""

'''
Binary Search Tree

>> Each node contains 'key' and attributes right, left and p representing 
    right child, left child and parent respectively. 
>>Root is the only node whoes parent is nil(missing)
>>the keys in the binary search tree are always sorted to satisfy 
binary search tree property: 
        if x is a node then x.left.key <= x.key and x.right.key >= x.key

>>BST property allows to print keys in sorted order 

>>INORDER TREE WALK   : print left, root, right 
 Time complexity : O(n)
>>PREORDER TREE WALK  : print root, left, right     | root, right, left 
>>POSTORDER TREE WALK : print left, right , root    | right, left, root            
    
>>Finding MAXIMUM --> traverse the right keys from the root
>>Finding MINIMUM --> traverse the left keys from the root 
>>Finding SUCCESSOR -->  Given a node in BST, we need to find the successor in 
    sorted order determined by inorder tree walk. 
    (the element that comes after a given element in sorted order) 
    If keys are distinct than successor of node x is the node with key greater 
    than  x.key
    
>>Finding PREDECESSOR --> opposite of successor 

>>INSERTION 
>>DELETION

'''

class Node:
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.val = key

    def search(root, key):
        print(root.val if root != None else root, key)
        
        # Base case 
        if root is None or root.val == key:            
            return root
    
        if root.val < key: # recursive case 
            return search(root.right, key)
    
        return search(root.left, key)    
        
        
    def inorder_bst(root):
        
        if root != None:   
            inorder_bst(root.left)
            print(root.val)
            inorder_bst(root.right)

     def preorder_bst(root):
        
        if root != None:   
            print(root.val)
            inorder_bst(root.left)
            inorder_bst(root.right)
            
     def postorder_bst(root):
        
        if root != None:   
            inorder_bst(root.left)
            inorder_bst(root.right)
            print(root.val)

#    def maximum(root):
#        if root != None:
#            maximum(root.right)
#        print(root.val)
#        
#        
#    def insert(root, key):
#        if root == None:
#            return root
#        
#        if root.val < key:
#            insert(root.right)
#        else insert(root.left)
        
    
    
root = Node(10)
root.left = Node(2)
root.right = Node(13)

inorder_bst(root)
preorder_bst(root)
postorder_bst(root)


