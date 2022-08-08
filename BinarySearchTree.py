class binarySearchTree():
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

    def insertTree(self, root, key):
        if root is None:
            return binarySearchTree(key)
        else:
            if root.val == key:
                return root
            elif root.val<key:
                root.right=self.insertTree(root.right,key)
            else:
                root.left=self.insertTree(root.left,key)
