# graph as adjacency matrix
from Graph import Graph
import queue

class GraphAM(Graph):
  def __init__(self, numVertexes):
    self.numVertexes = numVertexes
    self.graph = [[0 for _ in range(numVertexes)] for _ in range(numVertexes)]
  
  def dfs(self, src, dest):
    stack = []
    stack.insert(0, src)
    visited = []
    visited.append(src)
    pathFrom = [None] * self.numVertexes
    pathFrom[src] = -1

    while len(stack) > 0:
      current = stack.pop()
      for neighbour in self.neighbours(current):
        if neighbour not in visited:
          visited.append(neighbour)
          stack.insert(0, neighbour)
          pathFrom[neighbour] = current

    # unwind path from tree
    current = dest
    shortestPath = []
    shortestPath.append(dest)
    while not current == src:
      current = pathFrom[current]
      shortestPath.append(current)
    print(shortestPath)
    return shortestPath

  def bfs(self, src, dest):
    q = queue.Queue() # can also visualise it as the "frontier"
    q.put(src)
    visited = []
    visited.append(src)
    pathFrom = [None] * self.numVertexes
    pathFrom[src] = -1

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
    shortestPath.append(dest)
    while not current == src:
      current = pathFrom[current]
      shortestPath.append(current)
    print(shortestPath)
    return shortestPath
    
  def insertUndirected(self, x, y):
    self.graph[x][y] = 1
    self.graph[y][x] = 1

  def removeUndirected(self, x, y):
    self.graph[x][y] = 0
    self.graph[y][x] = 0

  def insert(self, x, y):
    self.graph[x][y] = 1

  def remove(self, x, y):
    self.graph[x][y] = 0

  def neighbours(self, v):
    neighbours = []
    for i in range(self.numVertexes):
      if self.graph[v][i]:
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

