class Graph2:
    def __init__(self, adj_list):
        self.adj_list = adj_list
        
    def add_vertex(self, vertex, neighbors, weights):
        self.adj_list[vertex] = []
        for i in range(len(neighbors)):
            self.adj_list[vertex].append([neighbors[i], weights[i]])
            self.adj_list[neighbors[i]].append([vertex, weights[i]])
    
    def add_edge(self, vertex1, vertex2, weight):
        self.adj_list[vertex1].append([vertex2, weight])
        self.adj_list[vertex2].append([vertex1, weight])
    
    def get_neighbors(self, vertex):
        hits = []
        for i in self.adj_list[vertex]:
            hits.append(i[0])
        return hits
    
    def get_incident_edges(self, vertex):
        return self.adj_list[vertex]
    
    def get_vertices(self):
        return self.adj_list.keys()
    
    def get_edges(self):
        return self.adj_list.items()
    
    def DFS(self, vertex, visited, compID, currID):
        currPos = list(self.get_vertices()).index(vertex)
        if visited[currPos] == True:
            return
        visited[currPos] = True
        compID[currPos] = currID
        for i in self.get_neighbors(vertex):
            self.DFS(i, visited, compID, currID)
    
    def get_ID_array(self):
        visited = [-1 for i in self.get_vertices()]
        visited[0] = False
        compID = [-1 for i in self.get_vertices()]
        currID = 0
        for i in self.get_vertices():
            currPos = list(self.get_vertices()).index(i)
            if visited[currPos] == False:
                currID = currID + 1
                self.DFS(i, visited, compID, currID)
        return compID
        
    def is_reachable(self, vertex1, vertex2):
        compID = self.get_ID_array()
        v1pos = list(self.get_vertices()).index(vertex1)
        v2pos = list(self.get_vertices()).index(vertex2)
        if compID[v1pos] == compID[v2pos]:
            return True
        else:
            return False
        
        