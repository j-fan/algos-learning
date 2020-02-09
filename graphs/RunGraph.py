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

w.show()
assert w.dijkstra(1, 8) == 9
assert w.dijkstra(1, 0) == 16
assert w.dijkstra(1, 4) == 4
assert w.dijkstra(6, 0) == 22
assert w.dijkstra(1, 1) == 0
