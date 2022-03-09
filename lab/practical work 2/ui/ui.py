from graph.undirectedgraph import UndirectedGraph, UndirectedGraphException
from utils.external_functions import read_graph_from_file


class UI:
    def __init__(self):
        self._graph = UndirectedGraph(0)
        self._commands = {
            "1": self._number_of_vertices_ui,
            "2": self._parse_the_set_of_vertices_ui,
            "3": self._add_edge_ui,
            "4": self._remove_edge_ui,
            "5": self._add_vertex_ui,
            "6": self._remove_vertex_ui,
            "7": self._read_graph_from_file_ui,
            "8": self._connected_components_ui
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
        print("──────────────────────────────────────────────────────────────────────────────")
        print("|  3 | add edge                                                              |")
        print("|  4 | remove edge                                                           |")
        print("|  5 | add vertex                                                            |")
        print("|  6 | remove vertex                                                         |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("|  7 | read the graph from a text file                                       |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("|  8 | get the connected components of the graph                             |")
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

    def _add_edge_ui(self):
        vertex_1 = int(input("\n• give the first vertex: "))
        vertex_2 = int(input("\n• give the second vertex: "))
        self._graph.add_edge(vertex_1, vertex_2)
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

    def _connected_components_ui(self):
        connected_components = self._graph.connected_components()
        no_of_cc = len(connected_components)
        print("\nthere are", no_of_cc, "connected components in the graph.\n")
        for i in range(0, len(connected_components)):
            print("component", i + 1, ": ", connected_components[i])

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
                except UndirectedGraphException as ge:
                    print("\n", ge)
            else:
                print("\n• bad command! try another one.")
