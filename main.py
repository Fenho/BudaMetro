import io_handler
from Network import ColoredNetwork

def make_network(nodes, color):
    network = ColoredNetwork(nodes, color)
    network.add_all_vertex(nodes)
    network.add_all_edges(nodes)
    return network

def get_shortest(network, start, end):
    visited = network.bfs(start, end)
    visited_str = '->'.join(visited)
    return visited_str

if __name__ == "__main__":
    network_descriptor = input("Ingrese el path del archivo que contiene la descripción del grafo: ")
    nodes = io_handler.network_processer(network_descriptor)
    start, end = io_handler.get_start_end(nodes)
    color = io_handler.get_color()

    network = make_network(nodes, color)

    visited_str = get_shortest(network, start, end)
    print(f"El camino más corto es:\n{visited_str}")