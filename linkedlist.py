class LinkedListIter:
  def __init__(self, lst): #Not receiving list?
      self.index = 0
      self.List = lst
      self.length = lst.__len__()

  def __next__(self):
    if self.index == self.length:
        raise StopIteration
    else:
        self.index += 1
        return self.List[self.index-1]

class LinkedList:
  def __init__(self, lst=[]):
    self.L = lst
    self.size = 0

  def addLast(self, x):
    self.L.append(x)
    self.size += 1

  def addFirst(self, x):
    dummy = []
    dummy.append(x)
    for element in self.L:
        dummy.append(element)
    self.L = dummy
    self.size += 1

  def removeFirst(self):
    if self.size > 1:
        x = self.L[0]
        dummy = []
        for element in range(1, self.size):
            dummy.append(self.L[element])
        self.L = dummy
        self.size -= 1
        return x
    else:
        return None

  def removeLast(self):
    if self.size > 1:
        dummy = []
        x = self.L[self.size-1]
        for element in range(self.size-1):
            dummy.append(self.L[element])
        self.L = dummy
        self.size -= 1
        return x
    else:
        return None

  def addAt(self, idx, x):
    if idx == 0 or idx == self.size*-1:
        self.addFirst(x)
    elif idx > self.size or idx <= (self.size * -1):
        return None
    else:
        dummy = []
        for z in range(idx):
            dummy.append(self.L[z])
        dummy.append(x)
        for z in range(idx, self.size):
            dummy.append(self.L[z])
        self.L = dummy
        self.size += 1
        return True


  def removeAt(self, idx):
    if idx >= self.size or idx <= (self.size * -1):
        return None
    elif idx == 0 or idx == self.size*-1:
        self.removeFirst()
    elif idx == self.size -1 or idx == -1:
        self.removeLast()
    else:
        dummy = []
        for x in range(idx):
            dummy.append(self.L[x])
        for x in range(idx+1, self.size):
            dummy.append(self.L[x])
        self.L = dummy
        self.size -= 1

  def __str__(self):
     if self.size == 0:
         return (str(self.L))
     else:
         str1 = '['
         str3 = ']'
         for x in self.L:
             str2 = str(x) + ';'
             str1 = str1 + str2
         return(str1[:len(str1)-1] + str3)

  def __contains__ (self, x):
      for element in self.L:
          if element == x:
              return True
              break
          else:
              pass
      return False

  def __setitem__(self, idx, x):
      if idx >= self.size or idx < (self.size * -1):
          raise Exception("Invalid index " + str(idx))
      else:
          self.L[idx] = x

  def __getitem__(self, idx):
      if idx >= self.size or idx < (self.size * -1):
          raise Exception("Invalid index " + str(idx))
      else:
          return self.L[idx]

  def __iter__(self):
      return LinkedListIter(self.L)

  def __len__(self):
    return self.size

LL = LinkedList()
LL.addFirst(10)
LL.addLast(20)
LL.addLast(30)
LL.addAt(3, 40)
print(LL)

for x in LL:
    print(x)
