class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        modOperation = 10**9 + 7
        str = [0] * (n + 1)
        str[1] = 1  
        
        for i in range(1, n + 1):
            if str[i] > 0:
                start = i + delay
                end = min(n, i + forget - 1)
                for j in range(start, end + 1):
                    str[j] = (str[j] + str[i]) % modOperation
        
        op = 0
        for i in range(max(1, n - forget + 1), n + 1):
            op = (op + str[i]) % modOperation
        
        return op
