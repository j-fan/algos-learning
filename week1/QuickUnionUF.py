# Quick Union algo
# attempts to be faster through tree structure

# cost analysis:
# initalisation: N accesses
# union: N accesses
# find: N access (worst case)

# find op too expensive in the worst case when trees arent flat
# however is faster than quick find on union op

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

quickUnion = QuickUnionUF(8)
quickUnion.show()
quickUnion.union(1,2)
quickUnion.union(5,6)
quickUnion.show()
quickUnion.union(2,6)
quickUnion.show()
print(quickUnion.connected(1,6))
print(quickUnion.connected(7,6))


