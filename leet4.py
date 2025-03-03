class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3=[]
        size=len(nums1)
        for i in range(size):
            num3.append(nums1[i])

        size=len(nums2)
        for i in range(size):
            num3.append(nums2[i])

        size=len(num3)
        num3.sort()
        print(num3)
        if(size%2==0):
            median=(num3[size//2]+num3[size//2 - 1])/2
            return median
        else:
            median=num3[size//2]
            return median


        