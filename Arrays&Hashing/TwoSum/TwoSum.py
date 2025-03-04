#! /usr/bin/env python3

class Solution:
    def __init__(self):
        pass

    def realList(self, nums:list[int], target: int) -> list[int]:
        newDico = {}
        compteurPosition = 0
        for elem in nums:
            # if elem <= target:
            if elem not in newDico : 
                newDico[elem] = [compteurPosition]
            else:
                newDico[elem].append(compteurPosition)
            compteurPosition += 1
        return newDico, compteurPosition

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        currentDico, position = self.realList(nums, target)
        if currentDico == None : 
            return [position]
        for currentElement in currentDico:
            listPositionCurrentElement = currentDico[currentElement]
            expected = target - currentElement
            if currentElement == expected :
                if len(listPositionCurrentElement) > 1 :
                    return [listPositionCurrentElement[0], listPositionCurrentElement[1]]
                else:
                    continue
            if expected in currentDico :
                listPositonExpectedElement = currentDico[expected] 
                return [listPositionCurrentElement[0], listPositonExpectedElement[0]]
        return []
        

def main():
    mainSolution = Solution()
    currentList = [-3,4,3,90]
    trarget = 0
    outputListe = mainSolution.twoSum(currentList, trarget)
    return outputListe

if __name__ == "__main__":
    output = main()
    print(output)