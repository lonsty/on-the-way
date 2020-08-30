class Solution:
    min_num = -2**31
    max_num = 2**31 - 1
    
    def reverse(self, x: int) -> int:
        if x >= 0:
            ans = int(str(x)[::-1])
        else:
            ans = int('-' + str(x)[1:][::-1])
            
        if (ans < self.min_num) or (ans > self.max_num):
            ans = 0

        return ans
