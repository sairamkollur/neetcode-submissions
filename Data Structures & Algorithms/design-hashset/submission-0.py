class ListNode:
    def __init__(self, key, next_node=None):
        self.key = key
        self.next = next_node

class MyHashSet:
    def __init__(self):
        # Create a list of 'dummy' head nodes to simplify insertion/deletion
        self.size = 10**4
        self.set = [ListNode(0) for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        cur = self.set[self._hash(key)]
        while cur.next:
            if cur.next.key == key:
                return  # Key already exists, no need to add
            cur = cur.next
        # Add new node at the end of the chain
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[self._hash(key)]
        while cur.next:
            if cur.next.key == key:
                # Bypass the node to delete it
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[self._hash(key)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False