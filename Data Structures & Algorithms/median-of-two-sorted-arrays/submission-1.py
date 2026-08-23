class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(A: List[int], B: List[int], k: int) -> int:
            if len(A) > len(B):
                tmp = A
                A = B
                B = tmp
            if len(A) == 0:
                return B[k-1]
            if k == 1:
                return min(A[0], B[0])
            
            i = min(len(A), k//2)
            j = min(len(B), k//2)

            if A[i - 1] <= B[j - 1]:
                return getKthElement(A[i:], B, k - i)
            else:
                return getKthElement(A, B[j:], k - j)
        
        m = len(nums1)
        n = len(nums2)
        k = (m + n + 2) // 2
        mid = getKthElement(nums1, nums2, k)
        mid_m_1 = getKthElement(nums1, nums2, k-1)
        print(mid)
        print(mid_m_1)
        if (m + n) % 2 == 0:
            return (mid + mid_m_1)/2
        return mid
            
        

        


