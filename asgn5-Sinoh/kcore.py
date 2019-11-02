import sys
from collections import defaultdict 

class Graph:

    def __init__(self):
        self.vertices = defaultdict(list)
        self.cycles = []
        self.results = []

    def addVertex(self, u):
        self.vertices[u.vertex].append(u)

    def getVertex(self, u):
        return self.vertices[u][0]

    def makeUndiscovered(self):
        for vertex in self.vertices:
            self.vertices[vertex][0].discovered = False

    def updateDegree(self):
        for vertex in self.vertices:
            self.getVertex(vertex).degree = len(self.getVertex(vertex).edges)

    def printVerticies(self):
        for vertex in self.vertices:
            print(vertex, self.vertices[str(vertex)][0].edges)
    
    def removeVertex(self, u):
        for vertex in self.vertices:
            self.getVertex(vertex).removeEdge(u)
        self.vertices.pop(u, None)

    def preResults(self):
        max = 0
        for vertex in self.vertices:
            if len(self.getVertex(vertex).edges) > max:
                max = len(self.getVertex(vertex).edges)
        for i in range(max + 1):
            self.results.append([['Vertices in {}-cores:'.format(i)],[]])

    def updateResults(self, vertex, k):
        self.results[k][1].append(int(vertex.vertex))

    def degreeDFS(self, vertex, k):
        vertex.discovered = True
        for neighbors in vertex.edges:
            neighbor = self.getVertex(neighbors)
            if vertex.degree < k:
                neighbor.degree -= 1
            
            if neighbor.discovered == False:
                self.degreeDFS(neighbor, k)

class Vertex:

    def __init__(self, vertex):
        self.vertex = vertex
        self.discovered = False
        self.edges = []
        self.degree = 0

    def addEdge(self, u):
        self.edges.append(u.vertex)
        u.edges.append(self.vertex)
    
    def removeEdge(self, u):
        if u in self.edges:
            self.edges.remove(u)

def getKCores(graph, k):
    graph.degreeDFS(graph.getVertex('0'), k)
    
    for verticies in graph.vertices:
        vertex = graph.getVertex(verticies)
        if vertex.discovered == False:
            graph.degreeDFS(vertex, k)

    for verticies in graph.vertices:
        vertex = graph.getVertex(verticies)
        if vertex.degree >= k:
            graph.updateResults(vertex,k)

def main():

    graph = Graph()

    with open(sys.argv[1]) as file: # Read the inputed file
        for lines in file:
            lines = lines.replace(',','').strip().split()

            vertex0 = Vertex(lines[0])
            vertex1 = Vertex(lines[1])

            if (lines[0] not in graph.vertices):
                graph.addVertex(vertex0)
            if (lines[1] not in graph.vertices):
                graph.addVertex(vertex1)
            
            graph.getVertex(vertex0.vertex).addEdge(graph.getVertex(vertex1.vertex))
    
    graph.preResults()
    graph.updateDegree()

    for i in range(0, len(graph.results)):
        getKCores(graph, i)
        graph.makeUndiscovered()
        graph.updateDegree()
    
    for index in range(len(graph.results)):
        if index == 0:
            continue
        if len(graph.results[index][1]) > 0:
            print(graph.results[index][0][0])
            print(*sorted(graph.results[index][1]), sep=', ')

        
if __name__ == "__main__":
    main()