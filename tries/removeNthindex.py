#Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
     def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

     def get_index(self, Node, index:int):
          count = 0
          current = Node
          while current != None:
               if count == index:
                    return current.val
               count+=1
               current = current.next
          return -1
     def length(self, Node):
          current = Node
          count = 0
          while current != None:
               count+=1
               current = current.next
          return count


class Solution:
     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
          #temp = head
          #prev = None
          print(head.get_index(head, 0))
          if head.val != None and head.next == None:
               head = head.next
          if head != None:
               print("match!")
               lg = head.length(head)
               

          return head
     
a = ListNode(5, None)
values = (1)
head = ListNode(values, None)
print(a.get_index(a, 0))
print(a.length(a))
print(Solution().removeNthFromEnd(head, 1))