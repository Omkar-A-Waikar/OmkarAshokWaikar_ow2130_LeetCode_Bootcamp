class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        
        op = []
        pLength, sLength = len(p), len(s)
        
        pCounter = [0] * 26
        windowCount = [0] * 26
        
        for i in range(pLength):
            pCounter[ord(p[i]) - ord('a')] += 1
            windowCount[ord(s[i]) - ord('a')] += 1
        
        if windowCount == pCounter:
            op.append(0)
        
        for i in range(pLength, sLength):
            windowCount[ord(s[i]) - ord('a')] += 1
            windowCount[ord(s[i - pLength]) - ord('a')] -= 1
            
            if windowCount == pCounter:
                op.append(i - pLength + 1)
        
        return op
