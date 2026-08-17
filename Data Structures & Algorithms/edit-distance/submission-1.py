class Solution:
    def __init__(self):
        self.memo = {}
    def minDistance(self, word1: str, word2: str) -> int:
        if self.memo.get(word1 + "," + word2, None) != None:
            return self.memo[word1 + "," + word2]
        if not word1 or not word2:
            return abs(len(word1)-len(word2))

        if word1[0] == word2[0]:
            equalOps = self.minDistance(word1[1:], word2[1:])
            if equalOps < self.memo.get(word1 + "," + word2, float("inf")):
                self.memo.update({word1 + "," + word2: equalOps})
            return equalOps
        else:
            insertOps = self.minDistance(word1, word2[1:])
            deleteOps = self.minDistance(word1[1:], word2)
            replaceOps = self.minDistance(word1[1:], word2[1:])
            minOps = min(insertOps, deleteOps, replaceOps) + 1
            if minOps < self.memo.get(word1 + "," + word2, float("inf")):
                self.memo.update({word1 + "," + word2: minOps})
            return minOps
        
