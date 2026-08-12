class Graph:

    def __init__(self):
        self.adjList = {}

    def set_vertex(self, vertex):
        self.adjList[vertex] = []

    def set_edge(self, edgeFrom, edgeTo):
        self.adjList[edgeFrom].append(edgeTo)
        self.adjList[edgeTo].append(edgeFrom)

    def get_vertices(self):
        return self.adjList.keys()

    def get_edges(self):
        return self.adjList.items()

    def get_edges_vertex(self, vertex):
        return self.adjList.get(vertex)



def main():
    g = Graph()

    g.set_vertex('a')
    g.set_vertex('b')
    g.set_vertex('c')

    g.set_edge('a', 'b')
    g.set_edge('b', 'c')

    print(g.get_vertices())
    print(g.get_edges())

    print(g.get_edges_vertex("b"))


if "__name__" == "main":
    main()
