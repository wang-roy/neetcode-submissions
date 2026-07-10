class Solution:
    def __init__(self):
        self.power = 0

    def countBits(self, n: int) -> List[int]:
        output = [0]
        for i in range(1, n+1):
            if pow(2, self.power+1) == i:
                self.power += 1
            if pow(2, self.power) == i:
                output.append(1)
                continue
            
            currPow = pow(2, self.power)
            remainder = i - currPow
            output.append(output[currPow] + output[remainder])
        return output
        