class Node:
    def __init__(self, item, next=None):
        self.data = item
        self.next = next

    def __repr__(self):
        if self.next is not None:
            return self.next


def traverseNode(node:Node) -> str:
    result = str()

    curr_node = node
    while curr_node is not None:
        result += '{} '.format(curr_node.data)
        curr_node = curr_node.next
    return result.rstrip()
