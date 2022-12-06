class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList : Empty'

        s = str()
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        bins = []
        curr = self.head
        while curr.next:
            curr = curr.next
            bins.append(curr.data)

        return bins

    def insertAtHead(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.nodeCount += 1

    def insertAt(self, pos, newNode):
        if pos <= 0 or pos > self.nodeCount+1:
            return False

        if pos != 1 and pos == self.nodeCount+1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)

        return self.insertAfter(prev, newNode)

    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos <= 0 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)

        return self.popAfter(prev)

    def popAfter(self, prev):
        curr = prev.next
        if curr is None:
            return None

        if curr is self.tail:
            self.tail = prev
            prev.next = None
        else:
            prev.next = curr.next

        self.nodeCount -= 1

        return curr.data


    def concat(self, L):
        self.tail.next = L.head.next
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount

    def getLength(self):
        return '현재 노드의 갯수 : {}'.format(self.nodeCount)

L = LinkedList()
print(L)

for i in range(1, 11):
    L.insertAt(i, Node(i))
print(L)

print(L.head.next.next.data)
print(L.getAt(0).next.data)
print(L.popAt(10))

print(L.traverse())
print(L.getLength())
print(L.head.data)

L.insertAtHead(131)
print(L.traverse())
print(L.getLength())
print(L.head.data)
