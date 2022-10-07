# 🌳 Tree - Binary Tree

### Prerequisites:

* [X]  [Recursion](../(4)%20Recursion)

### Contents:

* [Binary Tree]()
  * Create `Node`.
  * Create `Tree`.
* [Tree Traverse]()
  * `Pre-order` traverse.
  * `Post-order` traverse.
  * `In-order` traverse.
* <span style="color: gray;">EXTRA</span>: Tracking Parent Node.

`If we wanted, 'stack' can be applied instead of 'recursion' for the algorithms.`

Used In: `Tree clone, binary search tree`

How to get the parent node of a node?
➡️

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
  
    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self
```
