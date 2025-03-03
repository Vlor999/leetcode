#! /usr/bin/env python3

class Solution:
    def removeSpace(self, s:str)->str:
        alphaNum = """ ,.<>/?!'\"\\[]{}@£$%^&*(-_)=+#€;:|`~§±"""
        ouput = ""
        for lettre in s:
            if lettre in alphaNum:
                continue
            lowerLettre = lettre.lower()
            ouput += lowerLettre
        return ouput 

    def isPalindrome(self, s: str) -> bool:
        output = True
        sWithoutSpace = self.removeSpace(s)
        taille = len(sWithoutSpace)
        for i in range(taille//2):
            if sWithoutSpace[i] != sWithoutSpace[taille - i - 1]:
                print(sWithoutSpace[i], sWithoutSpace[taille - i - 1])
                return False
        return output

def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.isPalindrome(Input)
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [("Was it a car or a cat I saw?", True), ("tab a cat", False), ("No lemon, no melon", True), ("Madam, in Eden, I'm Adam", True)]
    for input in dicoElem:
        output = input[1]
        input = input[0]
        gereInput(input, output)

if __name__ == "__main__":
    main()