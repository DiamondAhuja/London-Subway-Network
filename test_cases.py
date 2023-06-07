from data_extraction import *
from graph_maker import *
from pathFinding import *
import pytest

#Make Graph
data = dataExtraction()

#Update Path
path = r"C:\Users\saads\l1-graph-lab\_dataset\london.connections.csv"

graph = Graph(data.extract(path))
graph.makeGraph()

#### Start Graph Tests ####

#Function to test if graph has right avg degree #
def degAverageCheck():
    return graph.degAverage()

#Function to test if graph has right # of edges
def edgeCounterCheck():
    return graph.edgeCounter()

#Function to test if graph has right the right nodes
def nodelistCheck():
    return graph.nodelist

def test_degAverageCheck():
    assert degAverageCheck() == 2.689

def test_edgeCounterCheck():
    assert edgeCounterCheck() == 406

def test_nodelistCheck():
    nodeList = []
    for i in range(1, 304):
        if (i != 189):
            nodeList.append(i)
    a = nodelistCheck()
    a.sort()
    assert a == nodeList

#### End Graph Tests ####

#### Start AStar Test Cases ####

a = aStar(graph)

### Random AStar Node Tests ###
def aStarToNode193():
    return a.aStar(11, 193)

def test_aStarToNode193():
    assert [11, 163, 82, 193] == aStarToNode193()

def aStarToNode13():
    return a.aStar(11, 13)

def test_aStarToNode13():
    assert [11, 28, 192, 259, 126, 48, 250, 13] == aStarToNode13()

### End Random AStar Node Tests ###

### Return start Node Start ###
#Start node to start node
def aStartToStart11():
    return a.aStar(11,11)

def aStartToStart116():
    return a.aStar(116,116)

def test_aStartToStart11():
    assert [11] == aStartToStart11()

def test_aStartToStart116():
    assert [116] == aStartToStart116()

### Return start Node End ###

### No Existing Node Test Start ###
#No exisitng ending Node
def aStartToStart189():
    return a.aStar(11,189)

def aStartToStart400():
    return a.aStar(11,400)

#No existing Starting Node
def aStartToStartS():
    return a.aStar(400,23)

#No existing Starting and ending Node
def aStartToStartSE():
    return a.aStar(400,432)

def test_aStartToStart189():
    assert None == aStartToStart189()

def test_aStartToStart400():
    assert None == aStartToStart400()

def test_aStartToStartS():
    assert None == aStartToStartS()

def test_aStartToStartSE():
    assert None == aStartToStartSE()

### No Existing Node Test End ###

#### End AStar Test Cases ####

#### Start Dijkstra Test Cases ####

d = dijk(graph)

### Start Radom Node Test ###
def dijkFrom73():
    return d.dijkstra(73)

# 73 -> 1 -> 52 (total cost 4)
def test_dijkFrom73():
    assert 4 == dijkFrom73()[52]

# 73 -> 72 -> 286 (total cost 7)
def test_dijkFrom73():
    assert 7 == dijkFrom73()[286]
### End Radom Node Test ###

### Start Return 0 Test ###
def dijkFrom94():
    return d.dijkstra(94)

def test_dijkFrom94():
    assert 0 == dijkFrom94()[94]

def dijkFrom194():
    return d.dijkstra(194)

def test_dijkFrom194():
    assert 0 == dijkFrom194()[194]
### End Return 0 Test ###

### Start Non-exist Node Test ###
def dijkFrom189():
    return d.dijkstra(189)

def test_dijkFrom189():
    assert float('inf') == dijkFrom189()[11]

def dijkFrom402():
    return d.dijkstra(402)

def test_dijkFrom402():
    assert float('inf') == dijkFrom402()[11]
### End Non-exist Node Test ###

#### End Dijkstra Testing ####