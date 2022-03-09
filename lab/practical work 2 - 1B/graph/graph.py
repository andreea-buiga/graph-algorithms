class GraphException(Exception):
    def __init__(self, errors):
        self._errors = errors

    def get_errors(self):
        return self._errors


class Graph:
    def __init__(self, n):
        """
        constructor for a graph
        :param n: the number of vertices
        in_neighbours - the predecesors
        out_neighbours - the successors
        costs - the cost of every edge
        isolated - the isolated vertices
        """
        self._vertices = n
        self._edges = {}
        self._vert_list = []
        for i in range(0, n):
            self._edges[i] = []
            self._vert_list.append(i)

    def get_number_of_verteces(self):
        """
        getter for the number of vertices of the graph
        :return: total number of vertices of the graph
        """
        return self._vertices

    def get_number_of_edges(self):
        """
        getter for the number of edges of the graph
        :return: total number of edges of the graph
        """
        return len(self._edges)

    def get_all_edges(self):
        """
        getter for the costs of the graph ((vertex_1, vertex_2) with cost)
        :return: costs of the graph
        """
        return self._edges

    def parse_vertices_of_the_graph(self):
        """
        function that parses through the vertices of the graph
        :return: the vertex
        """
        for v in self._edges:
            yield v

    def add_edge(self, vertex_1, vertex_2):
        """
        function that adds an edge between two vertices
        :param vertex_1: the vertex from where the edge starts
        :param vertex_2: the vertex where the edge ends
        :return: -
        """
        self._edges[vertex_1].append(vertex_2)

    def strongly_connected(self):
        """
        function that returns the strongly connected components of the graph
        :return: the strongly connected components of the graph
        """
        visited = set()
        stack = []
        position = {}
        limits = []
        for vertex in self._vert_list:
            if vertex not in position:
                for strongly_connected_component in self.dfs(vertex, visited, stack, position, limits):
                    yield strongly_connected_component

    def dfs(self, start, visited, stack, position, limits):
        """
        function that uses dfs for finding a strongly connected component for a vertex
        :param start: the starting vertex
        :param visited: the list of visited vertices
        :param stack: the strongly connected component
        :param position: dictionary that has as key the vertex and as value the position in the stack
        :param limits: the limits of each strongly connected component
        :return: the strongly connected component
        the function will recursively call
        """
        position[start] = len(stack)
        stack.append(start)
        limits.append(position[start])
        for vertex in self._edges[start]:
            if vertex not in position:
                for strongly_connected_component in self.dfs(vertex, visited, stack, position, limits):
                    yield strongly_connected_component
            elif vertex not in visited:
                while position[vertex] < limits[-1]:
                    limits.pop()
        if limits[-1] == position[start]:
            limits.pop()
            strongly_connected_component = set(stack[position[start]:])
            del stack[position[start]:]
            visited.update(strongly_connected_component)
            yield strongly_connected_component
