#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        walk1=l1
        walk2=l2
        done_walking=False
        root_output=res_walker=ListNode(0)
        tail_pointer=None
        if walk1 == None and walk2 == None:
            done_walking=True
        while done_walking==False:
            if walk1 == None and walk2 == None:
                done_walking=True
                continue
            elif walk1 == None:
                num=walk2.val + res_walker.val
                walk2=walk2.next
            elif walk2 == None:
                num=walk1.val + res_walker.val
                walk1=walk1.next

            else:
                num = walk1.val + walk2.val + res_walker.val
                walk2=walk2.next
                walk1=walk1.next

            
            carryover=int(num/10)
            res_walker.val=int(num%10)
            res_walker.next=ListNode(carryover)
            tail_pointer=res_walker
            res_walker=res_walker.next
            
        
        if res_walker.val==0:
            tail_pointer.next=None
            
        return root_output

     
    
    def makeTheNumber(self, l1: ListNode):
        temp=l1
        num=0
        arr=[]
        multiplier=1
        while temp != None:
            arr.append(temp.val)
            num=num + (temp.val*multiplier)
            multiplier*=10
            temp=temp.next
        return num
    
    def makeTheList(self, num):
        temp=num
        root = curr_node=ListNode(int(temp%10))
        temp=temp/10        
        while temp>=1:
            curr_node.next = ListNode(int(temp%10))
            temp=temp/10            
            curr_node=curr_node.next

        return root



temp = Solution()
l1=temp.makeTheList(342)
l2=temp.makeTheList(465)
temp.addTwoNumbers(l1,l2)