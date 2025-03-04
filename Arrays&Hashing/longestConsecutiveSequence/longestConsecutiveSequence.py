#! /usr/bin/env python3

class Solution:
    

    def __init__(self):
        dicoNextVal = {}


    def getStartsElements(self, dicoPrev:dict[int: bool])->list[int]:
        listPrev = []
        for number in dicoPrev:
            if not dicoPrev[number]:
                listPrev.append(number)
        return listPrev

    def getLength(self, start:int, dicoNext:dict[int:bool])->int:
        taille = 1
        current = start
        while dicoNext[current]:
            taille += 1
            current += 1
        return taille

    def longestConsecutive(self, nums: list[int]) -> int:
        dicoNext = {}
        dicoPrev = {}
        setElements = set(nums)
        
        if len(nums) == 0:
            return 0
        for elem in setElements:
            dicoNext[elem] = elem + 1 in setElements
            dicoPrev[elem] = elem - 1 in setElements
        currentLongest = 1
        listStartElem = self.getStartsElements(dicoPrev)
        for start in listStartElem:
            lenght = self.getLength(start, dicoNext)
            if lenght > currentLongest:
                currentLongest = lenght
        return currentLongest


def main():
    mainSolution = Solution()
    currentInput = [0,3,7,2,5,8,4,6,0,1]
    outputListe = mainSolution.longestConsecutive(currentInput)
    print(outputListe)

    currentInput = [100,4,200,1,3,2]
    outputListe = mainSolution.longestConsecutive(currentInput)
    print(outputListe)
    return outputListe

if __name__ == "__main__":
    output = main()
    print(output)