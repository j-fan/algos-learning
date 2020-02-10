class QuickUnionUF:
  def __init__(self, N):
    self.id =[]
    for i in range(N):
      self.id.append(i)

  def root(self, i):
    while(i != self.id[i]):
      i = self.id[i]
    return i
  
  def connected(self, p, q):
    return self.root(p) == self.root(q)

  def union(self, p, q):
    pRoot = self.root(p)
    qRoot = self.root(q)
    self.id[pRoot] = qRoot

  def show(self):
    print(self.id)