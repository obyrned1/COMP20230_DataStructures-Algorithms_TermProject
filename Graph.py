""" A Python Class
A simple Python graph class that uses a dictionary to store the vertices and adjacent nodes.
Adapted from: https://www.python-course.eu/graphs_python.php

Example graphs instance used graph structure from the lectures.
"""


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":


    g = Graph()
    vertices= ['a','b','c','d','e','f','g','h','i']
    for v in vertices:
        g.add_vertex(v)
    print("Vertices of graph:", g.vertices())
    #     vertex a adjacency list 
    g.add_edge({'a','b'})
    g.add_edge({'a','c'})
    g.add_edge({'a','d'})
    g.add_edge({'a','e'})
    g.add_edge({'a','j'})
    #     vertex b adjacency list     
    g.add_edge({'b','e'})
    g.add_edge({'b','f'})    


    g.add_edge({'c','d'})
    
    g.add_edge({'d','j'})

    g.add_edge({'e','f'})
    g.add_edge({'e','h'})
    
    
    g.add_edge({'f','g'})

    g.add_edge({'g','i'})
    
    g.add_edge({'h','i'})
    g.add_edge({'i','j'})
    
    print("Edges of graph:")
    print(g.edges())

    g.add_edge({'c','a'})#this is a duplicate a-c already added    
    print("Edges of graph after adding duplicate:")    
    print(g.edges())    

# The Graph class constructor allows a dictionary to be passed to the init method where 
# the key is the vertex and the values are the adjacency list values


    gdict = { "a" : ["b","c","d","e","j"],
          "b" : ["a","e","f"],
          "c" : ["a", "d"],
          "d" : ["a", "c", "j"],
          "e" : ["a","b","f","h"],
          "f" : ["b","e","g"],
          "g" : ["f","i"],
          "h" : ["e","i"],
          "i" : ["g","h","j"],
          "j" : ["a","d","i"]
    }


    graph = Graph(gdict)
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())