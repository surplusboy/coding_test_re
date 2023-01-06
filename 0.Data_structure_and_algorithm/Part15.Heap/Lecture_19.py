'''
힙 (Heap) 이란?

Binary Tree 의 한 종류 (= Binary Heap)

특징
1. root node (sub tree 포함) 가 언제나 최댓값 or 최솟값을 가짐 -> 최대 힙 (max heap), 최소 힙 (min heap)
2. 완전 이진 트리 (complete binary tree) 여야 함

Binary Search Tree 와의 비교
1. elements 가 완전히 크기 순으로 정렬되어 있는가 ? -> heap 은 느슨하게 정렬되어 있다.
2. specific key value 의 element 를 빠르게 검색할 수 있는가 ? 
3. 부가 제약 조건은 어떤 것인가 ? -> 완전 이진트리여야 한다는 제약 조건

Heap 의 응용
1. 우선 순위 큐 (priority queue)
    - Enqueue할 때 '느스한 정렬' 을 이루고 있도록 함 : O(logn)
    - Dequeue할 때 최댓값을 순서대로 추출 :O(logn)
    양방향 연결리스트와 비교하였을때 시간복잡도상 이점이 있음
2. 힙 정렬 (heap sort)
    - 정렬되지 않은 원소들을 무작위 순서로 최대 힙에 삽입 : O(logn)
    - 삽입이 끝나면 힙이 비어질 때까지 하나씩 삭제 : O(logn)
    - 원소들의 삭제 순서가 원소들의 정렬 순서
    - heap sort의 시간 복잡도 (Onlogn)
'''

'''
최대 힙 (Max Heap)의 추상적 자료구조

연산의 정의
1. __init__() : 빈 최대 힙 생성
2. insert(item) : 새로운 원소를 삽입
3. remove() : 최대 원소 (root node)를 반환 및 삭제 -> max heap 은 root node 가 항상 최댓 값이다.
* traverse 나 search 들의 메소드들은 heap 에서 제공 되지 않는다 -> binary search tree 와의 차이점 때문
'''

# 배열을 이용한 이진트리의 표현

class MaxHeap:
    def __init__(self):
        self.data = [None] # 0번 index 는 버리면서 생성하며 초기화

    def print(self):
        print(self.data)

    def insert(self, item):
        self.data.append(item)
        m = len(self.data) - 1 # 노드 번호 m -> 인덱싱 활용

        while m > 1:
            if self.data[m] > self.data[m//2]:
                self.data[m], self.data[m//2] = self.data[m//2], self.data[m]
                m = m//2
            else:
                break


    '''
    원소 삭제 로직
    1. 루트 노드 제거 (최대힙 기준 최댓값)                    
    2. 트리 마지막 자리 노드를 임시로 루트 노드의 자리에 배치
    3. 임시 루트 노드의 자식 노드들 과의 값 비교와 이동 -> 자식이 둘 이상일 경우 대소 비교
    '''
    def maxHeapify(self, i): # 인덱스를 인자로 받음
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = 2 * i

        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = (2 * i) + 1

        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if len(self.data) > left and self.data[left] > self.data[smallest]:
        # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            smallest = left
        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if len(self.data) > right and self.data[right] > self.data[smallest]:
        # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest = right
        if smallest != i:
        # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
        # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)

        else:
            data = None
        return data
    # def insert(self, item):
    #     m = len(self.data)
    #
    #     if m == 1:
    #         self.data.append(item)
    #     else:
    #         if item == self.data[m//2]:
    #             raise ValueError
    #
    #         if item < self.data[m//2]:
    #             self.data.append(item)
    #         else:
    #             while not item < self.data[m//2]:
    #                 a = self.data[m//2]
    #                 b = item
    #
    #                 self.data[m//2], b = b, a
    #                 m = m//2
    #             self.data.append(b)


def heapsort(unsorted:list) -> list:
    H = MaxHeap()
    for item in unsorted:
        H.insert(item)
    sorted = list()
    d = H.remove()
    while d:
        sorted.append(d)
        d = H.remove()
    return sorted

H = MaxHeap()

H.insert(10)
print(H.insert(9))
print(H.insert(8))
print(H.insert(7))
print(H.insert(6))
print(H.insert(30))

print(H.print())

# import numpy as np
