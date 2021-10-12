class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        
    def add_vertex(self, vertex, neighbors, weights):
        self.vertices.append(vertex)
        for i in range(len(neighbors)):
            self.edges.append((vertex, neighbors[i], weights[i]))
    
    def add_edge_between(self, vertex1, vertex2, weight):
        self.edges.append((vertex1, vertex2, weight))
    
    def remove_vertex(self, vertex):
        self.vertices.pop(self.vertices.find(vertex))
        for i in range(len(self.edges)):
            if vertex in self.edges[i]:
                self.edges.pop(i)
    
    def remove_edge(self, vertex1, vertex2):
        for i in range(len(self.edges)):
            if vertex1 in self.edges[i] and vertex2 in self.edges[i]:
                self.edges.pop(i)
    
    def get_neighbors(self, vertex):
        hits = []
        for i in self.edges:
            if vertex in i:
                hits.append(i)
        return hits
    
    def get_vertices(self):
        return self.vertices
    
    def get_edges(self):
        return self.edges
    