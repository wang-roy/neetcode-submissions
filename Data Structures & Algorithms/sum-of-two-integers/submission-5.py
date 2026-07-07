class Solution:
    def getSum(self, a: int, b: int) -> int:
        carryOver = 0
        result = 0
        mask = pow(2, 32)-1
        for i in range(0, 32):
            aBit = (a >> i) & 1
            bBit = (b >> i) & 1
            sumBit = aBit ^ bBit ^ carryOver
            carryOver = (aBit & bBit) | (aBit & carryOver) | (bBit & carryOver)
            if sumBit == 1:
                result |= (1 << i)
        
        if result > pow(2, 31):
            result = ~(result ^ mask)
        return result