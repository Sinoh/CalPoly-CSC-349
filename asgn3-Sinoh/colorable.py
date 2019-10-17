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

    def getColor(self, u):
        for neighbors in self.graph[u]:
            if not (self.color[neighbors] == None):
                if self.color[neighbors] == 'red':
                    return 'blue'
                else:
                    return 'red'

        return 'red'


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
        graph = [[], []]
        queue.append(graph)

        for i in sorted(self.graph):
            found = False
            for index in queue:
                
                if ((len(index[0]) == 0)):
                    index[0].append(i)
                    found = True
                    break
                elif not (len(set(self.graph[i]) & set(index[0])) == 0):
                    index[1].append(i)
                    found = True
                    break
                elif not (len(set(self.graph[i]) & set(index[1])) == 0):
                    index[0].append(i)
                    found = True
                    break
            if (found == False):
                if self.color[i] == 'red':
                    graph = [[i], []]
                else:
                    graph = [[],[i]]
                queue.append(graph)




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

    if (len(content) == 0):
        print('Is not 2-colorable.')
        exit()

    for vertices in range(len(content)):
        if (int(content[vertices][0]) == 0):
            graph.addEdge(int(content[vertices][0]), int(content[vertices][1]))
        else:
            graph.addEdge(int(content[vertices][0]), int(content[vertices][1]))


    for i in (list(graph.graph.keys())):
        if (graph.discovered[i] == False):
            if (graph.explore(i, graph.getColor(i)) == True):
                continue
            else:
                print('Is not 2-colorable.')
                exit()

    graph.prepResult(print_queue)
    print('Is 2-colorable:')

    for i in print_queue:
        for j in i:
            print(*j, sep=', ')

    file.close()
   

if __name__ == "__main__":
    main()
