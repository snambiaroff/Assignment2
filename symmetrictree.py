from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    if not root:
        return True

    # Create a deque for BFS and add the root's left and right children.
    queue = deque([root.left, root.right])

    while queue:
        # Pop two nodes from the queue for comparison.
        left_node = queue.popleft()
        right_node = queue.popleft()

        # If both nodes are None, they are symmetric.
        if not left_node and not right_node:
            continue
        # If one of the nodes is None or their values don't match, they are not symmetric.
        if not left_node or not right_node or left_node.val != right_node.val:
            return False

        queue.append(left_node.left)
        queue.append(right_node.right)
        queue.append(left_node.right)
        queue.append(right_node.left)

    return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

result = is_symmetric(root)
print(result)
