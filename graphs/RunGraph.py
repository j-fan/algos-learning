from GraphAM import GraphAM


def isArraySame(arr1, arr2):
    if not len(arr1) == len(arr2):
        return False
    for i in range(len(arr1)):
        if not arr1[i] == arr2[i]:
            return False
    return True


g = GraphAM(10)
g.insertUndirected(1, 9)
g.insertUndirected(3, 4)
g.insertUndirected(2, 9)
g.insertUndirected(9, 5)
g.insertUndirected(5, 4)
g.insertUndirected(6, 1)
g.insertUndirected(3, 8)
g.insertUndirected(2, 7)
g.insertUndirected(6, 4)

assert isArraySame(g.bfs(1, 7), g.dfs(1, 7)) == True
assert isArraySame(g.bfs(1, 4), g.dfs(1, 4)) == True
assert isArraySame(g.bfs(3, 1), g.dfs(3, 1)) == True
assert isArraySame(g.bfs(8, 7), g.dfs(8, 7)) == True

w = GraphAM(10)
w.insertUndirected(1, 9, 1)
w.insertUndirected(3, 4, 2)
w.insertUndirected(2, 9, 3)
w.insertUndirected(9, 5, 1)
w.insertUndirected(5, 4, 2)
w.insertUndirected(6, 1, 6)
w.insertUndirected(3, 8, 3)
w.insertUndirected(2, 7, 9)
w.insertUndirected(6, 4, 9)
w.insertUndirected(0, 7, 3)
w.insertUndirected(0, 8, 9)

assert w.dijkstra(1, 8) == 9
assert w.dijkstra(1, 0) == 16
assert w.dijkstra(1, 4) == 4
assert w.dijkstra(6, 0) == 22
assert w.dijkstra(1, 1) == 0

c = GraphAM(11)
# component 1
c.insertUndirected(1, 5)
c.insertUndirected(1, 4)
c.insertUndirected(2, 4)
c.insertUndirected(5, 0)
#component 2
c.insertUndirected(3, 6)
#component 3
c.insertUndirected(8, 7)
c.insertUndirected(8, 9)
# component 4
c.insertUndirected(10, 10)
c.connectedComponents()
print(c.components)

assert c.connected(1, 0)
assert not c.connected(3, 8)
assert c.connected(2, 5)
assert c.connected(10, 10)
assert c.connected(2, 0)
assert c.connected(0, 2)
