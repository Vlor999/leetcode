#! /usr/bin/env python3

class Solution:
    def __init__(self):
        pass

    def getListProd(self, nums: list[int]) -> list[int]:
        outputListProd = []
        currentVal = 1
        for num in nums:
            currentVal *= num
            outputListProd.append(currentVal)
        return outputListProd


    def getLeftProd(self, nums: list[int]) -> list[int]:
        return self.getListProd(nums)
            

    def getRightProd(self, nums: list[int]) -> list[int]:
        return self.getListProd(nums[::-1])[::-1]


    def getIndice(self, i:int, taille:int) -> tuple[int,int]:
        indiceLeft = i - 1
        indiceRight = i + 1
        if indiceLeft < 0 : 
            indiceLeft = None
        if indiceRight > taille - 1:
            indiceRight = None
        return (indiceLeft, indiceRight)

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        leftProd = self.getLeftProd(nums)
        rightProd = self.getRightProd(nums)
        outputProd = []
        taille = len(nums)
        for i in range(taille) : 
            indiceLeft, indiceRight = self.getIndice(i, taille)
            elemLeft = 1
            elemRight = 1
            if indiceLeft != None :
                elemLeft = leftProd[indiceLeft]
            if indiceRight != None :
                elemRight = rightProd[indiceRight]
            outputProd.append(elemLeft * elemRight)
        return outputProd
            
def main():
    mainSolution = Solution()
    nums = [-1,1,0,-3,3]
    output = mainSolution.productExceptSelf(nums)
    return output

if __name__ == "__main__":
    output = main()
    print(output)