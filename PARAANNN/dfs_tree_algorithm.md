# Assessment 3.6: DFS Methods in Tree — Algorithm

**Name:** Jepald Paran

## Tree

```
                 J
              /     \
            E         R
           / \       / \
          A   L     D   P
         / \ / \
        A  R A  N
```

Depth-First Search (DFS) goes as deep as possible down one branch before backtracking. For a binary tree, it has three forms, which differ only in *when* the root of each subtree is visited.

## 1. Preorder (Root → Left → Right)

```
ALGORITHM Preorder(node)
  1. START
  2. IF node is NULL THEN RETURN
  3. VISIT node (record node.data)
  4. CALL Preorder(node.left)
  5. CALL Preorder(node.right)
  6. END
```

**Result:** J - E - A - A - R - L - A - N - R - D - P

## 2. Inorder (Left → Root → Right)

```
ALGORITHM Inorder(node)
  1. START
  2. IF node is NULL THEN RETURN
  3. CALL Inorder(node.left)
  4. VISIT node (record node.data)
  5. CALL Inorder(node.right)
  6. END
```

**Result:** A - A - R - E - A - L - N - J - D - R - P

## 3. Postorder (Left → Right → Root)

```
ALGORITHM Postorder(node)
  1. START
  2. IF node is NULL THEN RETURN
  3. CALL Postorder(node.left)
  4. CALL Postorder(node.right)
  5. VISIT node (record node.data)
  6. END
```

**Result:** A - R - A - A - N - L - E - D - P - R - J

## Main Program

```
  1. START
  2. BUILD the tree (root = J)
  3. CALL Preorder(root)  and display the result
  4. CALL Inorder(root)   and display the result
  5. CALL Postorder(root) and display the result
  6. END
```

## Complexity

- Time: O(n) — every node is visited exactly once
- Space: O(h) — recursion stack depth equals the tree height h
