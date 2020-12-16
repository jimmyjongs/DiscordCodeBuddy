# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

m1 = ListNode(5)
m2 = ListNode(6)
m3 = ListNode(4)

m1.next = m2
m2.next = m3


def printLL(head):
    curr = head
    while(curr):
        print(curr.val, end="")
        curr = curr.next


printLL(n1)
print("\n-----")
printLL(m1)
print("\n-----")


def addTwoNums(head1, head2):
    curr1 = head1
    curr2 = head2

    num1 = ""
    num2 = ""

    while(curr1):
        num1 += str(curr1.val)
        curr1 = curr1.next

    while(curr2):
        num2 += str(curr2.val)
        curr2 = curr2.next

    num1 = num1[::-1]
    num2 = num2[::-1]

    return int(num1) + int(num2)



print(addTwoNums(n1, m1))
