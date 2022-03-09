import sys


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
        self._costs = {}
        for i in range(0, n):
            self._edges[i] = []

    def get_number_of_vertices(self):
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
        return len(self._costs)

    def get_all_costs(self):
        """
        getter for the costs of the graph ((vertex_1, vertex_2) with cost)
        :return: costs of the graph
        """
        return self._costs

    def get_all_edges(self):
        """
        getter for the costs of the graph ((vertex_1, vertex_2) with cost)
        :return: costs of the graph
        """
        return self._edges

    def add_edge(self, vertex_1, vertex_2, cost):
        """
        function that adds an edge between two vertices
        :param vertex_1: the vertex from where the edge starts
        :param vertex_2: the vertex where the edge ends
        :param cost: the cost of the edge vertex_1 - vertex_2
        :return: -
        """
        if vertex_1 in self._edges[vertex_2]:
            raise UndirectedGraphException("\n• edge " + str(vertex_1) + "-" + str(vertex_2) + "already exists!\n")
        if vertex_2 in self._edges[vertex_1]:
            raise UndirectedGraphException("\n• edge " + str(vertex_1) + "-" + str(vertex_2) + "already exists!\n")
        self._edges[vertex_1].append(vertex_2)
        self._edges[vertex_2].append(vertex_1)
        self._costs[(vertex_1, vertex_2)] = cost
        self._costs[(vertex_2, vertex_1)] = cost

    def remove_edge(self, vertex_1, vertex_2):
        """
        function that removes an edge between two vertices
        :param vertex_1: the vertex from where the edge starts
        :param vertex_2: the vertex where the edge ends
        :return: -
        :precondition: • check if the edge exists
        """
        if vertex_1 in self._edges[vertex_2]:
            raise UndirectedGraphException("\n• edge " + str(vertex_1) + "-" + str(vertex_2) + "already exists!\n")
        if vertex_2 in self._edges[vertex_1]:
            raise UndirectedGraphException("\n• edge " + str(vertex_1) + "-" + str(vertex_2) + "already exists!\n")

        if vertex_1 in self._edges[vertex_2] and vertex_2 in self._edges[vertex_1]:
            self._edges[vertex_1].remove(vertex_2)
            self._edges[vertex_2].remove(vertex_1)
        del self._costs[(vertex_1, vertex_2)]
        del self._costs[(vertex_2, vertex_1)]

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
        self._vertices = self._vertices + 1

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
            del self._costs[(vertex, v)]
            del self._costs[(v, vertex)]
        self._edges.pop(vertex)
        self._vertices = self._vertices - 1

    def parse_vertices_of_the_graph(self):
        """
        function that will parse through all the vertices of the graph
        :return: the vertices
        """
        for v in self._edges:
            yield v

    def vertex_colouring(self):
        """
        function that returns the vertices with the minimum colouring
        :return: the vertices with the minimum colouring

        the idea of it:
        • mark the first vertex (vertex 0) with the "colour" 1
        • for the next vertices:
            • the current vertex will be marked with the lowest "colour" k that wasn't used for any
              adjacent vertices to the current vertex
            • in case all previous colours are marked on the vertices adjacent to the current vertex,
              mark a new "colour" k to it
        """
        # in colouring, we will store the "colour" k (1, 2, ..., k) corresponding to each vertex
        # initially, all vertices will have value -1, then we mark vertex 0 with the "colour" 1
        colouring = [-1] * self._vertices
        colouring[0] = 1

        # visited will be updated for each iteration with false for all it's values
        # it will help when we iterate each time to know which vertices were already coloured
        visited = [False] * self._vertices

        for vertex in range(1, self._vertices):
            # check each adjacent node i to vertex
            for i in self._edges[vertex]:
                # if the value in colouring is not the one we initialised it with, that means it was coloured
                # therefore we mark visited with true (since the colouring is from 1,
                # the value of visited[colour - 1] would mean that colour - 1 is marked to one of its adjacent vertices)
                if colouring[i] != -1:
                    visited[colouring[i] - 1] = True

            # assigning the colour to the vertex
            k = 1
            while k < self._vertices:
                if visited[k - 1] is False:
                    break
                k = k + 1
            colouring[vertex] = k

            # visited will be reset to false for the next iteration
            for i in self._edges[vertex]:
                if colouring[i] != -1:
                    visited[colouring[i] - 1] = False

        return colouring
