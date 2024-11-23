class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle(head):
    if head is None or head.next is None:
        return head
    slow,fast = head,head.next # slow,fast = head,head generly rabit tortise need to head.next to
    # Fast is taken as head.next, to grab the last element of first half in "slow" and make it's next as None
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next
    return slow

def merge(h1,h2):
    temp = ListNode(-1) 
    curr = temp
    while h1 is not None and h2 is not None:
        if h1.val<=h2.val:
            temp.next = h1
            h1 = h1.next
        else:
            temp.next = h2
            h2 = h2.next
        temp =  temp.next
   

    if h1 is not None:
        temp.next = h1

    if h2 is not None:
        temp.next = h2

    return curr.next



def sort(head):
    if head is None or head.next is None:
        return head

    mid = middle(head)
    right = mid.next
    mid.next = None
    left = head
    left = sort(left)
    right = sort(right)
    return merge(left,right)

class Main():
     head = ListNode()
     sort(head)
     

if __name__ == '__main__':
     Main()