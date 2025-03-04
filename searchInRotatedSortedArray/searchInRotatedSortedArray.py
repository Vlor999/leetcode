#! /usr/bin/env python3

class Solution:
    def classiqueSearch(self, nums: list[int], target: int, debut: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid + debut
        return -1

    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left
        if target >= nums[pivot] and target <= nums[-1]:
            return self.classiqueSearch(nums[pivot:], target, pivot)
        else:
            return self.classiqueSearch(nums[:pivot], target, 0)

    
def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.search(Input[0], Input[1])
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [
        ([3, 4, 5, 6, 1, 2], 1, 4), 
        ([3, 5, 6, 0, 1, 2], 4, -1), 
        ([10, 11, 13, 15, 17, 18], 10, 0),
        ]
    for input in dicoElem:
        output = input[-1]
        input = input[0:-1]
        gereInput(input, output)

if __name__ == "__main__":
    main()