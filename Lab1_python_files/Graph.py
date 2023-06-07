class Graph:
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict
    
    def generate_edges(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def get_neighbours(self, key):
        values = self.graph_dict.get(key)
        return list(values.keys())

    def weight(self, vertex, neighbour):
        values = self.graph_dict.get(vertex)
        if neighbour not in values.keys():
            return 
        else:
            return values[neighbour]

    def get_vertices(self):
        return list(self.graph_dict.keys())
    
    def num_of_vertices(self):
        return len(self.graph_dict.keys())

    def num_of_edges(self):
        return len(self.generate_edges())

    def degree(self, vertex):
        connected_to = self.graph_dict.get(vertex)
        return len(connected_to.keys())

    def avg_degree(self):
        degrees = []
        for key in self.graph_dict:
            degrees.append(self.degree(key))
        return sum(degrees)/len(degrees)

    def print_dict(self):
        print(self.graph_dict)

    def dict(self):
        return(self.graph_dict)