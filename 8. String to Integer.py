class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if not s:
            return 0
        
        signCheck = 1
        index = 0
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                signCheck = -1
            index += 1
        
        op = 0
        while index < len(s) and s[index].isdigit():
            Ndigits = int(s[index])
            op = op * 10 + Ndigits
            index += 1
        
        op *= signCheck
        
        max = 2**31 - 1
        min = -2**31
        
        if op < min:
            return min
        if op > max:
            return max
        
        return op
