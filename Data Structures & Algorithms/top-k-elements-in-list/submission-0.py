class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        heap = [(-v, k) for k, v in mp.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result