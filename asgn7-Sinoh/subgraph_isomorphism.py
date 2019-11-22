# Naively brute forces the subgraph isomorphism problem.
# NOTE: Do not alter this file.
# CSC 349, Assignment 7
# Given code, Fall '19


import sys
import itertools
import graph


def isomorphic_subgraph(graph_g, graph_h):
    """
    Determine whether a graph G contains a subgraph isomorphic to a graph H.
    :param graph_g: The graph G
    :param graph_h: The graph H
    :return: An isomorphic subgraph, None if no such subgraph exists
    """

    # For every possible subgraph of G...
    for vertices in itertools.combinations(graph_g, len(graph_h.matrix)):
        subgraph = _subgraph(graph_g, set(vertices))
        if _isomorphism(subgraph, graph_h) is not None:
            return subgraph

    return None


def _subgraph(graph_g, vertices):
    """
    Construct the subgraph induced by a set of vertices.
    :param graph_g: The graph from which to construct a subgraph
    :param vertices: A set of vertices in the graph
    :return: The subgraph induced by the set of vertices
    """
    subgraph = graph.Graph()
    subgraph.matrix = {v: graph_g[v] & vertices for v in vertices}

    return subgraph


def _isomorphism(graph_g, graph_h):
    """
    Determine whether a graph G is isomorphic to a graph H.
    :param graph_g: The graph G
    :param graph_h: The graph H
    :return: An isomorphism if G is isomorphic to H, None otherwise
    """

    # If the graphs have differing numbers of vertices,
    #  then they cannot possibly be isomorphic.
    if len(graph_g.matrix) != len(graph_h.matrix):
        return None

    # For every possible bijection f: V(H) -> V(G)...
    h_vertices = list(graph_h)
    for g_vertices in itertools.permutations(graph_g):
        map_f = {v: u for v, u in zip(h_vertices, g_vertices)}
        if _is_isomorphism(lambda v: map_f[v], graph_g, graph_h):
            return map_f

    return None


def _is_isomorphism(fn_f, graph_g, graph_h):
    """
    Determine whether a mapping is an isomorphism.
    :param fn_f: A bijection f: V(H) -> V(G)
    :param graph_g: A graph G
    :param graph_h: A graph H
    :return: True if fn_f is an isomorphism, False otherwise
    """
    for vertex in graph_h:
        for neighbor in graph_h[vertex]:
            # If two vertices are adjacent in H, then their corresponding
            #  vertices must be adjacent in G. The converse need not hold.
            if fn_f(neighbor) not in graph_g[fn_f(vertex)]:
                return False

    return True


def main(argv):
    graph_g = graph.read_graph(argv[1])
    graph_h = graph.read_graph(argv[2])
    subgraph = isomorphic_subgraph(graph_g, graph_h)

    if subgraph is not None:
        print("Isomorphic vertices:")
        print(", ".join([str(v) for v in sorted(subgraph)]))
        return 0
    else:
        print("No isomorphic vertices.")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
