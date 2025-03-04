#! /usr/bin/env python3

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        position = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return position


def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.search(Input[0], Input[1])
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [([-1,0,3,5,9,12], 9, 4), ([-1,0,3,5,9,12], 2, -1), ([5], 5, 0)]
    for input in dicoElem:
        output = input[-1]
        input = input[0:2]
        gereInput(input, output)

if __name__ == "__main__":
    main()