# "Google: 90% of our engineers use the software you wrote (Homebrew), 
# but you can’t invert a binary tree on a whiteboard so f*** off."

# wayment... inverting a bin tree is kinda easy tho

# Invert a binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(7)

n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(9)


n1.left = n2
n1.right = n3 
n2.left = n4
n2.right = n5 
n3.left = n6
n3.right = n7 


def BFSPrint(root):
    if(root.left != None or root.right != None):
        print("Root: ",root.val)
        print("Left: ", root.left.val)
        print("Right: ", root.right.val)
        print("------")
        BFSPrint(root.left)
        BFSPrint(root.right)




def invertBinTree(root):

    if(root.left != None or root.right != None):
        root.right, root.left = root.left, root.right
        invertBinTree(root.left)
        invertBinTree(root.right)




BFSPrint(n1)
invertBinTree(n1)
print("\nAfter: ")
BFSPrint(n1)