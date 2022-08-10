from collections import deque


class Node():
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


class Solution:
    def levelOrder(self, root):
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                result.append(level)
        return result


root1 = Node(3)
root1.left = Node(9)
root1.right = Node(20)
root1.right.left = Node(15)
root1.right.right = Node(7)
sln = Solution()
print(sln.levelOrder(root1))
