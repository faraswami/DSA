class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def printInorder(root):
    stack = []
    current = root

    while stack or current:

        while current:
            stack.append(current)
            current = current.left

        # Current is None at this point
        current = stack.pop()
        print(current.data, end=" ")

        # Visit the right subtree
        current = current.right


def printInorderRecur(root):

    if root:
        printInorderRecur(root.left)
        print(root.data),
        printInorderRecur(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

printInorder(root)
printInorderRecur(root)
