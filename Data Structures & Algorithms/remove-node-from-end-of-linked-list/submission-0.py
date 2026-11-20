
class Solution:
    def removeNthFromEnd(self, head, n):

        nodes = []
        curr = head

        # Store all nodes
        while curr:
            nodes.append(curr)
            curr = curr.next

        # Find node to remove
        index = len(nodes) - n

        # If removing head
        if index == 0:
            return head.next

        # Reconnect previous node to next node
        nodes[index - 1].next = nodes[index].next

        return head
