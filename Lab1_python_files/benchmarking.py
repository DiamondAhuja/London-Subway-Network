from random import random
from dijkstra import *
import timeit, random, csv
import matplotlib.pyplot as plt


def run_dijkstra(graph):
    start_node = random.randint(1, len(graph.get_vertices()))
    end_node = random.randint(1, len(graph.get_vertices()))
    start = timeit.timeit()
    p, s = dijkstra_algorithm(graph, str(start_node))
    path, time = print_result(p, s, str(start_node), str(end_node))
    end = timeit.timeit()
    elapsed_time = end - start
    if len(path) - 2 < 0:
        nodes_between = 0
    else:
        nodes_between = len(list(path)) - 2

    return float(elapsed_time), int(nodes_between)


def dijkstra_iterations(graph):
    TESTS = 10
    header = ['Runtime', 'Nodes_Visited']
    with open('dijkstra_benchmark.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # writer.writerow(header)
        for i in range(TESTS):
            time, nodes = run_dijkstra(graph)
            writer.writerow([time, nodes])


def create_plot():
    x = []
    y = []

    with open('dijkstra_benchmark.csv', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            y.append(float(row[0]))
            x.append(int(row[1]))

    plt.plot(x, y, color='g', linestyle='solid',
            marker='o', label="Dijkstra Algorithm")

    plt.xticks(rotation=25)
    plt.xlabel('Number of Stations Visited')
    plt.ylabel('Runtime')
    plt.title('Dijkstra Algorithm Benchmark', fontsize=20)
    plt.grid()
    plt.legend()
    plt.show()
