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
        self._in_neighbours = {}
        self._out_neighbours = {}
        for i in range(0, n):
            self._in_neighbours[i] = []
            self._out_neighbours[i] = []
        self._costs = {}
        self._isolated = []

    def add_isolated_vertex(self, vertex):
        """
        function that adds a vertex to the isolated vertices
        :param vertex: the isolated vertex
        :return: -
        """
        self._isolated.append(vertex)

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
        return len(self._costs)

    def get_all_costs(self):
        """
        getter for the costs of the graph ((vertex_1, vertex_2) with cost)
        :return: costs of the graph
        """
        return self._costs

    def get_all_isolated(self):
        """
        getter for the isolated vertices
        :return: the isolated vertices
        """
        return self._isolated

    def valid_vertex(self, vertex):
        """
        function that validates a vertex before getting its in/out edges
        :param vertex: the vertex to be validated
        :return: vertex
        """
        return vertex in self._out_neighbours

    def get_in_degree(self, vertex):
        """
        getter for the in degree of an vertex
        :param vertex: the vertex
        :return: the in degree of the vertex
        """
        try:
            return len(self._in_neighbours[vertex])
        except KeyError:
            raise GraphException("\n• invalid vertex!")

    def get_out_degree(self, vertex):
        """
        getter for the out degree of an vertex
        :param vertex: the vertex
        :return: the out degree of the vertex
        """
        try:
            return len(self._out_neighbours[vertex])
        except KeyError:
            raise GraphException("\n• invalid vertex!")

    def get_in_edges(self, vertex):
        """
        getter for the in edges of an vertex
        :param vertex: the vertex
        :return: the in edges of the vertex
        :precondition: the vertex exists
        """
        if not self.valid_vertex(vertex):
            return GraphException("\n• invalid vertex!\n")
        for v in self._in_neighbours[vertex]:
            yield v

    def get_out_edges(self, vertex):
        """
        getter for the out edges of an vertex
        :param vertex: the vertex
        :return: the out edges of the vertex
        :precondition: the vertex exists
        """
        if not self.valid_vertex(vertex):
            return GraphException("\n• invalid vertex!\n")
        for v in self._out_neighbours[vertex]:
            yield v

    def get_cost_edge(self, vertex_1, vertex_2):
        """
        getter for the cost between two vertices
        :param vertex_1: the vertex from where the edge starts
        :param vertex_2: the vertex where the edge ends
        :return: -
        :precondition: • check if the edge exists
        """
        if self.check_edge_in_costs(vertex_1, vertex_2) is False:
            raise GraphException("\n• can't get the cost of an inexistent edge!\n")
        return self._costs[(vertex_1, vertex_2)]

    def set_cost_edge(self, vertex_1, vertex_2, new_cost):
        """
        setter for the cost between two vertices
        :param vertex_1: the vertex from where the edge starts
        :param vertex_2: the vertex where the edge ends
        :param new_cost: the new cost for the edge
        :return:
        :precondition: • check if the edge exists
        """
        if self.check_edge_in_costs(vertex_1, vertex_2) is False:
            raise GraphException("\n• can't set the cost of an inexistent edge!\n")
        self._costs[(vertex_1, vertex_2)] = new_cost

    def parse_vertices_of_the_graph(self):
        for v in self._out_neighbours:
            yield v

    def is_edge(self, vertex_1, vertex_2):
        """
        function that checks if between vertex_1 and vertex_2 there is an edge
        :param vertex_1: the vertex from where the edge starts
        :param vertex_2: the vertex where the edge ends
        :return: the edge
        :precondition: check if vertex_1 and vertex_2 exist
        """
        if vertex_1 not in self._in_neighbours and vertex_2 not in self._out_neighbours:
            return GraphException("\n• invalid vertices!\n")
        try:
            return vertex_2 in self._out_neighbours[vertex_1]
        except KeyError as error:
            raise GraphException("\n• no edge between the two vertices!")

    def check_edge_in_costs(self, vertex_1, vertex_2):
        """
        function used for validating the parameters when adding, removing, getting/modifying the cost of an edge
        :param vertex_1: the vertex from where the edge starts
        :param vertex_2: the vertex where the edge ends
        :return: True - if the edge exists
                 False - otherwise
        """
        if (vertex_1, vertex_2) in self._costs.keys():
            return True
        return False

    def add_edge(self, vertex_1, vertex_2, cost):
        """
        function that adds an edge between two vertices
        :param vertex_1: the vertex from where the edge starts
        :param vertex_2: the vertex where the edge ends
        :param cost: the cost of the edge between the two vertices
        :return: -
        :precondition: • check if the edge exists
                       • edge can't be between the same vertex
        """
        if self.check_edge_in_costs(vertex_1, vertex_2) is True:
            raise GraphException("• the edge already exists! cannot add it twice!\n")

        if vertex_1 in self._isolated:
            self._isolated.remove(vertex_1)
        if vertex_2 in self._isolated:
            self._isolated.remove(vertex_2)

        self._in_neighbours[vertex_2].append(vertex_1)
        self._out_neighbours[vertex_1].append(vertex_2)
        self._costs[(vertex_1, vertex_2)] = cost

    def remove_edge(self, vertex_1, vertex_2):
        """
        function that removes an edge between two vertices
        :param vertex_1: the vertex from where the edge starts
        :param vertex_2: the vertex where the edge ends
        :return: -
        :precondition: • check if the edge exists
        """
        if self.check_edge_in_costs(vertex_1, vertex_2) is False:
            raise GraphException("• cannot remove an edge that doesn't exist!\n")

        self._in_neighbours[vertex_2].remove(vertex_1)
        self._out_neighbours[vertex_1].remove(vertex_2)
        del self._costs[(vertex_1, vertex_2)]
        if self.get_in_degree(vertex_1) == 0 and self.get_out_degree(vertex_1) == 0:
            self._isolated.append(vertex_1)
        if self.get_in_degree(vertex_2) == 0 and self.get_out_degree(vertex_2) == 0:
            self._isolated.append(vertex_1)

    def valid_vertex_add_vertex(self, vertex):
        """
        function that validates the parameter before adding it
        :param vertex: the vertex to be verified
        :return: True - if vertex is in the in neghbours
                 False - otherwise
        """
        if vertex in self._in_neighbours.keys():
            return True
        return False

    def add_vertex(self, vertex):
        """
        function that adds a new vertex
        :param vertex: the new vertex to be added
        :return: -
        :precondition: • check if the vertex exists
        """
        if self.valid_vertex_add_vertex(vertex) is True:
            raise GraphException("• the vertex already exists! cannot add it twice!\n")

        self._isolated.append(vertex)
        self._in_neighbours[vertex] = []
        self._out_neighbours[vertex] = []
        self._vertices = self._vertices + 1

    def remove_vertex(self, vertex):
        """
        function that removes a vertex
        :param vertex: the new vertex to be removed
        :return: -
        :precondition: • check if the vertex exists

        • the function checks the in neighbours and removes vertex if vertex is a succesor of v
        • the function checks the in neighbours and removes vertex if vertex is a predecesor of v
        • additionally, it checks if after removing vertex, v would be isolated
        """
        if vertex not in self.parse_vertices_of_the_graph():
            raise GraphException("• cannot remove a vertex that doesn't exist!\n")

        if vertex in self._isolated:
            self._isolated.remove(vertex)

        for v in self._in_neighbours[vertex]:
            self._out_neighbours[v].remove(vertex)
            del self._costs[(v, vertex)]
            if self.get_in_degree(v) == 0 and self.get_out_degree(v) == 0:
                self._isolated.append(v)
        del self._in_neighbours[vertex]

        for v in self._out_neighbours[vertex]:
            self._in_neighbours[v].remove(vertex)
            del self._costs[(vertex, v)]
            if self.get_in_degree(v) == 0 and self.get_out_degree(v) == 0:
                self._isolated.append(v)
        del self._out_neighbours[vertex]
        self._vertices = self._vertices - 1
