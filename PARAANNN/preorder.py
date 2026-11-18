# Preorder Traversal - JEPALD PARAN
# Assessment 3.6: DFS Method in Tree
#
#                 J
#              /     \
#            E         R
#           / \       / \
#          A   L     D   P
#         / \ / \
#        A  R A  N


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    root = Node("J")
    root.left = Node("E")
    root.right = Node("R")
    root.left.left = Node("A")
    root.left.right = Node("L")
    root.right.left = Node("D")
    root.right.right = Node("P")
    root.left.left.left = Node("A")
    root.left.left.right = Node("R")
    root.left.right.left = Node("A")
    root.left.right.right = Node("N")
    return root


def preorder(node, result=None):
    """Root -> Left -> Right"""
    if result is None:
        result = []
    if node:
        result.append(node.data)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


if __name__ == "__main__":
    root = build_tree()
    print("=== PREORDER ===")
    print("Preorder:", "-".join(preorder(root)))
