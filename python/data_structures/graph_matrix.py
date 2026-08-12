#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: adeela
"""


class Graph:
    
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.vertices = [0] * numVertices
        self.adjMatrix = [[-1] * numVertices for x in range(numVertices)]
    
    def set_vertex(self, vertexId, vertexName):
        self.vertices[vertexId] = vertexName
    
    def set_edge(self, edge_to, edge_from):
        self.adjMatrix[edge_to][edge_from] = 1
        self.adjMatrix[edge_from][edge_to] = 1

        
    def remove_edge(self, edge_to, edge_from):
        self.adjMatrix[edge_to][edge_from] = 0

    def get_edges(self):
        edges = []
        for row in range(len(self.vertices)):
            for col in range(len(self.vertices)):
                if self.adjMatrix[row][col] > 0:
                    edge = (self.vertices[row], self.vertices[col], self.adjMatrix[row][col])
                    edges.append(edge)
        return edges


    def get_vertices(self):
        return self.vertices
        
    def __str__(self):
        return "Graph has {} vertices ".format(self.numVertices)
    
    
g = Graph(5)  

g.set_vertex(0,'a')
g.set_vertex(1,'b')
g.set_vertex(2,'c')
g.set_vertex(3,'d')
g.set_vertex(4,'e')

g.set_edge(0,1)
g.set_edge(0,2)


print(g.adjMatrix)

print(g.get_edges())

