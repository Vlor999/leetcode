#! /usr/bin/env python3

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        position = -1

        while up <= down:
            mid = (up+down)//2
            if matrix[mid][0] < target:
                up = mid + 1
            elif matrix[mid][0] > target:
                down = mid - 1
            else:
                position = mid
                break
        
        if position != -1:
            return True
        
        
        listGauche = matrix[max(down, 0)]
        listDroite = matrix[min(up, len(matrix) - 1)]

        if listGauche[0] != listDroite[0]:
            listeElem = listGauche + listDroite
        else:
            listeElem = listGauche
        left, right = 0, len(listeElem) - 1

        while left <= right:
            mid = (left+right)//2
            if listeElem[mid] < target:
                left = left + 1
            elif listeElem[mid] > target:
                right = right - 1
            else:
                return True
        return False


def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.searchMatrix(Input[0], Input[1])
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True), 
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False), 
        ([[-10,-10],[-9,-9],[-8,-6],[-4,-2],[0,1],[3,3],[5,5],[6,8]], 0, True), 
        ([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 20, True),
        ([[-9,-9,-9,-7,-5,-3,-3,-3],[-2,-2,0,1,2,3,3,4],[5,5,5,7,9,11,11,12],[14,14,15,16,18,18,19,20],[21,23,24,25,27,29,30,31],[34,35,37,38,38,38,40,40],[42,44,44,45,47,47,47,48],[50,51,51,52,53,54,56,56],[58,59,60,62,64,64,64,66]], 5, True)]
    for input in dicoElem:
        output = input[-1]
        input = input[0:2]
        gereInput(input, output)

if __name__ == "__main__":
    main()