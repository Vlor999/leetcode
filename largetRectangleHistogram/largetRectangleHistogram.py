#! /usr/bin/env python3

class Solution:    
    def convBinListVal(self, valBinaire):
        listPosition = []
        pos = 0
        for lettre in valBinaire:
            if lettre == "1":
                listPosition.append(pos)
            pos += 1
        return listPosition

    def getIElem(self, nbElem, taille):
        listElemReturn = []
        debut = 0
        fin = nbElem
        while fin != taille + 1:
            listElemReturn.append(debut * "0" + "1" * nbElem + "0" * (taille - nbElem - debut))
            debut += 1
            fin+=1
        return listElemReturn

    def listCombinaison(self, nbElem):
        listElem = []
        output = []
        for i in range(1, nbElem + 1):
            listElem.append(self.getIElem(i, nbElem))
        for listBinaire in listElem:
            for binaire in listBinaire : 
                output.append(self.convBinListVal(binaire))
        return output

    def getTaille(self, comb, heights):
        taille = len(comb)
        listHeight = [heights[pos] for pos in comb]
        return min(listHeight) * taille

    def largestRectangleArea(self, heights: list[int]) -> int:
        heights = self.correctionHeights(heights)
        taille = len(heights)
        listComb = self.listCombinaison(taille)
        maxVal = -1
        for comb in listComb:
            currentVal = self.getTaille(comb, heights)
            if currentVal > maxVal:
                maxVal = currentVal
        return maxVal

def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.largestRectangleArea(Input)
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [([2,1,5,6,2,3], 10), ([2,4], 4), ([1] * 1000, 1000)]
    for input in dicoElem:
        output = input[1]
        input = input[0]
        gereInput(input, output)

if __name__ == "__main__":
    main()