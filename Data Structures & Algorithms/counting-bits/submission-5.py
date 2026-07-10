class Solution:
    def __init__(self):
        self.power = 0

    def countBits(self, n: int) -> List[int]:
        output = [0]
        currPow = pow(2, 0)
        for i in range(1, n+1):
            if currPow * 2 == i:
                currPow *= 2
            if currPow == i:
                output.append(1)
                continue
            
            remainder = i - currPow
            output.append(output[currPow] + output[remainder])
        return output
        