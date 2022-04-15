class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        has_incoming = set([v for u,v in edges])
        return list(set(range(n)).difference(has_incoming))
