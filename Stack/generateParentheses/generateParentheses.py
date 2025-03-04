#! /usr/bin/env python3


class Solution:
    def __init__(self):
        pass

    def generateParenthesisRec(self, n: int) -> set[str]:
        if n <= 0:
            return set()
        elif n == 1:
            return set(["()"])
        else:
            lastSet = self.generateParenthesisRec(n - 1)
            newSet = set()
            for elem in lastSet:
                for i in range(len(elem)):
                    newElem = elem[:i] + "()" + elem[i:]
                    newSet.add(newElem)
        return newSet
    
    def generateParenthesis(self, n: int) -> list[str]:
        setParenthesis = self.generateParenthesisRec(n)
        return list(setParenthesis)

def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.generateParenthesis(Input)
    print("Got : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = {3:["((()))","(()())","(())()","()(())","()()()"], 1:["()"], 2:["()()", "(())"]}
    for input in dicoElem:
        output = dicoElem[input]
        gereInput(input, output)

if __name__ == "__main__":
    main()