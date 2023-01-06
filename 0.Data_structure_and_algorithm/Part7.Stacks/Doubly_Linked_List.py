class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def getLength(self):
        return self.nodeCount

    def traverse(self):
        result = list()
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def reverse(self):
        result = list()
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result

    def insertAt(self, pos, newNode, before=False):
        if pos < 1 or pos > self.nodeCount + 1:
            raise IndexError
        prev = self.getAt(pos - 1)
        if not before:
            return self.insertAfter(prev, newNode)
        elif before and pos < self.nodeCount + 1:
            next = prev.next
            return self.insertBefore(next, newNode)
        else:
            raise IndexError

    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertBefore(self, next, newNode):
        prev = next.prev
        newNode.prev = prev
        newNode.next = next
        next.prev = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def popAt(self, pos, option=None):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        curr = self.getAt(pos)
        if option is None:
            curr.next.prev = curr.prev
            curr.prev.next = curr.next
            self.nodeCount -= 1
            return curr.data
        elif option is True and pos < self.nodeCount:
            return self.popAfter(curr)
        elif option is False and pos > 1:
            return self.popBefore(curr)

    def popAfter(self, prev):
        curr = prev.next
        curr.next.prev = prev
        prev.next = curr.next
        self.nodeCount -= 1
        return curr.data

    def popBefore(self, next):
        curr = next.prev
        curr.prev.next = next
        next.prev = curr.prev
        self.nodeCount -= 1
        return curr.data

    def concat(self, L):
        if self.nodeCount == 0:
            self.head.next = L.head.next
            self.tail.prev = L.tail.prev
            self.nodeCount = L.nodeCount
            return True
        elif L.nodeCount == 0:
            return False
        self.tail.prev.next = L.head.next
        self.tail = L.tail
        self.nodeCount += L.nodeCount
        return True

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1
        return curr
