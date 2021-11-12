class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Codec:
    def __init__(self):
        self.ret = ''
        self.dataArray = []

    def rserialize(self, root):
        if not root:
            self.ret += "None"
        else:
            self.ret += str(root.val) + ','
            self.rserialize(root.next)

    def serialize(self, root):
        self.rserialize(root)
        return self.ret

    def rdeserialize(self):
        if not self.dataArray or self.dataArray[0] == 'None':
            return None

        root = ListNode(int(self.dataArray[0]))
        self.dataArray.pop(0)
        root.next = self.rdeserialize()
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
