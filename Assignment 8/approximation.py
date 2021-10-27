import graph as g
import sys

def DFS(graph, vertex_u, visited, parent = None, aproxy = None):

    visited.append(vertex_u)

    for neighbor in graph.__getitem__(vertex_u):
        if neighbor in visited:
            if neighbor == parent:
                continue
            else:
                return True
        if(DFS(graph, neighbor, visited, vertex_u)):
            return True
        
    return False

def ifCycle(graph, vertex_u, vertex_v, wieght):
    visited = []
    g.add_edge(graph, vertex_u, vertex_v, wieght)
    if (DFS(graph,vertex_u, visited)):
        graph.__getitem__(vertex_u).pop(vertex_v, None)
        graph.__getitem__(vertex_v).pop(vertex_u, None)
    return graph

def find_min(graph, list):
    min_weight = 99999
    for i in graph.matrix:
        for j in graph.__getitem__(i):
            if ((i, j) in list):
                continue
            if (min_weight > graph.__getitem__(i)[j]):
                min_weight = graph.__getitem__(i)[j]
    
    return min_weight

def mst(graph):

    mst = g.Graph()
    edge_list = []
    while (len(edge_list) != (len(graph.matrix) * (len(graph.matrix)- 1))):
        min_weight = find_min(graph, edge_list)
        for i in graph.matrix:
            for j in graph.__getitem__(i):
                if ((i, j) in edge_list):
                    continue
                if (graph.__getitem__(i)[j] == min_weight):
                    edge_list.append((i, j))
                    mst = ifCycle(mst, i,j, min_weight)
                    
    return mst

def aproxDFS(graph, vertex_u, visited, aproxy, parent = None):

    if parent != None:
        visited.append(vertex_u)
    for neighbor in sorted(graph.__getitem__(vertex_u)):
        if neighbor == parent or neighbor in visited:
            continue
        else:
            
            g.add_edge(aproxy, vertex_u, neighbor, graph.__getitem__(vertex_u)[neighbor])
            aproxy.__getitem__(neighbor).pop(vertex_u, None)
            return aproxDFS(graph, neighbor, visited, aproxy, vertex_u)
    return aproxy

def aproxDFS2(graph, mstGraph, visited, aproxy, parent = None):
    for vertex_u in (graph.matrix):
        if (len(aproxy.__getitem__(vertex_u)) == 0):
            visited.append(vertex_u)
            for neighbor in graph.matrix:
                if (neighbor != 0) and neighbor not in visited:
                    g.add_edge(aproxy, vertex_u, neighbor, graph.__getitem__(vertex_u)[neighbor])
                    aproxy.__getitem__(neighbor).pop(vertex_u, None)
    

def approximate(graph ,mstGraph):
    visited = []
    vertexRoot = 0
    aproxy = g.Graph()

    for vertex in (mstGraph.matrix):
        g.add_vertex(aproxy, vertex)

    aproxDFS(mstGraph, vertexRoot, visited, aproxy)
    aproxDFS2(graph, mstGraph, visited, aproxy)

    for vertex_u in (graph.matrix):
        if (len(aproxy.__getitem__(vertex_u)) == 0):
            g.add_edge(aproxy, vertex_u, 0, graph.__getitem__(vertex_u)[0])
            aproxy.__getitem__(0).pop(vertex_u, None)
    return aproxy

def main():

    graph = g.read_graph(sys.argv[1])
    mstGraph = mst(graph)
    total_weight = 0
    aproxy = approximate(graph, mstGraph)
    results = []
    vertex = 0
    while(len(results) != len(graph.matrix)):
        results.append(vertex)
        for neighbor in aproxy.__getitem__(vertex):
            total_weight += aproxy.__getitem__(vertex)[neighbor]
            vertex = neighbor
            
    results.append(results[0])
    print("Hamiltonian cycle of weight %i:" % total_weight)
    print(*results, sep=', ')
if __name__ == "__main__":
    main()