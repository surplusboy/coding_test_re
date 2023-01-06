'''
이진 트리의 추상적 자료 구조

연산의 정의
1. size() : 현재 트리에 포함되어 있는 노드의 수
2. depth() : 현재 트리의 깊이 (또는 높이; height)를 구함
3. traversal() : 정해진 조건에 맞게 순회

이진 트리의 순회 (traversal)
1. 깊이 우선 순회 (depth first traversal)
 1) 중위 순회 (in-order traversal)
 2) 전위 순회 (pre-order traversal)
 3) 후위 순회 (post-order traversal)
2. 넓이 우선 순회 (breadth first traversal)
 - 원칙
    1) level 이 낮은 노드를 우선 방문
    2) 같은 level 의 노드들 사이에는 parent 노드의 방문 순서에 따라 방문 -> left child 노드를 우선 방문
    -> recursive 한 방법이 적합한가 ? X
'''
from pythonds.basic.queue import Queue

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        if r > l:
            return r + 1
        else:
            return l + 1

    def inorder(self):
        traversal = list()
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        traversal = list()
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    def postorder(self):
        traversal = list()
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal

class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

    def btf(self):
        traversal = list()
        q = Queue()

        if self.root:
            q.enqueue(self.root)
        else:
            return []

        while q.size():
            node = q.dequeue()
            traversal.append(node.data)

            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
        return traversal