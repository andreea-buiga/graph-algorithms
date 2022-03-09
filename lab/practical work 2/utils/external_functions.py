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
            graph.add_edge(int(line[0]), int(line[1]))
        f.close()
    except IOError as error:
        print("\n• an error occured -" + str(error))
        raise error
    return graph
