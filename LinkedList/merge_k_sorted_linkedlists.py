# Definition for singly-linked list.

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    len_lists = len(lists)
    
    if lists is None or len_lists == 0:
        return []
    
    if len_lists == 1:
        return lists[0]
    
    def merge_two_lists(l1, l2):
        first_node = ListNode()
        tail = first_node
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        while l1:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
            
        while l2:
            tail.next = l2
            l2 = l2.next
            tail = tail.next
            
        return first_node.next

    while len(lists) > 1:

        answer = []
        for i in range(0, len(lists), 2):
            left_arr = lists[i]
            if i+1 < len(lists):
                right_arr = lists[i+1]
            else:
                right_arr = None

            answer.append(merge_two_lists(left_arr, right_arr))
        lists = answer
    return lists[0]

## test
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(5)
l4 = ListNode(1)
l5 = ListNode(3)
l6 = ListNode(4)
l7 = ListNode(2)
l8 = ListNode(6)

l1.next = l2
l2.next = l3
l3.next = None

l4.next = l5
l5.next = l6
l6.next = None

l7.next = l8
l8.next = None

lists = [l1, l4, l8]

x = mergeKLists(lists)

# to print
complete = []
while x is not None:
    complete.append(str(x.val))
    x = x.next
print("-->".join(complete))
