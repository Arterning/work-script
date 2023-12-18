class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    # 定义一个辅助函数，用于合并两个有序链表
    def mergeTwoLists(l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            return l2

    # 使用分治法将链表两两合并
    while len(lists) > 1:
        new_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged_list = mergeTwoLists(lists[i], lists[i + 1])
                new_lists.append(merged_list)
            else:
                new_lists.append(lists[i])
        lists = new_lists

    return lists[0]


# 示例
# 创建链表1: 1 -> 4 -> 5
l1 = ListNode(1, ListNode(4, ListNode(5)))
# 创建链表2: 1 -> 3 -> 4
l2 = ListNode(1, ListNode(3, ListNode(4)))
# 创建链表3: 2 -> 6
l3 = ListNode(2, ListNode(6))

# 合并链表 [l1, l2, l3]
lists = [l1, l2, l3]
merged = mergeKLists(lists)

# 打印合并后的链表
while merged:
    print(merged.val, end=" -> ")
    merged = merged.next
