

import heapq
from queue import PriorityQueue

# variable that hold the output string
context=""
heuristicValue={'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsowa': 151, 'Lasi': 226, 
'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

# queue that hold path from source city to distination city
class priorityQueue:
    def __init__(self):
        self.cities = []
    # add to queue
    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))
    # get from queue
    def pop(self):
        return heapq.heappop(self.cities)[1]
    # check if empty
    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)

# node class, hold city and distance
class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)

# romania map dict
romania = {}

# take input from website to store new map data
# cities are seperated with spacess and lines
# example:
# city1 city2 6
def makedict(cities):
    for string in cities.split('\n'):
        line = string.split('-')
        ct1 = line[0]
        ct2 = line[1]
        dist = int(line[2])
        romania.setdefault(ct1, []).append(ctNode(ct2, dist))
        romania.setdefault(ct2, []).append(ctNode(ct1, dist))
    return romania

# take input from website to store heurstik values
# cities are seperated with spacess and lines
# example:
# city1 6
def makehuristikdict(valuse):
    global heuristicValue
    h = {}
    for line in valuse.split('\n'):
        line = line.strip().split("-")
        node = line[0].strip()
        sld = int(line[1].strip())
        h[node] = sld
    heuristicValue=h
    return h


def heuristic(node, values):
    return values[node]

# algorithm function
def astar(start, end):
    global heuristicValue
    path = {}
    distance = {}
    q = priorityQueue()
    
    h = heuristicValue
    
    # add start city to queue
    q.push(start, 0)
    # distance start with 0
    distance[start] = 0
    path[start] = None
    expandedList = []
    # add to queue and calcluate cost and distance 
    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)

        if (current == end):
            break

        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)
            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = current

    printoutput(start, end, path, distance, expandedList)

# make output of path
def printoutput(start, end, path, distance, expandedlist):
    global context
    finalpath = []
    i = end
    # loop over queue to get optimal path
    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    
    context+="Cost : " + str(distance[end]) +"\n"
    context+="ASTAR : " + " => ".join(finalpath)
    print(context)

# search with src and dst cities passed from website
def searchFunction(src,dst):
    global context
    global romania
    # if romania dict is empty : initialize
    if not bool(romania):
        initFunction()
        print("fist run: intialize map")
    context=""
    if not dst:
        dst="Bucharest"
    print(dst)
    # if cities not in the map
    if src not in romania :
        context= 'CITY NOT ON MAP.'
        print ('CITY NOT ON MAP.')
        return context
    
    else:
        # call algorithm function
        astar(src, dst)
        # return the path to website
        return context


# ADD NEW MAP
def storeFunction(graphSet,st):
    # Fetch global variables
    global romania
    global heuristicValue
    try:
        romania={}
        # intialize romania dictionary
        romania= makedict(graphSet)
        # intialize heuristiv values
        heuristicValue=makehuristikdict(st)
        return "NEW MAP SAVED"
    except:
        return "Data Error"
    
#init data for first run 
def initFunction():
    global romania
    global heuristicValue
    romania={}
    heuristicValue ={
                    'Arad': 366,
                    'Zerind': 374,
                    'Oradea': 380,
                    'Sibiu':  253,
                    'Fagaras':176,
                    'Rimnicu_Vilcea': 193,
                    'Timisoara': 329,
                    'Lugoj': 244,
                    'Mehadia': 241,
                    'Dobreta': 242,
                    'Pitesti':100,
                    'Craiova':160,
                    'Bucharest':0,
                    'Giurgiu':77,
                    'Urziceni': 80,
                    'Vaslui':199,
                    'Iasi':226,
                    'Neamt':234,
                    'Hirsova':151,
                    'Eforie':161
                    }
    str = "Arad Sibiu 140\nArad Timisoara 118\nArad Zerind 75\nBucharest Fagaras 211\nBucharest Giurgiu 90\nBucharest Pitesti 101\nBucharest Urziceni 85\nCraiova Dobreta 120\nCraiova Pitesti 138\nCraiova Rimnicu_Vilcea 146\nDobreta Mehadia 75\nEforie Hirsova 86\nFagaras Sibiu 99\nHirsova Urziceni 98\nIasi Neamt 87\nIasi Vaslui 92\nLugoj Mehadia 70\nLugoj Timisoara 111\nOradea Zerind 71\nOradea Sibiu 151\nPitesti Rimnicu_Vilcea 97\nRimnicu_Vilcea Sibiu 80\nUrziceni Vaslui 142" 
    
    romania= makedict(str)
    
    return "Reset Romania map successfully"