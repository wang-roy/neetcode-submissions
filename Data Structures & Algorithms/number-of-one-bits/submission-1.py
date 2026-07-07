class Solution:
    def hammingWeight(self, n: int) -> int:
        currentNum = 1
        numOnes = 0
        while currentNum <= n:
            print(currentNum)
            if currentNum & n:
                numOnes += 1
            
            currentNum = currentNum << 1
        return numOnes
            