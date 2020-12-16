# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.





class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


n1 = Node(3)
n2 = Node(2)
n3 = Node(0)
n4 = Node(-4)


n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n3


def twoPointers(head):
    fast = head.next
    slow = head

    while(fast != slow):
        if(fast.next == None or fast == None):
            return False
        # print("fast: " + str(fast.val))
        # print("slow: " + str(slow.val))
        fast = fast.next.next
        slow = slow.next


    return True

