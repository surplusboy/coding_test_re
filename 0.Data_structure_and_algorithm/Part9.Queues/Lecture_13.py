'''
큐 (Queue) : data elements 를 보관할 수 있는 선형의 자료구조

enqueue & dequeue 의 연산으로 FIFO 특징을 가지고 있다.

연산의 정의
1. size() : 현재 큐에 들어있는 데이터 원소의 수
2. isEmpty() : 현재 큐가 비어 있는지 체크
3. enqueue(x) : 데이터 원소 x를 큐에 추가
4. dequeue() : 큐의 맨 앞에 저장된 데이터 원소를 제거 및 반환
5. peek() : 큐의 맨 앞에 저장된 데이터 원소를 반환
'''
import queue
from pythonds.basic.queue import Queue
from Doubly_Linked_List import LinkedListQueue
from Doubly_Linked_List import DoublyLinkedList
# 배열로 구현한 큐
class ArrayQueue:

    def __init__(self):
        self.data = list()

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self): # O(n) 의 시간 복잡도를 가지게 된다.
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

L = DoublyLinkedList
Q = LinkedListQueue()
Q.size()
Q.enqueue(1)
print(Q.peek())