#! /usr/bin/env python3

class Solution:
    def canEat(self, piles: list[int], speed: int, h: int) -> bool:
        currentTemps = 0
        for banana in piles:
            currentTemps += (banana + speed - 1) // speed
            if currentTemps > h :
                return False
        return currentTemps <= h

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        minVitesse, maxVitesse = 1, max(piles)
        while minVitesse < maxVitesse:
            mid = (minVitesse + maxVitesse) // 2
            if self.canEat(piles, mid, h):
                maxVitesse = mid
            else:
                minVitesse = mid + 1
        return minVitesse

def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.minEatingSpeed(Input[0], Input[1])
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [
        ([3,6,7,11], 8, 4), 
        ([30,11,23,4,20], 5, 30), 
        ([30,11,23,4,20], 6, 23), 
        ]
    for input in dicoElem:
        output = input[-1]
        input = input[0:2]
        gereInput(input, output)

if __name__ == "__main__":
    main()