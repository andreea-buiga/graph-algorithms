from random import randint
from graph.graph import Graph


def read_graph_from_file(filename):
    """
    function used for reading a graph from a file
    :param filename: the file from where to read
    :return: the read graph
    """
    try:
        f = open(filename, "r")
        line = f.readline().strip("\n")
        line = line.split(" ")
        number_of_vertices = int(line[0])
        number_of_edges = int(line[1])
        graph = Graph(number_of_vertices)
        for i in range(0, number_of_edges):
            line = f.readline().strip("\n")
            line = line.split(" ")
            graph.add_edge(int(line[0]), int(line[1]), int(line[2]))
        for i in range(0, number_of_vertices):
            if graph.get_in_degree(i) == 0 and graph.get_out_degree(i) == 0:
                graph.add_isolated_vertex(i)
        f.close()
    except IOError as error:
        print("\n• an error occured -" + str(error))
        raise error
    return graph


def write_graph_to_file(filename, graph):
    """
    function used for writing a graph from a file
    :param filename: the file where to write
    :param graph: the graph to be written
    """
    f = open(filename, "w")
    try:
        vertices = graph.get_number_of_verteces()
        edges = graph.get_number_of_edges()
        f.write(str(vertices) + " " + str(edges) + "\n")
        costs = graph.get_all_costs()
        for vertex_1, vertex_2 in costs:
            f.write(str(vertex_1) + " " + str(vertex_2) + " " + str(costs[vertex_1, vertex_2]) + "\n")
        isolated = graph.get_all_isolated()
        for vertex in isolated:
            f.write(str(vertex) + "\n")
        f.close()
    except IOError as error:
        print("An error occurred -" + str(error))
        raise error


def create_random_graph(number_of_vertices, number_of_edges):
    """
    function that creates a random graph
    :param number_of_vertices: the total number of vertices
    :param number_of_edges: the total number of edges
    :return: the random graph created
    """
    graph = Graph(number_of_vertices)
    times = 0
    while times < number_of_edges:
        vertex_1 = randint(0, number_of_vertices - 1)
        vertex_2 = randint(0, number_of_vertices - 1)
        if not graph.is_edge(vertex_1, vertex_2):
            cost = randint(0, 100)
            graph.add_edge(vertex_1, vertex_2, cost)
            times = times + 1
    for i in range(0, number_of_vertices):
        if graph.get_in_degree(i) == 0 and graph.get_out_degree(i) == 0:
            graph.add_isolated_vertex(i)
    return graph
