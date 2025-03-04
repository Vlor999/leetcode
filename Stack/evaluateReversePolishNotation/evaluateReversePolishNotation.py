#! /usr/bin/env python3


class Solution:

    def __init__(self):
        self.tokens = {"+" : "PLUS", "*" : "MUL", "/":"DIV", "-":"SUB"}

    def getFirstToken(self, listTokens:list[str])->int:
        position = 2
        currentToken = listTokens[position]
        while currentToken not in self.tokens:
            position += 1
            currentToken = listTokens[position]
        return position
    
    def updateTokens(self, position:int, tokens:list[str])->list[str]:
        value = str(int(eval(tokens[position - 2] + tokens[position] + tokens[position - 1])))
        tokens = tokens[:position - 2] + [value] + tokens[position + 1:]
        return tokens

    def evalRPN(self, tokens: list[str]) -> int:
        while len(tokens) >= 3:
            position = self.getFirstToken(tokens)
            tokens = self.updateTokens(position, tokens)
        return tokens[0]

        

def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.evalRPN(Input)
    print("Got : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [(["2","1","+","3","*"],"9"), (["4","13","5","/","+"], "6"), (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], "22")]
    for tupleInOut in dicoElem:
        Input, Output = tupleInOut
        gereInput(Input, Output)

if __name__ == "__main__":
    main()
