from queue import PriorityQueue
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

    def mst_prim(self, v):
        """
        function that constructs the mst using prim's algorithm and the total cost
        :return: the mst and the minimum cost

        basic idea of the implementation / algoritm:
        • mst_visited - will help in checking if a certain vertex was already added to the mst
        • dist - will be initialised to have the max size (infinty) for all vertices, the root will have value 0
        • until we haven't visited all the vertices yet (mst_visited should have all the vertices)
            • try to choose a min_vertex with a minimum dist value and isn't in mst_visited
            • add it to mst_visited
            • all the vertices (vertex) adjacent to min_index will be updated, if the edge (min_vertex, vertex)
              will have a smaller cost than the one in the dist list and were not added yet to the mst
        • in the end
            • edges will contain on the [0] and [1] positions the edge, on position [2] the cost
            • mst_total_cost will have the total cost of the mst
        """
        # dist will help choosing the minimum cost
        dist = [sys.maxsize] * self._vertices
        # edges will contain the constructed mst (a collection of edges, forming a minimum cost spanning tree)
        prev = [0] * self._vertices
        # a set to know if an edge was visited
        mst_visited = [False] * self._vertices

        # v was chosen arbitrarily as the root
        dist[v] = 0
        prev[v] = -1

        # a tree has no. of vertices edges (since indexing starts from 0)
        for i in range(0, self._vertices):
            # now choose the minimum distance from the vertices that weren't added to the mst yet
            minimum = sys.maxsize
            min_vertex = 0
            for vertex in range(0, self._vertices):
                # if a distance smaller that minimum was encountered,the vertex wasn't added to the mst
                # update minimum and the vertex with the minimum distance was found (min_vertex)
                if dist[vertex] < minimum and mst_visited[vertex] is False:
                    minimum = dist[vertex]
                    min_vertex = vertex

            # the vertex with the minimum distance was found and update the set of processed vertices
            mst_visited[min_vertex] = True
            # now the dist value will be updated in case the cost of the min_vertex and adjacent vertex
            # will have a smaller value than the current value in dist
            # and if the vertex was not added yet to the mst
            for vertex in range(0, self._vertices):
                # if the edge is valid
                if (min_vertex, vertex) in self._costs:
                    # check if vertex wasn't added yet to the mst
                    # update the dist only if the cost between (min_vertex, vertex) is smaller than dist[vertex]
                    if self._costs[(min_vertex, vertex)] < dist[vertex] and mst_visited[vertex] is False:
                        dist[vertex] = self._costs[(min_vertex, vertex)]
                        prev[vertex] = min_vertex

        # in edges we will store mst consisting of the edges between prev[i], i
        # on positions [0] and [1], and on [2] the cost of that edge
        edges = []
        # in mst_total_cost, it'll be the final cost of the mst
        mst_total_cost = 0
        for i in range(0, self._vertices):
            if (i, prev[i]) in self._costs:
                mst_total_cost = mst_total_cost + self._costs[(i, prev[i])]
                edges.append([prev[i], i, self._costs[(i, prev[i])]])

        return edges, mst_total_cost
