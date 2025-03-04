#! /usr/bin/env python3


class Solution:
    def __init__(self):
        pass

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        taille = len(temperatures)
        outputList = [0] * taille  # Initialise la liste de sortie avec des zéros
        stack = []  # Une pile pour stocker les indices des températures

        for i, temp in enumerate(temperatures):
            # Tant que la pile n'est pas vide et que la température actuelle est plus élevée
            # que celle représentée par l'indice au sommet de la pile
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                outputList[prev_index] = i - prev_index
            # Ajouter l'indice actuel à la pile
            stack.append(i)

        return outputList

def gereInput(Input, Output):
    mainSolution = Solution()
    outputListe = mainSolution.dailyTemperatures(Input)
    print("Got : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    listElem = [([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]), ([30,40,50,60], [1,1,1,0]), ([30,60,90], [1,1,0]), ([55,38,53,81,61,93,97,32,43,78], [3,1,1,2,1,1,0,1,1,0])]
    for tupleInOut in listElem:
        Input, Output = tupleInOut
        gereInput(Input, Output)

if __name__ == "__main__":
    main()