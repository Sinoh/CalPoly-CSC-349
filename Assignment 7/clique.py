import subgraph_isomorphism as si
import sys
import graph as graph

def gernerateClique(k):
    cliqueGraph = graph.Graph()

    for v in range(k):
        for u in range(k):
            if v == u:
                continue
            graph.add_edge(cliqueGraph, v, u)

    return cliqueGraph

def clique(graph_g, k):
    cliqueGraph = gernerateClique(k)
    return si.isomorphic_subgraph(graph_g, cliqueGraph)


def main():

    graph_g = graph.read_graph(sys.argv[1])
    subgraph = clique(graph_g, int(sys.argv[2]))
    if subgraph is not None:
        print("Verticies of clique of %i:" % int(sys.argv[2]))
        print(", ".join([str(v) for v in sorted(subgraph)]))
        return 0
    else:
        print("No verticies in clique of %i." % int(sys.argv[2]))
        return 1


if __name__ == "__main__":
    main()