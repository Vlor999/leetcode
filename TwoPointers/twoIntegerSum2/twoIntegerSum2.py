#! /usr/bin/env python3

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        taille = len(numbers)
        for i in range(taille - 1):
            first = numbers[i]
            for j in range(i+1, taille):
                second = numbers[j]
                somme = first + second
                if somme > target:
                    break
                elif somme == target:
                    return [i + 1, j + 1]

def gereInput(Input, Output):
    mainSolution = Solution()
    numbers, target = Input
    outputListe = mainSolution.twoSum(numbers, target)
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [([[1,2,3,4], 3], [1,2]), ([[1,2,3,4], 5], [1,4])]
    for input in dicoElem:
        output = input[1]
        input = input[0]
        gereInput(input, output)

if __name__ == "__main__":
    main()