class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        curr = 0
        down = False
        
        for ch in s:
            rows[curr] += ch
            
            if curr == 0 or curr == numRows - 1:
                down = not down
            
            if down:
                curr += 1
            else:
                curr -= 1
        
        return ''.join(rows)