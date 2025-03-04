#! /usr/bin/env python3

class Solution:
    def trap(self, heights):
        volume = 0
        if heights == []:
            return volume
        
        left, right = 0, len(heights) - 1
        maxLeft, maxRight = heights[left], heights[right]

        while left < right:
            if maxLeft < maxRight:
                maxLeft = max(maxLeft, heights[left + 1])
                volume += max(0, maxLeft - heights[left+1])
                left += 1
            else:
                maxRight = max(maxRight, heights[right - 1])
                volume += max(0, maxRight - heights[right - 1])
                right -= 1
        return volume


def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.trap(Input)
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [([0,1,0,2,1,0,1,3,2,1,2,1], 6), ([4,2,0,3,2,5], 9), ([0,2,0,3,1,0,1,3,2,1], 9)]
    for input in dicoElem:
        output = input[1]
        input = input[0]
        gereInput(input, output)

if __name__ == "__main__":
    main()