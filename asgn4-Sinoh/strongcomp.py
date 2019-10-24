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
    temp1 = cycles
    temp2 = cycles
    for x in temp1:
        for y in temp2:
            if x == y:
                continue
            elif set(x) & set(y):
                temp1.append(x + list(set(y) - set(x)))
                temp1.remove(x)
                temp1.remove(y)
    return temp1

def selectionSort(results):            
    for i in range(len(results)):
        min_idx = i
        for j in range(i+1, len(results)):
            if results[min_idx][0] > results[j][0]:
                min_idx = j
        results[i], results[min_idx] = results[min_idx], results[i]
    return results

def prepResult(graph):
    results = []
    single = True
    for cycles in graph.cycles:
        cycles = sorted(cycles)
        if cycles not in results:
            results.append(cycles)

    results = common_element(results)

    for vertex in sorted(graph.vertices):
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
        i = sorted(i)
        print(*i, sep=', ')
if __name__ == "__main__":
    main()