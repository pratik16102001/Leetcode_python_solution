# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Solution:
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        tot1 = 0
        tot2 = 0
        
        i = 0
        while (l1):
            tot1 = tot1 + l1.val*(10**i)
            i = i+1
            l1 = l1.next
            
        i = 0
        while (l2):
            tot2 = tot2 + l2.val*(10**i)
            i = i+1
            l2 = l2.next
            
        tot = tot1 + tot2
        num_map = map(int, str(tot))
        ans = list(num_map)
        
        l3 = None
        for num in ans:
            newNode = ListNode(num)
            newNode.next = l3
            l3 = newNode
            
        return l3