class Station:
    def __init__(self, name, connections, color=None):
        self.name = name
        self.connections = connections # List of stations connected to this one
        self.color = color # None, red, green

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return hash(self.name)