class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        mp = {}
        ans = []
        for point in points:
            x, y = point[0], point[1]
            d = (x*x) + (y*y)
            distances.append(d)
            if d in mp:
                mp[d].append(point)
            else:
                mp[d] = [point]
        
        heapq.heapify(distances)
        while k > 0:
            d = heapq.heappop(distances)
            point = mp[d].pop()
            ans.append(point)
            k -= 1
        
        return ans