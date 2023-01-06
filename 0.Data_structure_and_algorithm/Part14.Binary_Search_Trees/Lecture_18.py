'''
이진 탐색 트리 (Binary Search Trees)
모든 노드에 대해서,
    1) 왼쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 작음
    2) 오른쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 큼
위의 성질을 만족하는 이진 트리
(단, 중복되는 데이터는 없다고 가정)

배열을 이용한 이진 탐색과 비교
장점 : 데이터 원소의 추가, 삭제가 용이
단점 : 공간 소요가 큼

시간 복잡도 : O(logn) -> 항상 그렇지는 않다.

이진 탐색 트리의 추상적 자료구조
- 데이터 표현 : 각 노드는 key, value 의 쌍

연산의 정의
1. insert(key, data) : 트리에 주어진 데이터 원소를 추가
2. remove(key) : 특정 원소를 트리로부터 삭제
3. lookup(key) : 특정 원소를 검색
4. inorder() : 키의 순서대로 데이터 원소 나열
5. min(), max() : 최소 키, 최대 키를 가지는 원소 탐색

이진 탐색 트리가 효율적이지 못한 경우
1. 한쪽으로 치우친 형태 (skew)의 트리 구조일 경우 (선형의 시간복잡도와 같음)

트리의 높이 균형을 유지하기 위한 트리 알고리즘
    - AVL trees
    - Red-black trees
'''


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        traversal = list()
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return None

    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            # return self.data, parent.data if parent else parent
            return self, parent

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('중복 키값은 허용되지 않음')

    def countChildren(self):
        degree = 0
        if self.left:
            degree += 1
        if self.right:
            degree += 1
        return degree

class BinSearchTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None

    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    temp_node = node.left
                else:
                    temp_node = node.right
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if parent.left == node:
                        parent.left = temp_node
                    else:
                        parent.right = temp_node
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = temp_node
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent = successor
                    successor = successor.left
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

            return True

        else:
            return False
BT = BinSearchTree()
BT.insert(5, 5)
BT.insert(2, 2)
BT.insert(4, 4)
BT.insert(1, 1)
BT.insert(8, 8)
BT.insert(6, 6)
BT.insert(9, 9)
# BT.insert(7, 7)

# print(BT.lookup(1))
# print(BT.lookup(2))
# print(BT.lookup(7))
# print(BT.lookup(9)[0].right)
# print(BT.lookup(7))
print(BT.lookup(5))
# BT.remove(5)
# print(BT.lookup(5))
print(BT.inorder())
print(BT.lookup(6)[0].data, BT.lookup(6)[1].data)
BT.remove(5)
print(BT.root.data)
# print(BT.lookup(9)[0].left.data)
print(BT.inorder())
