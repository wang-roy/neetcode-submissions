class Solution:
    def hammingWeight(self, n: int) -> int:
        # currentNum = 1
        # numOnes = 0
        # while currentNum <= n:
        #     print(currentNum)
        #     if currentNum & n:
        #         numOnes += 1
        #     currentNum = currentNum << 1
        # return numOnes

        numOnes = 0
        num = n
        while num > 0:
            if num % 2 == 1:
                numOnes += 1
            num = num >> 1
        return numOnes
            