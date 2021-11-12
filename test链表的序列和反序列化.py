from 链表的序列和反序列化 import ListNode, Codec

def reverseList(head):
    # 为什么使用这个方式赋值会报错？

    # pre= head
    # pre.next = None
    # cur = head.next
    pre = None
    cur = head
    while cur:
        print(cur.val)
        n = cur.next
        cur.next = pre
        pre = cur
        cur = n

    return pre

a = "1,2,3,4,5"
cer = Codec()
root = cer.deserialize(a)
r2 = reverseList(root)
s = cer.serialize(r2)
print(s)
