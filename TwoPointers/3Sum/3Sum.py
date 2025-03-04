#! /usr/bin/env python3

class Solution:
    def convSetList(self, setValeur):
        output = []
        for valeur in setValeur:
            valeur = valeur[1:-1].split(",")
            currentList = []
            for val in valeur:
                convVal = int(val)
                currentList.append(convVal)
            output.append(currentList)
        return output
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        nums.sort()
        taille = len(nums)
        for i in range(taille - 2):
            elemI = nums[i]
            if elemI > 0 : 
                break
            for j in range(i + 1, taille - 1):
                elemJ = nums[j]
                if elemI + elemJ > 0:
                    break
                for k in range(j + 1, taille):
                    elemK = nums[k]
                    if elemI + elemJ + elemK == 0:
                        res.add(f"{[elemI, elemJ, elemK]}")
                    elif elemI + elemJ + elemK > 0:
                        break
        output = self.convSetList(res)
        return output


def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.threeSum(Input)
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]), ([0,1,1], []), ([0,0,0], [[0,0,0]])]
    for input in dicoElem:
        output = input[1]
        input = input[0]
        gereInput(input, output)

if __name__ == "__main__":
    main()