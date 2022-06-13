from importlib.resources import contents
from multiprocessing import context
import queue

heuristicValue={'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 
'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu_Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

context=""

# getting Straight Length from user
def straightLength(hM):
    global heuristicValue
    h = {}
    for line in hM.split('\n'):
        line = line.strip().split("-")
        node = line[0].strip()
        sld = int(line[1].strip())
        h[node] = sld
    heuristicValue=h
    return h



# creating country map from user
def addCountry(map):
    graph = {}
    for string in map.split('\n'):
        node_val = string.split('-')

        if node_val[0] in graph and node_val[1] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})

            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})

        elif node_val[0] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})

            graph[node_val[1]] = [[node_val[0], node_val[2]]]

        elif node_val[1] in graph:
            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})

            graph[node_val[0]] = [[node_val[1], node_val[2]]]

        else:
            graph[node_val[0]] = [[node_val[1], node_val[2]]]
            graph[node_val[1]] = [[node_val[0], node_val[2]]]

    return graph


# Astar Algorithm
def Astar(startNode, heuristics, graph, goalNode):
    global context
    priorityQueue = queue.PriorityQueue()
    distance = 0
    path = []

    priorityQueue.put((heuristics[startNode] + distance, [startNode, 0]))

    while priorityQueue.empty() == False:
        current = priorityQueue.get()[1]
        path.append(current[0])
        distance += int(current[1])

        if current[0] == goalNode:
            break

        priorityQueue = queue.PriorityQueue()

        for i in graph[current[0]]:
            if i[0] not in path:
                priorityQueue.put((heuristics[i[0]] + int(i[1]) + distance, i))
    context+="Cost : "
    context+=str(distance)+"\n"
    return path



# running the program
def searchFunction(citySource, cityGoal="Bucharest"):
    global context
    context=""
    heuristic = heuristicValue
    graph = romania
    if citySource not in graph:
        context= 'CITY NOT ON MAP.'
        print ('CITY NOT ON MAP.')
        return context
    # print(graph)
    astar = Astar(citySource, heuristic, graph, cityGoal)
    context+="ASTAR => "+" => ".join(astar)
    return context


def storeFunction(map,h):
    # Fetch global variables
    global romania
    global heuristicValue
    try:
        romania={}
        # intialize romania dictionary
        romania= addCountry(map)
        # intialize heuristiv values
        heuristicValue=straightLength(h)
        return "NEW MAP SAVED"
    except:
        return "Data Error"


romania={'Arad': [['Sibiu', '140'], ['Timisoara', '118'], ['Zerind', '75']], 'Sibiu': [['Arad', 
'140'], ['Fagaras', '99'], ['Oradea', '151'], ['Rimnicu_Vilcea', '80']], 'Timisoara': [['Arad', '118'], ['Lugoj', '111']], 'Zerind': [['Arad', '75'], ['Oradea', '71']], 'Bucharest': [['Fagaras', '211'], ['Giurgiu', '90'], ['Pitesti', '101'], ['Urziceni', '85']], 'Fagaras': [['Bucharest', '211'], ['Sibiu', '99']], 'Giurgiu': [['Bucharest', '90']], 'Pitesti': [['Bucharest', '101'], ['Craiova', '138'], ['Rimnicu_Vilcea', '97']], 'Urziceni': [['Bucharest', '85'], ['Hirsova', '98'], ['Vaslui', '142']], 'Craiova': [['Dobreta', '120'], ['Pitesti', '138'], ['Rimnicu_Vilcea', '146']], 'Dobreta': [['Craiova', '120'], ['Mehadia', '75']], 'Rimnicu_Vilcea': [['Craiova', '146'], ['Pitesti', '97'], ['Sibiu', '80']], 'Mehadia': [['Dobreta', '75'], ['Lugoj', '70']], 'Eforie': [['Hirsova', '86']], 'Hirsova': [['Eforie', '86'], ['Urziceni', '98']], 'Iasi': [['Neamt', '87'], ['Vaslui', '92']], 'Neamt': [['Iasi', '87']], 'Vaslui': [['Iasi', '92'], ['Urziceni', '142']], 'Lugoj': [['Mehadia', '70'], ['Timisoara', '111']], 'Oradea': [['Zerind', '71'], ['Sibiu', '151']]}