class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.ret = ''
        self.dataArray = []

    def rserialize(self, root):
        if not root:
            self.ret += "None,"
        else:
            self.ret += str(root.val) + ','
            self.rserialize(root.left)
            self.rserialize(root.right)

    def serialize(self, root):
        self.rserialize(root)
        return self.ret

    def rdeserialize(self):
        if not self.dataArray:
            return None
        if self.dataArray[0] == 'None':
            self.dataArray.pop(0)
            return None
        
        root = TreeNode(int(self.dataArray[0]))
        self.dataArray.pop(0)
        root.left = self.rdeserialize()
        root.right = self.rdeserialize()
        return root

    def deserialize(self, data):
        s = ''
        for ch in data:

            if ch == ',':
                self.dataArray.append(s)
                s = ''
            else:
                s += ch
        if s:
            self.dataArray.append(s)
        print(self.dataArray)

        return self.rdeserialize()
