import sys
from collections import defaultdict 

class Graph:

    def __init__(self):
        self.vertices = defaultdict(list)
        self.cycles = []

    def addVertex(self, u):
        self.vertices[u.vertex].append(u)

    def getVertex(self, u):
        return self.vertices[u]

    def makeUndiscovered(self):
        for vertex in self.vertices:
            self.vertices[vertex][0].discovered = False

class Vertex:

    def __init__(self, vertex):
        self.vertex = vertex
        self.discovered = False
        self.pre = None
        self.post = None
        self.edges = []

    def addEdge(self, u):
        self.edges.append(u)

def Explore(graph, v, startv, path):
    v.discovered = True
    path.append(v.vertex)
    for neighbor in sorted(v.edges):
        if (graph.getVertex(neighbor)[0].discovered == False):
            Explore(graph, graph.getVertex(neighbor)[0], startv, path.copy())
        else:
            if (graph.getVertex(neighbor)[0].vertex == startv):
                graph.cycles.append(path)
    return v

def depthFirstSearch(graph):
    counter = 1
    for vertex in sorted(graph.vertices):
        path = []
        if (graph.getVertex(vertex)[0].discovered == False):
            Explore(graph, graph.getVertex(vertex)[0], graph.getVertex(vertex)[0].vertex, path.copy() )
            graph.makeUndiscovered()
            counter += 1

def common_element(cycles):

    results = []
    while len(cycles) > 0:
        first, *rest = cycles
        first = set(first)

        lf = -1

        while len(first) > lf:
            lf = len(first)
            rest2 = []
            for r in rest:
                if len(first.intersection(set(r))) > 0:
                    first |= set(r)
                else:
                    rest2.append(r)
            rest = rest2
        results.append(first)
        cycles = rest

    for i in range(len(results)):
       results[i] = list(results[i])
    return results

def selectionSort(results):            
    for i in range(len(results)):
        min_idx = i
        for j in range(i+1, len(results)):
            if int(results[min_idx][0]) > int(results[j][0]):
                min_idx = j
        results[i], results[min_idx] = results[min_idx], results[i]
        
    return results

def prepResult(graph):
    results = []
    single = True
    for cycles in graph.cycles:
        cycles = sorted(map(int, cycles))
        if cycles not in results:
            results.append(cycles)

    results = common_element(results)

    for vertex in sorted(map(int, graph.vertices)):
        for cycles in results:
            if vertex in cycles:
                single = False
        if (single):
            results.append([vertex])
        single = True

    results = selectionSort(results)
    return results

def main():

    graph = Graph()

    with open(sys.argv[1]) as file: # Read the inputed file
        for lines in file:
            lines = lines.replace(',','').strip().split()

            if (lines[0] not in graph.vertices):
                if (lines[1] not in graph.vertices):
                    vertex = Vertex(lines[1])
                    graph.addVertex(vertex)
                vertex = Vertex(lines[0])
                vertex.addEdge(lines[1])
                graph.addVertex(vertex)
            else:
                if (lines[1] not in graph.vertices):
                    vertex = Vertex(lines[1])
                    graph.addVertex(vertex)
                graph.vertices.get(lines[0])[0].addEdge(lines[1])
    
    depthFirstSearch(graph)
    result = prepResult(graph)
    print("{} Strongly Connected Component(s):".format(len(result)))
    for i in result:
        print(*i, sep=', ')
if __name__ == "__main__":
    main()