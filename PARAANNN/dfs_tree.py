# DFS Methods in Tree - JEPALD PARAN
# Assessment 3.6: DFS Method in Tree (based on Assessment 3.5)
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


def inorder(node, result=None):
    """Left -> Root -> Right"""
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.data)
        inorder(node.right, result)
    return result


def postorder(node, result=None):
    """Left -> Right -> Root"""
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.data)
    return result


if __name__ == "__main__":
    root = build_tree()
    print("=== DFS METHODS IN TREE ===")
    print("1) PREORDER :", "-".join(preorder(root)))
    print("2) INORDER  :", "-".join(inorder(root)))
    print("3) POSTORDER:", "-".join(postorder(root)))
