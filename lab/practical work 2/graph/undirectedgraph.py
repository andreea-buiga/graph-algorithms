from itertools import chain


class UndirectedGraphException(Exception):
    def __init__(self, errors):
        self._errors = errors

    def get_errors(self):
        return self._errors


class UndirectedGraph:
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
        for i in range(0, n):
            self._edges[i] = []

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

    def add_edge(self, vertex_1, vertex_2):
        """
        function that adds an edge between two vertices
        :param vertex_1: the vertex from where the edge starts
        :param vertex_2: the vertex where the edge ends
        :return: -
        """
        if vertex_1 not in self._edges[vertex_2] and vertex_2 not in self._edges[vertex_1]:
            self._edges[vertex_1].append(vertex_2)
            self._edges[vertex_2].append(vertex_1)
        else:
            return UndirectedGraphException("\n• edge " + str(vertex_1) + "-" + str(vertex_2) + "already exists!\n")

    def remove_edge(self, vertex_1, vertex_2):
        """
        function that removes an edge between two vertices
        :param vertex_1: the vertex from where the edge starts
        :param vertex_2: the vertex where the edge ends
        :return: -
        :precondition: • check if the edge exists
        """
        if vertex_1 not in self._edges:
            return UndirectedGraphException("\n• vertex " + str(vertex_1) + "doesn't exists!\n")
        if vertex_2 not in self._edges:
            return UndirectedGraphException("\n• vertex " + str(vertex_2) + "doesn't exists!\n")

        if vertex_1 in self._edges[vertex_2] and vertex_2 in self._edges[vertex_1]:
            self._edges[vertex_1].remove(vertex_2)
            self._edges[vertex_2].remove(vertex_1)

    def add_vertex(self, vertex):
        """
        function that adds a new vertex
        :param vertex: the new vertex to be added
        :return: -
        :precondition: • check if the vertex exists
        """
        if vertex in self._edges:
            return UndirectedGraphException("\n• vertex already exists!\n")

        self._edges[vertex] = []

    def remove_vertex(self, vertex):
        """
        function that removes a vertex
        :param vertex: the vertex to be removed
        :return: -
        :precondition: • check if the vertex exists
        """
        if vertex not in self._edges:
            return UndirectedGraphException("\n• vertex doesn't exists!\n")

        for v in self._edges[vertex]:
            self._edges[v].remove(vertex)
        self._edges.pop(vertex)

    def parse_vertices_of_the_graph(self):
        """
        function that will parse through all the vertices of the graph
        :return: the vertices
        """
        for v in self._edges:
            yield v

    def connected_components(self):
        """
        function that finds the connected components of the undirected graph
        :return: all the connected components of the graph

        visited list will mark every vertex we checked so when a vertex_1 is connected to vertex_2,
        we will not revisit the connected component of vertex_2
        """
        visited = []
        connected_components = []
        for vertex in self._edges:
            if vertex not in visited:
                connected_component = []
                visited, connected_component = self.dfs(vertex, visited, connected_component)
                connected_components.append(connected_component)
        return connected_components

    def dfs(self, start, visited, stack):
        """
        function for depth first search of a vertex
        the function will mark the start vertex as visited, add it to the stack (where it’s the final
        connected component) and the update it by recalling the function to look through all the adjacent
        vertices to the vertex start
        :param start: the vertex from where we start searching
        :param visited: the list of the visited vertices
        :param stack: the list that will store the connected component of a certain vertex
        :return: visited, stack
        """
        if start in visited:
            return visited, stack
        visited.append(start)
        stack.append(start)
        for node in self._edges[start]:
            visited, path = self.dfs(node, visited, stack)
        return visited, stack


