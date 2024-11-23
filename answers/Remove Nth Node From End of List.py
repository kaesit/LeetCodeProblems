class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

    


class Solution:
     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
          
          """#*************** ListNode Functions ***************#
        def get_index(Node:ListNode, index:int):
            count = 0
            current = Node
            while current != None:
                if count == index:
                    return current.val
                count+=1
                current = current.next
            return -1
        def length(Node:ListNode):
            current = Node
            count = 0
            while current != None:
                count+=1
                current = current.next
            return count
        def delete_node(Node:ListNode, val):
            current = Node
            temp = current
            prev = None
            if current != None and current.val == val:
                current = temp.next
                del temp
            else:
                while temp != None and temp.val != val:
                    prev = temp
                    temp = temp.next
                if temp == None:
                    print("Can't delete")
                else:
                    prev.next = temp.next

        #*************** ListNode Functions ***************#
        
        #*************** Code ***************#
        if head.val != None and head.next == None:
            head = head.next
        if head != None:
            indices = length(head)
            new = indices - n
            dep = get_index(head, new)
            delete_node(head, dep)
        

        #*************** Code ***************#
        return head"""
          dummy = ListNode(0)
          dummy.next = head
          first = dummy
          second = dummy

          for _ in range(n + 1):
               first = first.next

          while first is not None:
               first = first.next
               second = second.next

          second.next = second.next.next

          return dummy.next