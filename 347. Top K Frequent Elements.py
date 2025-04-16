class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        outputDir = {}
        for num in nums:
            outputDir[num] = outputDir.get(num, 0) + 1
        
        n = len(nums)
        holderList = [[] for _ in range(n + 1)]
        for num, count in outputDir.items():
            holderList[count].append(num)
        
        op = []
        for count in range(n, 0, -1):
            if holderList[count]:
                op.extend(holderList[count])
            if len(op) >= k:
                return op[:k]