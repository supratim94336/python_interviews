# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        if n > length:
            return head
        
        if length == n:
            return head.next
            
        temp = head
        curr = None
        next_ = None
        count = 0

        while count < (length - n):
            curr = temp
            next_ = temp.next.next
            temp = temp.next
            count += 1
            
        curr.next = next_
        
        return head

# list to linkedlist
def lst2link(lst):
  cur = dummy = ListNode(0)
  for e in lst:
      cur.next = ListNode(e)
      cur = cur.next
  return dummy.next

# print linkedlist
def print_ll(head: ListNode):
    s = ""
    values = []
    temp = head
    while temp:
        values.append(str(temp.val))
        temp = temp.next
    return "-->".join(values)

input_ = [9,0,3,8,7,3,8,6,3,1]
print_ll(lst2link(input_))
# '9-->0-->3-->8-->7-->3-->8-->6-->3-->1'
print_ll(removeNthFromEnd(lst2link(input_), 10))
# '0-->3-->8-->7-->3-->8-->6-->3-->1'
