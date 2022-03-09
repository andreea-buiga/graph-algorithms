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
        except KeyError:
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

    def dijkstra(self, start_vertex, target_vertex):
        """
        function that uses dijkstra's algorithm in order to find the lowest cost walk
        :param start_vertex: the vertex we start from
        :param target_vertex: the vertex we want to reach
        :return: lowest cost walk from start_vertex to target_vertex

        • the algorithm has a dictionary that stores the prevoius vertex and the cost, we mark the current vertex
        as the start vertex given as a parameter, and a set of visited vertices
        • until we do not reach the target vertex, we'll go through the out neighbours of the current vertex
        and mark the current vertex as visted
        • we parse the out neighbours and add the cost value from the current vertex and next vertex (next vertex is
        one of the out neighbours of the current vertex)
        • we add it to the lowest walks in case it wasn't visited before, otherwise we'll make sure if the value of the
        cost would be minimal, because in that case we'll need to update the tuple (previous vertex, cost), to the
        with the current vertex and the cost we have so far
        • we move to the next vertex that has been not visited yet
        • if we didn't reach the destination and the next targets in the lowest walks all have been visited, we
        will not have a walk between start_vertex and target_vertex
        • we change the value of the current vertex such that it will have the lowest cost
        • since lowest walks will have the values backwards, we'll need to reverse the final lowest cost walk
        """
        # lowest_walks is a dictionary that stores a tuple consisting of (previous vertex, cost)
        lowest_walks = {start_vertex: (None, 0)}
        current_vertex = start_vertex
        visited = set()

        # we keep looking until we reach the target_vertex
        while current_vertex != target_vertex:
            # mark the vertex as visted
            visited.add(current_vertex)
            # we'll try to parse the out neighbours of the current vertex
            # if we'll have a Key Error we throw an exception
            # (in case the start_vertex would be inexistent in the out_neighbours)
            try:
                targets = self._out_neighbours[current_vertex]
            except KeyError:
                raise GraphException("\n• cannot find a walk between start vertex and target vertex!\n")
            # get the current cost of the current vertex
            cost_current_vertex = lowest_walks[current_vertex][1]
            # go through each out neighbour
            for next_vertex in targets:
                # add the cost of the next vertex to the cost
                cost = self._costs[(current_vertex, next_vertex)] + cost_current_vertex
                # add next_vertex if the vertex in the targets was not added to the lowest walks
                if next_vertex not in lowest_walks:
                    lowest_walks[next_vertex] = (current_vertex, cost)
                else:
                    # if the vertex already exists in the lowest walks we check if the cost has a lower value
                    # than the current cost of the walk
                    current_minimal_cost = lowest_walks[next_vertex][1]
                    if current_minimal_cost > cost:
                        lowest_walks[next_vertex] = (current_vertex, cost)
            # we choose the next targets such that those vertices were not visited already
            next_targets = {v: lowest_walks[v] for v in lowest_walks if v not in visited}
            # the target is not met, and all the vertices in the lowest walks have been visted, we don't have a walk
            if not next_targets:
                raise GraphException("\n• cannot find a walk between start vertex and target vertex!\n")
            # change the value of the current vertex, such that the new vertex is the destination
            # having the lowest cost
            current_vertex = min(next_targets, key=lambda v: next_targets[v][1])

        # building the lowest cost walk
        lowest_cost_walk = []
        while current_vertex is not None:
            lowest_cost_walk.append(current_vertex)
            next_vertex = lowest_walks[current_vertex][0]
            current_vertex = next_vertex
        # as we go backwards though this, it'll be the lowest cost walk from start_vertex to target_vertex
        # reverse it
        lowest_cost_walk = lowest_cost_walk[::-1]

        return lowest_cost_walk, lowest_walks[target_vertex][1]
