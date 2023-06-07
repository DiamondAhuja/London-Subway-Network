from math import *
from aStar import find_all_paths
from graph_structure import *


class Itinerary:
    def __init__(self, station1, station2, graph):
        self.station1 = station1
        self.station2 = station2
        self.graph = graph
    
    def all_paths(self):
        paths = find_all_paths(self.graph.dict(), self.station1.get_id(), self.station2.get_id(), [])
        return paths

    def path_time(self, path):
        if len(path) <= 1:
            return
        total_time = 0
        graph = self.graph.dict()
        for i in range(len(path) - 1):
            j = i + 1
            curr_start = path[i]
            curr_dest = path[j]
            neighbours = graph[curr_start]
            total_time += neighbours[curr_dest]
        return total_time
    
    def path_stops(self, path):
        return len(path) - 1
            
    def best_path(self):
        paths = self.all_paths()
        if len(paths) == 0:
            return
        best_path = paths[0]
        times = []
        stops = []
        distances = []

        for i in range(len(paths)):
            times.append(self.path_time(paths[i]))
            stops.append(self.path_stops(paths[i]))
        
        for j in range(len(paths) - 1):
            for k in range(1, len(paths)):
                if times[k] == times[j]:
                    if stops[k] < stops[j]:
                        best_path = paths[k]
                    else:
                        best_path = paths[j]
                elif times[k] < times[j]:
                    best_path = paths[k]
                else:
                    best_path = paths[j]
        return best_path
                





