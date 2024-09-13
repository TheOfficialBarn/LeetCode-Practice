class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, 'b').zfill(32)[::-1],2)
    
# OR

class Solution2:
    def reverseBits(self, n: int) -> int:
        return int(format(n, '032b')[::-1],2)
    
class Solution3:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            lsb = n & 1
            res = res << 1
            res = res | lsb
            n = n >> 1
        return res