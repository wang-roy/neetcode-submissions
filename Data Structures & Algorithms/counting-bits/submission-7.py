class Solution:
    def __init__(self):
        self.power = 0

    def countBits(self, n: int) -> List[int]:
        output = [0]
        currPow = pow(2, 0)
        for i in range(1, n+1):
            
            remainder = i - currPow
            print(output)
            print(f"remainder: {remainder}")
            if remainder == currPow:
                currPow += remainder
                remainder = 0
            if remainder == 0:
                output.append(1)
                continue
            print(currPow)
            output.append(output[currPow] + output[remainder])
            
        return output
        