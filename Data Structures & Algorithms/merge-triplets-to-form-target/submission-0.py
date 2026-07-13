class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        foundFirst, foundSecond, foundThird = False, False, False
        for ai, bi, ci in triplets:
            if not foundFirst and (ai == x and bi <= y and ci <= z):
                foundFirst = True
            if not foundSecond and (ai <= x and bi == y and ci <= z):
                foundSecond = True
            if not foundThird and (ai <= x and bi <= y and ci == z):
                foundThird = True

        return foundFirst and foundSecond and foundThird