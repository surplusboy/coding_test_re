'''
우선순위 큐 (Priority Queue)
큐가 FIFO 방식을 따르지 않고 원소들의 우선순위에 따라 큐에서 빠져나오는 형식

* Point
1. Enqueue 할 때 우선순위 순서를 유지하며 삽입이 유리한가 ? Dequeue (무작위로 배열 된 데이터) 할 때 우선순위 높은 것을 선택하는 것이 유리한가 ? -> Enqueue 할 때가 유리
2. 선형 배열을 이용하는 것이 유리한가 ? 연결 리스트를 이용하는 것이 유리한가 ? -> 중간 노드를 끊으면 되는 연결 리스트를 이용하는 것이 유리 (메모리 사용량은 고려 x)
'''

from Doubly_Linked_List import Node, DoublyLinkedList

class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        while curr.next.data != None and newNode.data < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data

Q = PriorityQueue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(4)

# print(Q.dequeue())
# print(Q.dequeue())
# print(Q.dequeue())
print(Q.queue.traverse())