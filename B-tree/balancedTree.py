class Node:
  def __init__(self, left = None, right = None):
    self.value = None
    self.left = left
    self.right = right

class BalancedTree:
  def __init__(self):
    self.root = None

  def insert(self, val):
    new_node = Node(val)

    if self.root is None:
      self.root = new_node
      return

    queue = [self.root]
    while queue:
      current = queue.pop(0)
      if current.left is None:
        current.left = new_node
        return
      else:
        queue.append(current.left)

      if current.right is None:
        current.right = new_node
        return
      else:
        queue.append(current.right)

    def levelOrderTraversalStck(self):
      if self.root is None:
        return []

      queue = [self.root]
      res = []
      currLevel = 0

      while queue:
        current = queue
        if current.left is None:
          C

