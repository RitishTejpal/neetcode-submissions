"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = []
        q.append(node)
        mp = defaultdict(Node)

        head = Node(node.val)
        mp[node] = head
        
        for nei in node.neighbors:
            q.append(nei)

        while q:
            curr = q.pop(0)
            if curr not in mp: mp[curr] = Node(curr.val)
            for neighbor in curr.neighbors:
                if neighbor in mp:
                    continue
                q.append(neighbor)
        
        for old, new in mp.items():
            for nei in old.neighbors:
                new.neighbors.append(mp[nei])
        
        return head