class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    head = None

    node1 = LinkedListNode(10)
    head = node1

    node2 = LinkedListNode(20)
    node3 = LinkedListNode(30)
    node4 = LinkedListNode(40)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    # print the LinkedListNode
    def printLL(self, head):
        current = head
        while current is not None:
            print(current.val)
            current = current.next

    def insertAtFront(self, newNode, head):
        newNode.next = head
        head = newNode
        return head

    def insertBetween2Nodes(self, head, newNode, n1, n2):
        n1.next = newNode
        newNode.next = n2
        return head

    def insertAtEnd(self, head, newNode):
        current = head
        if current is None:
            return newNode
        while current.next is not None:
            current = current.next
        current.next = newNode
        return head

    def addNodeAfterNode(self, head, newNode, n1):
        current = head
        while current is not None and current != n1:
            current = current.next

        temp = current.next
        current.next = newNode
        newNode.next = temp
        return head

    def deleteFrontNode(self, head):
        if head is None:
            return head
        temp = head.next
        head.next = None
        head = temp
        return head

    def deleteFromEnd(self, head):
        current = head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = current.next
        return head

    def deleteNodeFromFront(self, head):
        dummyNode = LinkedListNode(-1)
        dummyNode.next = head

        tempNode = dummyNode.next
        dummyNode.next = None
        head = tempNode
        return head

    def deleteNodeFromEnd(self, head):
        dummyNode = LinkedListNode(-1)
        dummyNode.next = head
        prev = dummyNode
        current = head

        while current.next is not None:
            prev = current
            current = current.next
        prev.next = current.next
        return head

    printLL(head)
