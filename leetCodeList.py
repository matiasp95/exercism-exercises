
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        stub = ListNode(0)
        current = stub
        while (l1 != None or l2 != None or carry !=0):
            partRes = 0
            if (l1):
                partRes += l1.val
                l1 = l1.next
            else:
                l1 = None
            if (l2):
                partRes += l2.val
                l2 = l2.next
            else:
                l2 = None
            partRes += carry
            carry = partRes // 10
            aux = ListNode(partRes % 10)
            current.next = aux
            current = current.next
        return stub.next
    ###
    # Here ends the challenge, below is the code to test locally
    ### 
    def seeList(self, x: Optional[ListNode]):
        aux = x
        print(aux.val)
        while aux.next != None:
            aux = x.next
            print(aux.val)
            x = x.next

sl = Solution()
list1 = ListNode(2,ListNode(4, ListNode(3)))
list2 = ListNode(5,ListNode(6, ListNode(4)))

#xd = sl.addTwoNumbers(list1, list2)
print(sl.seeList(list1))
