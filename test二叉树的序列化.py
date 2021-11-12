from 二叉树序列和反序列 import TreeNode, Codec
a = "1,2,3,None,None,None,None"
cer = Codec()
root = cer.deserialize(a)
s = cer.serialize(root)
print(s)
