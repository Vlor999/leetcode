#! /usr/bin/env python3

class Solution:
    def trap(self, heights):
        if heights == []:
            return 0
        
        gauche, droite= 0, len(heights) - 1
        hauteurGaucheMax, hauteurDroiteMax = heights[gauche], heights[droite]
        volume = 0

        while gauche < droite:
            if hauteurGaucheMax < hauteurDroiteMax:
                gauche += 1
                hauteurGaucheMax = max(hauteurGaucheMax, heights[gauche])
                volume += max(0,hauteurGaucheMax - heights[gauche] )
            else:
                droite -= 1
                hauteurDroiteMax = max(hauteurDroiteMax, heights[droite])
                volume+= max(0, hauteurDroiteMax - heights[droite])
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