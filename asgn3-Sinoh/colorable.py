import sys
from collections import defaultdict 

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.discovered = [False] * vertices
        self.color = [None] * vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[u] = sorted(self.graph[u])
        self.graph[v].append(u)
        self.graph[v] = sorted(self.graph[v])

    def swapColor(self, color):
        if (color == 'red'):
            return 'blue'
        else:
            return 'red'
    
    def checkColor(self, u, color):

        for i in self.graph[u]:
            if (self.color[i] == color):
                return False
            else:
                return True
        
    def explore(self, u, color):
        self.discovered[u] = True
        
        if (self.checkColor(u, color) == True):
            self.color[u] = color
        else:
            return False

        for neighbors in self.graph[u]:
            if (self.discovered[neighbors] == False):
                if (self.explore(neighbors, self.swapColor(color)) == False):
                    return False
        return True

    def prepResult(self, queue):
        group1 = []
        group2 = []
        for i in range(len(self.graph)):
            if (self.color[list(self.graph.keys())[i]] == None and i > 0):
                break
            elif (self.color[list(self.graph.keys())[i]] == self.color[list(self.graph.keys())[0]]):
                group1.append(list(self.graph.keys())[i])
            else:
                group2.append(list(self.graph.keys())[i])
        
        queue.append(group1)
        queue.append(group2)
        


def countVertex(array):
    list = []

    for i in array:
        if (i[0] not in list):
            list.append(i[0])
        if (i[1] not in list):
            list.append(i[1])
    
    return len(list)


def main():

    content = []
    print_queue = []
    with open(sys.argv[1]) as file: # Read the inputed file
        for lines in file:
            content.append(lines.replace(',','').strip().split())

    graph = Graph(countVertex(content))

    for vertices in range(len(content)):
        if (int(content[vertices][0]) == 0):
            graph.addEdge(int(content[vertices][0]), int(content[vertices][1]))
        elif (int(content[vertices][0]) in graph.graph or int(content[vertices][1]) in graph.graph):
            graph.addEdge(int(content[vertices][0]), int(content[vertices][1]))
        else:
            if (graph.explore(list(graph.graph.keys())[0], 'red') == False):
                print('Is not 2-colorable.')
                exit()
            graph.prepResult(print_queue)
            graph.graph.clear()
            graph = Graph(countVertex(content))
            graph.addEdge(int(content[vertices][0]), int(content[vertices][1]))
            
    if (graph.explore(list(graph.graph.keys())[0], 'red') == True):
        graph.prepResult(print_queue)
    else:
        print('Is not 2-colorable.')
        exit()

    print('Is 2-colorable:')
    for i in print_queue:
        print(*i, sep=', ')
    file.close()
   

if __name__ == "__main__":
    main()