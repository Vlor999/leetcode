#! /usr/bin/env python3

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            iNums1 = (left + right) // 2
            iNums2 = (m + n + 1) // 2 - iNums1
            
            maxLeft1 = float("-inf") if iNums1 == 0 else nums1[iNums1 - 1]
            minRight1 = float("inf") if iNums1 == m else nums1[iNums1]
            maxLeft2 = float("-inf") if iNums2 == 0 else nums2[iNums2 - 1]
            minRight2 = float("inf") if iNums2 == n else nums2[iNums2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = iNums1 - 1
            else:
                left = iNums1 + 1
    
def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.findMedianSortedArrays(Input[0], Input[1])
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")

def main():
    dicoElem = [
        ([1,3], [2], 2.00000), 
        ([2], [1,3],2.00000), 
        ([1,2], [3], 2.00000),
        ([1,2], [3,4], 2.50000), 
        ]
    for input in dicoElem:
        output = input[-1]
        input = input[0:-1]
        gereInput(input, output)

if __name__ == "__main__":
    main()