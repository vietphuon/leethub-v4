class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        
        # Sentinel nodes: head = LRU end, tail = MRU end
        self.head = Node(0, 0)  # least recent
        self.tail = Node(0, 0)  # most recent
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node) -> Node:
        # Remove node from its current position
        # ... -> prev -> node -> nxt -> ...
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        node.next, node.prev = None, None
        return node

    def _insert_tail(self, node):
        # Insert node right before tail (most recent position)
        # ... -> tail -> none => ... -> tail -> node (new tail) -> none
        tmp = self.tail.prev
        tmp.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = tmp

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move to most recent position
            self._remove(node)
            self._insert_tail(node)

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to most recent
            ...
        else:
            # Create new node, add to cache and list
            new = Node(key, value)

            self.cache[key] = new

            tmp = self.tail.prev
            self.tail.prev = new
            new.prev = tmp
            tmp.next = new
            new.next = self.tail

            # Evict LRU if over capacity
            if len(self.cache) > self.capacity:
                # LRU node is right after head
                # none -> head -> lru -> lru-1 -> ...
                lru_node = self.head.next
                self._remove(lru_node)

                self.cache.pop(lru_node.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)