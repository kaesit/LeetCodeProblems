class Solution:
     def isPalindrome(self, head: Optional[ListNode]) -> bool:
          lst = []
          while head:
               lst.append(head.val)
               head = head.next
          if lst[0::] == lst[::-1]:
               return True
          return False