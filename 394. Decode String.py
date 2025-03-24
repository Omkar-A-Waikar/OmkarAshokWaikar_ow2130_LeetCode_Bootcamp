class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []         
        currentString = "" 
        currentCharNums = 0   

        for char in s:
            if char.isdigit():
                currentCharNums = currentCharNums * 10 + int(char)
            elif char == '[':
                stack.append((currentString, currentCharNums))
                currentString = ""
                currentCharNums = 0
            elif char == ']':
                prev_str, num = stack.pop()
                currentString = prev_str + num * currentString
            else:
                currentString += char

        return currentString