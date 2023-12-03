
def get_file(path, file_name):
    with open(path, 'r') as file_name:
        file_name = file_name.readlines()
        name = {}
        for row in file_name:
            row = row.strip().split('/')
            if row:  
                movie_title = row[0].strip()  
                temp_store = []
                for actor_info in row[1:]:  
                    actor_parts = actor_info.strip().split(',')
                    if len(actor_parts) > 1:
                        actor_name = actor_parts[-1].strip() + " " + actor_parts[0].strip()
                        temp_store.append(actor_name)
                    else:
                        temp_store.append(actor_info.strip())
                name[movie_title] = temp_store

        return name

ActionCastData = get_file(r"C:\Users\nuzha\OneDrive\Desktop\507\Kavin_bacon\BaconData\ActionCast.txt", "ActionCast")
#print(ActionCastData[2])

Bacon06Data = get_file(r"C:\Users\nuzha\OneDrive\Desktop\507\Kavin_bacon\BaconData\Bacon_06.txt", "Bacon06")
#print(Bacon06Data[2])

BaconCast_00_06Data = get_file(r"C:\Users\nuzha\OneDrive\Desktop\507\Kavin_bacon\BaconData\BaconCast_00_06.txt", "BaconCast_00_06")
#print(BaconCast_00_06Data[1])

BaconCastFullData = get_file(r"C:\Users\nuzha\OneDrive\Desktop\507\Kavin_bacon\BaconData\BaconCastFull.txt", "BaconCastFull")
#print(BaconCastFullData[2])

PopularCastData = get_file(r"c:\Users\nuzha\OneDrive\Desktop\507\Kavin_bacon\BaconData\PopularCast.txt", "PopularCast")
#print(PopularCastData.values())

Actors_set = set()

for i in PopularCastData.values():
    for j in i:
        Actors_set.add(j)
       
Actors_lst = list(Actors_set)
Actors_movie_dict = {}

for key,value in PopularCastData.items(): #key is movie, value is list of actors    
    for val in value:
        if val in Actors_movie_dict:
            Actors_movie_dict[val].append(key)
        else:
            Actors_movie_dict[val] = [key]

#print(Actors_movie_dict.keys())
#print(Actors_movie_dict["Kevin Bacon"])

class Vertex:
  def __init__(self, value):
    self.id = value
    self.connectedTo = {}
    self.degree = 0
  def addNeighbor(self, nbr, weight=0):
    self.connectedTo[nbr]= weight
  def getId(self):
    return self.id


class Graph:
  def __init__(self):
    self.vertList = {}
    self.numVertices = 0

  def addVertex(self, key):
    self.numVertices += 1
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    return newVertex

  def addEdge(self, f, t, weight=0):
    if f not in self.vertList:
      nv = self.addVertex(f)
    if t not in self.vertList:
      nv = self.addVertex(t)
    self.vertList[f].addNeighbor(self.vertList[t], weight = 0)

g = Graph()
for i in PopularCastData.keys():
    g.addVertex(i)
for j in Actors_movie_dict.keys():
    g.addVertex(j)

for key,value in PopularCastData.items():
    for val in value:
        g.addEdge(key,val)

for key,value in Actors_movie_dict.items():
    for val in value:
        #print(key,"\n", val)
        g.addEdge(key, val)
#print(Actors_movie_dict["Kevin Bacon"])


from collections import deque

def BFS_minimumPath(graph, start_vertex,end_vertex):
    
    discovered = {}
    distance = {}
    parent = {}

    for vert in graph.vertList:
        discovered[vert] = False
        distance[vert] = -1  
        parent[vert] = None

    q = deque()
    q.append(start_vertex)
    discovered[start_vertex] = True
    distance[start_vertex] = 0

    while q:
       current = q.popleft()
       for neighbor in graph.vertList[current].connectedTo:
           if discovered[neighbor.id] == False:
               discovered[neighbor.id] = True
               distance[neighbor.id] = distance[current] + 1
               parent[neighbor.id] = current
               q.append(neighbor.id)
               if neighbor.id == end_vertex:
                  break
    path = []
    current = end_vertex
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path, distance[end_vertex]


print(BFS_minimumPath(g, "Kevin Bacon", "Ed Hodson"))  


def BFS_averagePath(graph, start_vertex):
    
    discovered = {}
    distance = {}
    parent = {}

    for vert in graph.vertList:
        discovered[vert] = False
        distance[vert] = -1  
        parent[vert] = None

    q = deque()
    q.append(start_vertex)
    discovered[start_vertex] = True
    distance[start_vertex] = 0

    while q:
       current = q.popleft()
       for neighbor in graph.vertList[current].connectedTo:
           if discovered[neighbor.id] == False:
               discovered[neighbor.id] = True
               distance[neighbor.id] = distance[current] + 1
               q.append(neighbor.id)

    avg = sum(distance.values())/len(distance.values())
    return avg
print(BFS_averagePath(g, "Kevin Bacon"))
               
    