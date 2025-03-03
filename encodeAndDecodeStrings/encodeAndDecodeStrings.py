#! /usr/bin/env python3

class Solution:
    def __init__(self):
        pass

    def encode(self, strs: list[str]) -> str:
        outputString = ""
        for elem in strs:
            outputString += elem + "😀"
        return outputString

    def decode(self, s: str) -> list[str]:
        outputList = []
        tailleString = len(s)
        currentString = ""
        for i in range(tailleString):
            elem = s[i]
            if elem == "😀":
                outputList.append(currentString)
                currentString = ""
            else:
                currentString += elem
        return outputList

    
   

def main():
    mainSolution = Solution()
    Input = ["neet","code","love","you"]
    out1 = mainSolution.encode(Input)
    out2 = mainSolution.decode(out1)
    print(out1)
    print(out2)
    return out2

if __name__ == "__main__":
    output = main()
    print(output)