from graph.undirectedgraph import UndirectedGraph


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
        graph = UndirectedGraph(number_of_vertices)
        for i in range(0, number_of_edges):
            line = f.readline().strip("\n")
            line = line.split(" ")
            graph.add_edge(int(line[0]), int(line[1]), int(line[2]))
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
        vertices = graph.get_number_of_vertices()
        edges = graph.get_number_of_edges()
        f.write(str(vertices) + " " + str(edges) + "\n")
        costs = graph.get_all_costs()
        for vertex_1, vertex_2 in costs:
            f.write(str(vertex_1) + " " + str(vertex_2) + " " + str(costs[vertex_1, vertex_2]) + "\n")
        f.close()
    except IOError as error:
        print("An error occurred -" + str(error))
        raise error
