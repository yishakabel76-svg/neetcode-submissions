class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        result = []
        freq = {}
        for num in nums:
            freq[num]=freq.get(num, 0)+1
        heap = []
        for num , f in freq.items():
            heapq.heappush(heap,(f,num))
            if len(heap)>k:
                heapq.heappop(heap)
        for f, num in heap :
            result.append(num)
        return result

        