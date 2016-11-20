class LinkedList:
    def __init__(self, node):
        self.node = node

    def add(self, next_node):
        node = self.node
        while node.next:
            node = node.next
        node.next = next_node

    def remove(self, value):
        node = self.node
        if node.value == value:
            self.node = node.next

        while node.next:
            if node.next.value == value:
                self.node.next = node.next.next
                return
            node = node.next
