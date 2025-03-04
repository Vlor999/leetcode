#! /usr/bin/env python3

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[right]: 
                return nums[left]
            if nums[mid] > nums[left]:
                left = mid
            else :
                right = mid
            print(left,right)
        return nums[(left + 1) % len(nums)]

def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.findMin(Input)
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [
        ([3,4,5,1,2], 1), 
        ([4,5,6,7,0,1,2], 0), 
        ([10, 11,13,15,17,18], 10),
        ]
    for input in dicoElem:
        output = input[-1]
        input = input[0]
        gereInput(input, output)

if __name__ == "__main__":
    main()