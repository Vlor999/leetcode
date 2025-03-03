#! /usr/bin/env python3

class Solution:
    def __init__(self):
        pass

    def dicoFrequence(self, nums: list[int]) -> dict[int, int]:
        frequenceDico = {}
        for elem in nums:
            if elem not in frequenceDico : 
                frequenceDico[elem] = 1
            else :
                frequenceDico[elem] += 1 
        return frequenceDico
    
    def orderElementInDico(self, dicoFrequence: dict[int:int])-> list[int]:
        outputList = []
        for objet in dicoFrequence:
            frequence = dicoFrequence[objet]
            currentTuple = (frequence, objet)
            outputList.append(currentTuple)
        outputList = sorted(outputList, key = lambda tup : tup[0], reverse=True)
        return outputList

    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequenceDico = self.dicoFrequence(nums)
        outputList = self.orderElementInDico(frequenceDico)
        print(outputList)
        listElement = outputList[:k]
        return [elem[1] for elem in listElement]
   

def main():
    mainSolution = Solution()
    nums = [1]
    k = 1
    output = mainSolution.topKFrequent(nums, k) 
    return output

if __name__ == "__main__":
    output = main()
    print(output)