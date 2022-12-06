class ListNode:
    def __init__(self, item):
        self.val = item
        self.next = None

def traverseNode(node:ListNode) -> str:
    result = str()

    curr_node = node
    while curr_node is not None:
        result += '{} '.format(curr_node.val)
        curr_node = curr_node.next
    return result.rstrip()

class SinglyLinked:
    def __init__(self):
        self.head = None

    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

s = SinglyLinked()
s.addAtHead(1)
s.addAtHead(2)

print(traverseNode(s.head))