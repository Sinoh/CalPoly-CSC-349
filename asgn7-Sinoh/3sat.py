import subgraph_isomorphism as si
import clique as c
import graph as g
import sys
from string import digits


def prepResults(graph):
    results = []
    results = (", ".join(str(v) for v in sorted(graph)).replace(' ', '').split(','))
    remove_digits = str.maketrans('', '', digits) 
    results = [i.translate(remove_digits) for i in results]

    results = list(dict.fromkeys(results)) 
    return results


def sortKeys(v):
    if v[0] =='~':
        var = v[1]
        return '{0}~'.format(var)
    else:
        return v

def connection(u, v):
    if not (len(u) == len(v)):
        if len(v) == 4:
            if u[1] == v[2]:
                return False
        else:
            if v[1] == u[2]:
                return False
    return True

def createGraph(graph, clauses):
    for i in range(len(clauses)):
        for j in range(len(clauses)):
            if not (i // 3 == j // 3):
                if connection(clauses[i], clauses[j]):
                    g.add_edge(graph, clauses[i], clauses[j])

def parser(line, graph):
    start = end = 0
    clauses = []
    verticies = []

    while not (end >= len(line)):
        end = line.find(')', start) + 1
        clause = line[start:end]
        start = line.find('(', end)
        clauses.append(clause[2:-2].replace(' ', '').split('|'))
    
    for i in range(len(clauses)):
        for j in range(3):
            verticies.append(str(i + 1) + clauses[i][j] + str(j))

    createGraph(graph, verticies)
    return clauses

def main():
    subgraph = g.Graph()
    with open(sys.argv[1]) as file: # Read the inputed file
        line = file.readline().strip()
        clauses = parser(line, subgraph)

    if len(clauses) == 1:
        g.add_edge(subgraph, '1' + clauses[0][0]+'1', '1' + clauses[0][0] +'1')
    else:
        subgraph = c.clique(subgraph, len(clauses))
    
    if subgraph is not None:
        results = prepResults(subgraph)
        print("Satisfying assignment:")
        print(*sorted(results, key = sortKeys), sep=', ')
        return 0
    else:
        print("No satisfying assignments.")
        return 1


if __name__ == "__main__":
    main()