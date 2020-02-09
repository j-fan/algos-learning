# graph as adjacency matrix
from Graph import Graph
import queue
import sys

class GraphAM(Graph):
  def __init__(self, numVertexes):
    self.numVertexes = numVertexes
    self.graph = [[0 for _ in range(numVertexes)] for _ in range(numVertexes)]
    self.components = [None] * numVertexes
    self.reverseGraph = [[0 for _ in range(numVertexes)] for _ in range(numVertexes)]
  
  def dijkstra(self, src, dest):
    pq = queue.PriorityQueue()
    pq.put((0, src))
    visited = []
    visited.append(src)
    costSoFar = [sys.maxsize] * self.numVertexes
    costSoFar[src] = 0
    cameFrom = [None] * self.numVertexes

    while not pq.empty():
      current = pq.get()[1]
      for neighbour in self.neighbours(current):
        tentativeCost = self.graph[current][neighbour] + costSoFar[current]
        if neighbour not in visited or tentativeCost < costSoFar[neighbour]:
          costSoFar[neighbour] = tentativeCost
          pq.put((tentativeCost, neighbour))
          visited.append(neighbour)
          cameFrom[neighbour] = current
    
    current = dest
    shortestPath = []
    shortestPath.insert(0, dest)
    while not current == src:
      current = cameFrom[current]
      shortestPath.insert(0, current)
    return costSoFar[dest]

  # strongly connected components for directed graphs
  def stronglyConnectedComponents(self):
    self.components = [None] * self.numVertexes
    componentCount = 0
    visited = []
    for v in self.reversePostOrder(): # only this line differs!
      if v not in visited:
        self.connectedDfs(v, componentCount, visited)
        componentCount += 1

  # reverse post-order is step one for connected components
  # note!! the correct order is (e.g)
  # [ ... ][dfs traveral 3][new unseen unconnected vert][dfs traversal 2][dfs traversal 1 (from src to dest)]
  def reversePostOrder(self):
    start = 0
    stack = []
    stack.insert(start, 0)
    unvisited = [i for i in range(self.numVertexes)]
    unvisited.remove(start)
    reversePostOrder = []

    currentDfsOrder = []

    while len(unvisited) > 0:
      if len(stack) > 0:
        current = stack.pop()
        currentDfsOrder.append(current)
      else:
        current = unvisited.pop(0)
        reversePostOrder = currentDfsOrder + reversePostOrder
        currentDfsOrder = [current]

      for neighbour in self.reverseNeighbours(current):
        if neighbour in unvisited:
          unvisited.remove(neighbour)
          stack.insert(0, neighbour)

    print(reversePostOrder)
    return reversePostOrder      

  def reverseNeighbours(self, v):
    neighbours = []
    for i in range(self.numVertexes):
      if not self.reverseGraph[v][i] == 0:
        neighbours.append(i)
    return neighbours

  # do not confuse with strongly connected components for directed graphs
  def connectedComponents(self):
    self.components = [None] * self.numVertexes
    componentCount = 0
    visited = []
    for v in range(self.numVertexes):
      if v not in visited:
        self.connectedDfs(v, componentCount, visited)
        componentCount += 1
        
  def connectedDfs(self, src, count, visited):
    stack = []
    stack.insert(0, src)
    visited.append(src)

    while len(stack) > 0:
      current = stack.pop()
      self.components[current] = count
      for neighbour in self.neighbours(current):
        if neighbour not in visited:
          visited.append(neighbour)
          stack.insert(0, neighbour)
    return visited

  def connected(self, x, y):
    return self.components[x] == self.components[y]

  def dfs(self, src, dest):
    stack = []
    stack.insert(0, src)
    visited = []
    visited.append(src)
    pathFrom = [None] * self.numVertexes

    while len(stack) > 0:
      current = stack.pop()
      if current == dest:
        break
      for neighbour in self.neighbours(current):
        if neighbour not in visited:
          visited.append(neighbour)
          stack.insert(0, neighbour)
          pathFrom[neighbour] = current

    # unwind path from tree
    current = dest
    shortestPath = []
    shortestPath.insert(0, dest)
    while not current == src:
      current = pathFrom[current]
      shortestPath.insert(0, current)
    return shortestPath

  def bfs(self, src, dest):
    q = queue.Queue() # can also visualise it as the "frontier"
    q.put(src)
    visited = []
    visited.append(src)
    pathFrom = [None] * self.numVertexes

    # do BFS until dest is found
    while not q.empty():
      current = q.get()
      if current == dest:
        break
      for neighbour in self.neighbours(current):
        if neighbour not in visited:
          q.put(neighbour)
          visited.append(neighbour)
          pathFrom[neighbour] = current

    # unwind the path-from tree to find shortest path to dest
    current = dest
    shortestPath = []
    shortestPath.insert(0, dest)
    while not current == src:
      current = pathFrom[current]
      shortestPath.insert(0, current)
    return shortestPath
    
  def insertUndirected(self, x, y, weight=1):
    self.graph[x][y] = weight
    self.graph[y][x] = weight

  def removeUndirected(self, x, y):
    self.graph[x][y] = 0
    self.graph[y][x] = 0

  def insert(self, x, y, weight=1):
    self.graph[x][y] = weight
    self.reverseGraph[y][x] = weight

  def remove(self, x, y):
    self.graph[x][y] = 0
    self.reverseGraph[y][x] = 0

  def neighbours(self, v):
    neighbours = []
    for i in range(self.numVertexes):
      if not self.graph[v][i] == 0:
        neighbours.append(i)
    return neighbours

  def show(self):
    print("  ",end="")
    for x in range(self.numVertexes):
      print(f' {x} ',end="")
    print()

    for x in range(self.numVertexes):
      print(f'{x} ', end="")
      for y in range(self.numVertexes):
        print(f'[{self.graph[x][y]}]', end="")
      print()

