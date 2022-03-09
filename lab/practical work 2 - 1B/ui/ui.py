from graph.graph import Graph, GraphException
from utils.external_functions import read_graph_from_file


class UI:
    def __init__(self):
        self._graph = Graph(0)
        self._commands = {
            "1": self._number_of_vertices_ui,
            "2": self._parse_the_set_of_vertices_ui,
            "3": self._strongly_connected_components_ui,
            "4": self._read_graph_from_file_ui,
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
        print("|  3 | strongly connected components                                         |")
        print("──────────────────────────────────────────────────────────────────────────────")
        print("|  4 | read the graph from a text file                                       |")
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

    def _strongly_connected_components_ui(self):
        strongly_connected_components = list(self._graph.strongly_connected())
        comp = 1
        for i in range(0, len(strongly_connected_components)):
            print("component", comp, ":", strongly_connected_components[i])
            comp = comp + 1

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
