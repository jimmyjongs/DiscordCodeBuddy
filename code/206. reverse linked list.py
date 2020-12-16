# Reverse a singly linked list.



class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


def traverseLL(head):
    while(head != None):
        print(head.val)
        head = head.next
    print("-----")

traverseLL(n1)

def reverseListIter(head):
    curr = head
    prev = None 

    while(curr != None):
        temp = curr.next

        curr.next = prev 
        prev = curr
        curr = temp

    return prev


def reverseListRecur(head):
    if head == None or head.next == None:
        return head
    temp = reverseListRecur(head.next)
    head.next.next = head
    head.next = None 
    return temp

traverseLL(reverseListIter(n1))

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
traverseLL(reverseListRecur(n1))
