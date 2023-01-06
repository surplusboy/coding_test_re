'''
큐(Queue)의 활용
자료를 생성하는 작업과 그 자료를 이용하는 작업이 비동기적 (asynchronously) 일어나는 경우
자료를 생성하는 작업이 여러 곳에서 일어나는 경우
자료를 이용하는 작업이 여러 곳에서 일어나는 경우
자료를 생성하는 작업과 그 자료를 이용하는 작업이 양쪽 다 여러 곳에서 일어나는 경우
자료를 처리하여 새로운 자료를 생성하고, 나중에 그 자료를 또 처리해야 하는 경우 -> 환형큐가 적용되면 좋은 예시

연산의 정의
1. size() : 현재 큐에 들어있는 데이터 원소의 수
2. isEmpty() : 현재 큐가 비어 있는지 체크
3. isFull() : 큐에 데이터 원소가 꽉 차 있는지를 판단
4. enqueue(x) : 데이터 원소 x를 큐에 추가
5. dequeue() : 큐의 맨 앞에 저장된 데이터 원소를 제거 및 반환
6. peek() : 큐의 맨 앞에 저장된 데이터 원소를 반환
'''

# 배열로 구현한 환형 큐
class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue is full')
        self.rear = (self.rear+1) % self.maxCount
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue Empty')
        self.front = (self.front+1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue Empty')
        return self.data[(self.front+1) % self.maxCount]

C = CircularQueue(5)

print(C.data)
C.enqueue(2)
print(C.dequeue())
print(C.data)

# print(C.peek())