import unittest

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self):
    self.head = None

  def isEmpty(self) -> bool:
    return True if self.head == None else False

  def append(self, value):
    curr = self.head

    if self.head == None:
      self.head = Node(value)
    else:
      while curr.next:
        curr = curr.next
      curr.next = Node(value)

  def appendLeft(self, value):
    newHead = Node(value)
    newHead.next = self.head
    self.head = newHead

  def pop(self):
    # Check if the list is empty
    if self.head is None:
        return -1

    # Check if the list has only one element
    if self.head.next is None:
        value = self.head.value
        self.head = None
        return value

    curr = self.head
    while curr.next:
        prev = curr
        curr = curr.next

    # Remove the last node
    prev.next = None
    return curr.value


  def popLeft(self):
    print(self.head.value)
    if self.head is None:
      return -1

    if self.head.next is None:
      popValue = self.head.value
      self.head = None
      return popValue

    popValue = self.head.value
    newHead = self.head.next
    self.head = newHead

    return popValue

class TestQueue(unittest.TestCase):
  def testScenario(self):
    queue = Queue()
    self.assertEqual(queue.head, None)
    self.assertEqual(queue.isEmpty(), True)

    queue.append(10)
    self.assertEqual(queue.head.value, 10)

    queue.append(20)
    queue.append(30)
    queue.append(40)

    self.assertEqual(queue.head.next.value, 20)
    self.assertEqual(queue.head.next.next.value, 30)

    queue.appendLeft(0)
    self.assertEqual(queue.head.value, 0)

    pop= queue.pop()
    self.assertEqual(pop, 40)

    popLeft = queue.popLeft()
    self.assertEqual(popLeft, 0)


if __name__ == '__main__':
    unittest.main()