# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node, return head
        if not head or not head.next:
            return head
        
        # Initialize a dummy node to easily handle the head swap and pointer manipulations
        dummy = ListNode()
        dummy.next = head
        
        # Initialize pointers p1 and p2 to the first two nodes in the list
        p1 = head
        p2 = head.next
        
        # Save the second node (p2) to make it the new head of the list after the first swap
        holder = head.next
        
        # Perform the first pair swap
        p1.next = p2.next  # Point p1 (first node) to the node after p2 (second node)
        p2.next = p1       # Point p2 to p1, effectively swapping the first two nodes
        dummy.next = holder # Update dummy's next to point to the new head of the list (p2)
        
        # Set prev to p1 (the second node after the first swap) to use it for linking in further swaps
        prev = p1
        
        # Check if there are more pairs left to swap
        if not p1.next or not p1.next.next or not p1.next.next.next:
            return dummy.next
        
        # Move p1 and p2 to the next pair for further swaps
        p2 = p2.next.next.next
        p1 = p1.next

        # Continue swapping pairs in the remaining list
        while True:
            # Save the current second node in the next pair (p2) to make it the new "first" in this swap
            holder = p2
            
            # Swap the next pair of nodes
            p1.next = p2.next  # Point p1 to the node after p2
            p2.next = p1       # Point p2 to p1 to complete the swap
            prev.next = holder  # Link the previous swapped pair to the current swapped pair
            
            # Check if there are more pairs to swap, break the loop if not
            if not p1.next or not p1.next.next or not p1.next.next.next:
                break
            
            # Move prev, p1, and p2 pointers to the next pair for further swaps
            prev = p1
            p1 = p1.next
            p2 = p2.next.next.next
        
        # Return the new head of the modified list
        return dummy.next
