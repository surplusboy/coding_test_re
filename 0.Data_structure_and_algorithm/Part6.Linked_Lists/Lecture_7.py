'''
추상적 자료구조 (Abstract Data Structures)
1. Data
2. A set of operations
'''


'''
Singly Linked List 의 추상적 자료구조 구현해보기
서로 Linked 되어있는 Node(Data, Link)의 집합
Head - Tail 의 구조로 형성
Node의 총 갯수를 알고 있으면 좋다 (of nodes : n)

선형배열과의 비교
저장공간이 연속한 위치에 있지 않으며 메모리 임의의 위치에 존재하게 된다.
또한 특정 원소를 지칭할때 O(1)이 아닌 O(n) 즉, 선형탐색과 유사한 형태가 된다.
'''


class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

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
        if pos <= 0 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        bins = []
        curr = self.head
        while curr != None:
            bins.append(curr.data)
            curr = curr.next
        return bins

    def insertAt(self, pos, newNode):
        if pos <= 0 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos -1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True
    '''
    pop 메소드 check list
    
    입력 인자의 범위 유효성 O
    head 부터 시작해서 삭제할 노드를 찾아감 (하나 하나 따라가는 수밖에 없지요, 연결 리스트의 특성상) O
    삭제할 노드의 이전 노드의 next 에 삭제할 노드의 다음 노드를 연결 O
    (특별한 상황 1) 만약 삭제되는 노드가 첫번째 노드 (head) 라면 연결 리스트의 head 를 갱신 O
    (특별한 상황 2) 만약 삭제되는 노드가 마지막 노드 (tail) 라면 연결 리스트의 tail 을 갱신 O
    연결 리스트의 노드 개수를 나타내는 값을 1 만큼 감소 O
    삭제되는 노드가 담고 있는 데이터를 반환 O
    '''
    def popAt(self, pos):
        if pos <= 0 or pos > self.nodeCount:
            raise IndexError

        # curr = self.getAt(pos)
        i = 1
        curr = self.head
        while i < pos:
            if pos - 1 == i:
                prev = curr
            curr = curr.next
            i += 1

        if pos == 1:
            if self.nodeCount == 1:
                self.head = None
                self.tail = None
            else:
                self.head = curr.next
        else:
            if pos == self.nodeCount:
                self.tail = prev
            prev.next = curr.next
        self.nodeCount -= 1
        return curr.data

    def concat(self, L): # 연결 리스트 연결
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount

    def getLength(self):
        return '현재 노드의 갯수 : {}'.format(self.nodeCount)

'''
단방향 연결 리스트의 시간복잡도

삽입
맨 앞에 삽입 : O(1)
중간에 삽입 : O(n)
맨 끝에 삽입 : O(1)

삭제
맨 앞에서 삭제 : O(1)
중간에서 삭제 : O(n)
맨 끝에서 삭제 : O(n)
'''


a = Node(67)
b = Node(34)
c = Node(28)
L = LinkedList()
print(L)

for i in range(1, 11):
    L.insertAt(i, Node(i))
# print('before pop : {}, {}'.format(L.head, L.tail))
# print(L.insertAt(1, a))
# print(L.insertAt(2, b))
# print(L.insertAt(1, c))
# L.insertAt(L.nodeCount + 1, Node(5))
# print('after for loop : {}'.format(L.traverse()))
# L.popAt(3)
# print(L.tail.next.data)
# print('L.head : {}'.format(L.head.data))
# print('L.tail addr : {}'.format(L.tail))
# print(L.getAt(2).next.data)

# print('pop value : {}'.format(L.popAt(1)))
# print('after pop : {}, {}'.format(L.head, L.tail))

print(L.traverse())
# print(L.tail.next.data)
# print('L.head : {}'.format(L.head.data))
# print(L.getAt(2).next.data)
print(L.getLength())