'''
Stack 이란 ?
Data Element 를 보관 할 수 있는 선형적인 데이터 구조
LIFO 의 처리 제어 방식을 가지고 있다.

Stack 에서 발생하는 대표적인 오류
1. 비어있는 스택에서 데이터 원소를 꺼내려 할 때 -> 스택 언더 플로우
2. 꽉 찬 스택에 데이터 원소를 넣으려 할때 -> 스택 오버 플로우

이번 실습은 스택을 추상적 자료구조로 구현해볼 것

Stack 의 대표적인 연산
1. size() : 현재 스택에 들어있는 데이터 원소의 수 반환
2. isEmpty() : 현재 스택의 null 체크 반환
3. push(x) : 데이터 원소 x 를 스택에 추가
4. pop() : 스택의 맨 위에 저장된 데이터 원소를 제거 및 반환
5. peek() : 스택의 맨 위에 저장된 데이터 원소를 반환
'''

# 배열(array)를 이용한 구현 -> python에 builtin 으로 제공되는 list와 method 를 이용
class ArrayStack:
    def __init__(self):
        self. data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

from Doubly_Linked_List import Node
from Doubly_Linked_List import DoublyLinkedList

# 연결 리스트 (linked list) 를 이용하여 구현 -> DoublyLinkedList 이용

class LinkedListStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def push(self, x):
        node = Node(x)
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data

from pythonds.basic.stack import Stack
S = Stack()
S.push(1)
S.push(2)
# print(S.items)


# def solution(expr):
#     match = {
#         ')': '(',
#         '}': '{',
#         ']': '['
#     }
#     S = ArrayStack()
#     for c in expr:
#         if c in '({[':
#             S.push(c)
#         elif c in match:
#             if:
#
#                 return False
#
#             else:
#
#                 if t != :
#                     return False
#     return


def 괄호_검사(expr):
    stack = list()
    match = {
            ')': '(',
            '}': '{',
            ']': '['
        }

    for i in expr:
        if i in '({[':
            stack.append(i)
        elif i in match:
            if len(stack) == 0:
                return False
            else:
                t = stack.pop()
                if t != match[i]:
                    return False
    return not bool(stack)

# print(괄호_검사('[(A + B) * C]'))