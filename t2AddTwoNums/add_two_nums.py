"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked
list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
题⽬⼤意
2 个逆序的链表，要求从低位开始相加，得出结果也逆序输出，返回值是逆序结果链表的头结点。
<p>
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNums(self, first: ListNode, second: ListNode):
    # 1.初始化一个临时虚拟节点(0)
    dummy = ListNode(0)
    # 2.定义临时变量
    current = dummy
    # 3.定义每一轮的余数(进位)
    carry = 0
    while first or second:
        x = 0
        if first:
            x = first.val
        y = 0
        if second:
            y = second.val
        # 补上一轮进位的余数
        sums = carry + x + y
        carry = sums / 10
        # 下一节点指向本轮各节点和的商值
        current.next = ListNode(sums % 10)
        # 开启下一轮循环(节点位置向下移动)
        current = current.next
        if first:
            first = first.next
        if second:
            second = second.next
    # 余数超过0进位末位节点
    if carry > 0:
        current.next = ListNode(carry)
    return dummy.next
