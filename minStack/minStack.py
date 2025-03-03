#! /usr/bin/env python3


class Solution:
    def __init__(self):
        self.dicoElem = {"[" : "]", "{":"}", "(":")"}
        pass

    def getCorrespondant(self, s:str, currentPosition:int)->str:
        isGoodEnd = True
        firstElem = s[currentPosition]
        if firstElem in self.dicoElem:
            lastElem = self.dicoElem[firstElem]
        else:
            return None, False
        compteur = 1
        position = currentPosition + 1
        while compteur > 0 and position < len(s):
            if s[position] == firstElem:
                compteur += 1
            elif s[position] == lastElem:
                compteur -= 1
            position += 1
        if position <= len(s):
            isGoodEnd = s[position - 1] == lastElem
        else:
            isGoodEnd = False
        return position, isGoodEnd

    def isValid(self, s: str) -> bool:
        valid = True
        currentPositon = 0
        while currentPositon < len(s):
            last = currentPositon
            currentPositon, isGood = self.getCorrespondant(s, currentPositon)
            if not isGood:
                return False
            subString = s[last + 1: currentPositon - 1]
            if subString != "":
                isSubValid = self.isValid(subString)
                if not isSubValid:
                    return False
        return valid

def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.isValid(Input)
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = {"()":True, "()[]{}" : True, "(]": False, "([])": True, "(){}}{": False}
    for input in dicoElem:
        output = dicoElem[input]
        gereInput(input, output)

if __name__ == "__main__":
    main()
