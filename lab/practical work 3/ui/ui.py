from graph.graph import Graph, GraphException
from utils.external_functions import read_graph_from_file, write_graph_to_file, create_random_graph
from copy import deepcopy


class UI:
    def __init__(self):
        self._graph = Graph(0)
        self._graph_copy_list = []
        self._graph_copy = Graph(0)
        self._commands = {
            "1": self._number_of_vertices_ui,
            "2": self._parse_the_set_of_vertices_ui,
            "3": self._exists_edge_between_two_vertices_ui,
            "4": self._in_and_out_degree_ui,
            "5": self.parse_outbound_edges_of_vertex_ui,
            "6": self.parse_inbound_edges_of_vertex_ui,
            "7": self._get_endpoints_of_edge_specified_ui,
            "8": self._modify_information_attached_to_edge_ui,
            "9": self._add_edge_ui,
            "10": self._remove_edge_ui,
            "11": self._add_vertex_ui,
            "12": self._remove_vertex_ui,
            "13": self._create_copy_of_graph,
            "14": self._read_graph_from_file_ui,
            "15": self._write_graph_from_file_ui,
            "16": self._create_random_graph_ui,
            "17": self._lowest_cost_walk_dijkstra_ui
        }

    @staticmethod
    def _print_menu_ui():
        print("──────────────────────────────────────────────────────────────────────────────")
        print("|                                                                | – | □ | x |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("|                           • G R A P H  M E N U •                           |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("|  1 | get the number of vertices                                            |")
        print("|  2 | parse (iterate) the set of vertices                                   |")
        print("|  3 | given two vertices, find out whether there is an edge from the first  |")
        print("|    | one to the second one                                                 |")
        print("|  4 | get the in degree and the out degree of a specified vertex            |")
        print("|  5 | parse (iterate) the set of outbound edges of a specified vertex       |")
        print("|  6 | parse the set of inbound edges of a specified vertex                  |")
        print("|  7 | get the endpoints of an edge specified                                |")
        print("|  8 | retrieve or modify the information attached to a specified edge       |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("|  9 | add edge                                                              |")
        print("| 10 | remove edge                                                           |")
        print("| 11 | add vertex                                                            |")
        print("| 12 | remove vertex                                                         |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("| 13 | make an exact copy of the graph                                       |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("| 14 | read the graph from a text file                                       |")
        print("| 15 | write the graph from a text file                                      |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("| 16 | create a random graph with specified number of vertices and of edges  |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("| 17 | finds a lowest cost walk between two given vertices                   |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("|  0 | exit                                                                  |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("\n")

    def _number_of_vertices_ui(self):
        print("\n• the number of vertices: ", self._graph.get_number_of_verteces())

    def _parse_the_set_of_vertices_ui(self):
        all_vertices = self._graph.parse_vertices_of_the_graph()
        print("\nall the vertices of the graph:\n")
        for v in all_vertices:
            print("vertex:", v)

    def _exists_edge_between_two_vertices_ui(self):
        vertex_1 = int(input("\n• give the first vertex: "))
        vertex_2 = int(input("\n• give the second vertex: "))
        if self._graph.is_edge(vertex_1, vertex_2):
            print("\n• yes there is an edge between", vertex_1, "and", vertex_2)
        else:
            print("\n• no edge between", vertex_1, "and", vertex_2)

    def _in_and_out_degree_ui(self):
        vertex = int(input("\n• give vertex: "))
        in_degree = self._graph.get_in_degree(vertex)
        out_degree = self._graph.get_out_degree(vertex)
        print("\n• in degree of", vertex, ": ", in_degree)
        print("\n• out degree of", vertex, ": ", out_degree)

    def parse_outbound_edges_of_vertex_ui(self):
        vertex_1 = int(input("\n• give vertex: "))
        isolated = self._graph.get_all_isolated()
        if vertex_1 in isolated:
            print("\n• vertex", vertex_1, "is isolated!\n")
            return
        outbound_edges = self._graph.get_out_edges(vertex_1)
        print("\n• outbound edges for vertex", vertex_1)
        for vertex_2 in outbound_edges:
            cost = self._graph.get_cost_edge(vertex_1, vertex_2)
            print("• the edge", vertex_1, "-", vertex_2, "has the cost:", cost)

    def parse_inbound_edges_of_vertex_ui(self):
        vertex_2 = int(input("\n• give vertex: "))
        isolated = self._graph.get_all_isolated()
        if vertex_2 in isolated:
            print("\n• vertex", vertex_2, "is isolated!\n")
            return
        inbound_edges = self._graph.get_in_edges(vertex_2)
        print("\n• inbound edges for vertex", vertex_2)
        for vertex_1 in inbound_edges:
            cost = self._graph.get_cost_edge(vertex_1, vertex_2)
            print("• the edge", vertex_1, "-", vertex_2, "has the cost:", cost)

    def _get_endpoints_of_edge_specified_ui(self):
        vertex_1 = int(input("\n• give the first vertex: "))
        vertex_2 = int(input("\n• give the second vertex: "))
        cost = self._graph.get_cost_edge(vertex_1, vertex_2)
        print("\n• the edge", vertex_1, "-", vertex_2, "has the cost:", cost)

    def _modify_information_attached_to_edge_ui(self):
        vertex_1 = int(input("\n• give the first vertex: "))
        vertex_2 = int(input("\n• give the second vertex: "))
        new_cost = int(input("\n• give the new cost: "))
        self._graph.set_cost_edge(vertex_1, vertex_2, new_cost)
        print("\n• the edge", vertex_1, "-", vertex_2, "updated its cost!")

    def _add_edge_ui(self):
        vertex_1 = int(input("\n• give the first vertex: "))
        vertex_2 = int(input("\n• give the second vertex: "))
        cost = int(input("\n• give the cost of the edge: "))
        self._graph.add_edge(vertex_1, vertex_2, cost)
        print("\n• the edge", vertex_1, "-", vertex_2, "was successully added!")

    def _remove_edge_ui(self):
        vertex_1 = int(input("\n• give the first vertex: "))
        vertex_2 = int(input("\n• give the second vertex: "))
        self._graph.remove_edge(vertex_1, vertex_2)
        print("\n• the edge", vertex_1, "-", vertex_2, "was successully removed!")

    def _add_vertex_ui(self):
        vertex = int(input("\n• give vertex you want to add: "))
        self._graph.add_vertex(vertex)
        print("\n• the vertex", vertex, "was successully added!")

    def _remove_vertex_ui(self):
        vertex = int(input("\n• give vertex you want to remove: "))
        self._graph.remove_vertex(vertex)
        print("\n• the vertex", vertex, "was successully removed!")

    def _create_copy_of_graph(self):
        self._graph_copy_list.append(deepcopy(self._graph))
        print("\n• the graph was successfully copied! check graph_copt.txt!\n")
        if len(self._graph_copy_list) == 0:
            return
        self._graph_copy = self._graph_copy_list.pop(-1)
        write_graph_to_file("graph_copy.txt", self._graph_copy)

    def _read_graph_from_file_ui(self):
        done = False
        while not done:
            filename = input("\n• please provide a file from where to read: ")
            try:
                self._graph = read_graph_from_file(filename)
                done = True
                print("\n• filename", filename, "read successfully!\n")
            except IOError:
                print("\n• please provide a valid filename!\n")

    def _write_graph_from_file_ui(self):
        done = False
        while not done:
            filename = input("\n• please provide a file where to write: ")
            try:
                write_graph_to_file(filename, self._graph)
                done = True
                print("\n• filename", filename, "written successfully!\n")
            except IOError:
                print("\n• please provide a valid filename!\n")

    def _create_random_graph_ui(self):
        number_of_vertices = int(input("\n• give the number of vertices: "))
        number_of_edges = int(input("\n• give the number of edges: "))
        if number_of_vertices ** 2 < number_of_edges:
            with open("random_graph2.txt", "w") as f:
                f.write("cannot create the graph!"
                        "\nthe number of edges provided is greater than the maximum possible!\n")
            print("\n• the number of edges provided is greater than the maximum possible!\n")
        else:
            self._graph = create_random_graph(number_of_vertices, number_of_edges)

    def _lowest_cost_walk_dijkstra_ui(self):
        vertex_1 = int(input("\n• give the start vertex: "))
        vertex_2 = int(input("\n• give the target vertex: "))
        string_walk = ""
        lowest_cost_walk, cost = self._graph.dijkstra(vertex_1, vertex_2)
        for i in range(0, len(lowest_cost_walk)):
            if i != len(lowest_cost_walk)-1:
                string_walk = string_walk + str(lowest_cost_walk[i]) + " -> "
            else:
                string_walk = string_walk + str(lowest_cost_walk[i])
        print("\nlowest cost walk between", vertex_1, "and", vertex_2, ":\n")
        print(string_walk)
        print("\nthe cost is:", cost)

    def run_graph_app(self):
        self._print_menu_ui()
        are_we_done = False
        while not are_we_done:
            command = input("\n• give a command: ")
            if command == 0:
                print("\n• thank you for using the app. arrivederci!\n")
                are_we_done = True
            elif command in self._commands:
                try:
                    self._commands[command]()
                except ValueError:
                    print("\ninvalid numerical value!\n")
                except GraphException as ge:
                    print("\n", ge)
            else:
                print("\n• bad command! try another one.")
