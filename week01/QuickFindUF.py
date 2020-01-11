# quick find algo
# cost analysis:
# initalisation: N accesses
# union: N accesses
# find: 1 access

# union operation too expensive
# Takes n^2 accesses to process N commands on N objects

class QuickFindUF:
  def __init__(self, N):
    self.id = []
    for i in range(N):
      self.id.append(i)
    print(self.id)

  def connected(self, p, q):
    return self.id[p] == self.id[q]

  def union(self, p, q):
    pId = self.id[p]
    qId = self.id[q]
    for i in range(0, len(self.id)):
      if(self.id[i] == pId): 
        self.id[i] = qId

  def show(self):
    print(self.id)

quickFindUF = QuickFindUF(8)
quickFindUF.union(1,2)
quickFindUF.union(2,3)
quickFindUF.union(6,7)
quickFindUF.union(3,6)
quickFindUF.show()
print(quickFindUF.connected(1,6))



