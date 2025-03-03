#! /usr/bin/env python3

class Solution:
    def __init__(self):
        pass

    def convElementOrd(self, currentString:str) -> str:
        sorted_string = ''.join(sorted(currentString))
        return sorted_string
    
    def geneListTupleStrSortedStr(self, strs: list[str]) -> list[(str,str)]:
        currentDico = {}
        taille = len(strs)
        for i in range(taille):
            elem = strs[i]
            sortedElem = self.convElementOrd(elem)
            if sortedElem not in currentDico :
                currentDico[sortedElem] = [elem]
            else : 
                currentDico[sortedElem].append(elem)
        return currentDico

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        listOutput = []
        dicoOrdered = self.geneListTupleStrSortedStr(strs)
        for valOrdered in dicoOrdered:
            listOutput.append(dicoOrdered[valOrdered])
        return listOutput


        
def main():
    mainSolution = Solution()
    input = ["a"]
    output = mainSolution.groupAnagrams(input)
    return output

if __name__ == "__main__":
    output = main()
    print(output)