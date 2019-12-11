# Represents an undirected, weighted graph.
# NOTE: Do not alter this file.
# CSC 349, Assignment 8
# Given code, Fall '19


class Graph:
    """ A collection of vertices connected by weighted edges """

    def __init__(self, num_vertices = 0):
        # The backing adjacency dictionary:
        self.matrix = {vertex: {} for vertex in range(num_vertices)}

    def __eq__(self, other):
        return type(other) == Graph and self.matrix == other.matrix

    def __repr__(self):
        return "Graph({\n    %s\n})" % ",\n    ".join(
                ["%s: %s" % (v, sorted(self[v])) for v in sorted(self)])

    def __iter__(self):
        return iter(self.matrix)

    def __contains__(self, item):
        return item in self.matrix

    def __getitem__(self, key):
        return self.matrix[key]

    def __setitem__(self, key, value):
        self.matrix[key] = value


def add_vertex(graph, vertex):
    """
    Add a vertex to a graph, if it does not exist.
    :param graph: The graph to which to add the vertex
    :param vertex: The vertex to be added
    :return: The vertex's adjacency dictionary
    """
    return graph.matrix.setdefault(vertex, {})


def add_edge(graph, vertex_u, vertex_v, weight):
    """
    Add an edge to a graph, adding vertices first if they do not exist.
    :param graph: The graph to which to add the edge
    :param vertex_u: The edge's first endpoint
    :param vertex_v: The edge's second endpoint
    :param weight: The weight of the edge
    :return: The resulting graph
    """
    add_vertex(graph, vertex_u)[vertex_v] = weight
    add_vertex(graph, vertex_v)[vertex_u] = weight
    return graph


def read_graph(graph_fname):
    """
    Read a graph from a file.
    :param graph_fname: The name of a file containing an edge list
    :return: The corresponding new graph
    """
    graph = Graph()

    with open(graph_fname, "r") as graph_file:
        for edge in graph_file:
            add_edge(graph, *(int(v) for v in edge.strip().split(", ")))

    return graph
