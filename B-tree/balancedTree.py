from collections import deque

from collections import deque

class Node:
  def __init__(self, left = None, right = None):
    self.value = None
    self.left = left
    self.right = right

class BalancedTree:
    def __init__(self):
        self.root = None

    def insertBalanced(self, val):
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

    def in_order_traversal(self):
        def in_order(root: Node):
            if self.root is None:
                return

            in_order(root.left)
            print(root.val)
            in_order(root.right)

        in_order(self.root)

    def pre_order_traversal(self):
        def pre_order(root: Node):
            if self.root is None:
                return

            print(root.val)
            pre_order(root.left)
            pre_order(root.right)

        pre_order(self.root)

    def post_order_traversal(self):
        def post_order(root: Node):
            if self.root is None:
                return

            post_order(root.left)
            post_order(root.right)
            print(root.val)

        post_order(self.root)

    def in_order_traversal_iter(self):
        if self.root is None:
            return

        queue = deque()
        curr = self.root
        queue.append(curr)
        while queue:
            while curr is None:
                queue.append(curr.left)
                curr = curr.left

            curr = queue.popleft()
            print(curr.data)

            curr = curr.right

    def pre_order_traversal_iter(self):
        if self.root is None:
            return

        queue = deque()
        curr = self.root
        queue.append(curr)

        while queue:
            while curr is None:
                queue.append(curr.left)
                val  = queue.popleft()
                print(val)

            queue.append(curr.right)
