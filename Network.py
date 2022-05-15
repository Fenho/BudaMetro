class ColoredNetwork:
    '''
    This network depends on the train color.
    This means that the nodes that are not the train's color or no color,
    are ignored, and new connections with the ignored station's
    children are added (if a child of an ignored station is also
    of an unfit color, it will also be ignored).
    '''
    def __init__(self, nodes, color=''):
        self.graph = {}
        self.nodes = nodes
        self.train_color = color

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].add(vertex2)
        self.graph[vertex2].add(vertex1)

    def add_all_vertex(self, nodes):
        for node in nodes:
            self.add_vertex(node.name)

    def connect_to_neighbors(self, parent, vertex1):
        for connection in parent.connections:
            connection_node = self.get_node(connection)
            if (connection_node.color == self.train_color
                or connection_node.color == ''
                or self.train_color == ''):
                self.add_edge(vertex1.name, connection_node.name)
            else:
                # Ignore station that is not train's color or no color
                self.connect_to_neighbors(connection_node, vertex1)

    def add_all_edges(self, nodes):
        for node in nodes:
            self.connect_to_neighbors(node, node)

    def print_graph(self):
        for key in self.graph:
            print(key, ":", self.graph[key])

    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

    def bfs(self, start, end):
        '''
        start: string
        end: string
        '''
        visited = []
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            vertex = self.get_node(path[-1])
            if (vertex not in visited):
                visited.append(vertex)
                for neighbour in self.graph[vertex]:
                    new_path = path.copy()
                    if vertex.name == end:
                        return new_path
                    new_path.append(neighbour)
                    queue.append(new_path)
        return -1