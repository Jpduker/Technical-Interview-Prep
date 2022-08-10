from collections import deque
from re import L


class Node():
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val

    def levelOrder(self, root):
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            for i in range(len(level)):
                node = queue.pop()
                if node:
                    level.append(node)
                    queue.append(root.left)
                    queue.append(root.right)
            if level:
                result.append(level)
        return result
