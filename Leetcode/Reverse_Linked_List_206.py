'''
Docstring for Leetcode.Reverse_Linked_List_206
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''
from typing import Optional

# 1. The definition for a singly-linked list (Uncommented from your snippet)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Your exact Solution class
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0)
        curr = head
        while curr:
            nxt = curr.next
            curr.next = d.next
            d.next = curr 
            curr = nxt 
        return d.next

# ==========================================
# DRIVER CODE (To test and run it locally)
# ==========================================

def print_list(node: Optional[ListNode]):
    """Helper function to print the linked list in a readable format."""
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values) if values else "Empty List")

def create_list(values: list) -> Optional[ListNode]:
    """Helper function to turn a standard Python list into a Linked List."""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

if __name__ == "__main__":
    # Create a test case: 1 -> 2 -> 3 -> 4 -> 5
    my_test_values = [1, 2, 3, 4, 5]
    head_of_list = create_list(my_test_values)
    
    print("Original List:")
    print_list(head_of_list)

    # Initialize your Solution class and call the method
    sol = Solution()
    reversed_head = sol.reverseList(head_of_list)

    print("\nReversed List:")
    print_list(reversed_head)