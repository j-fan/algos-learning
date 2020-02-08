from GraphAM import GraphAM

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

g.show()
g.bfs(1, 4)
