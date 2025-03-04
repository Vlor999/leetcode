#! /usr/bin/env python3

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = []
        stack = []
        
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        # On cherhce maintenant a ordonner les elemts afin de savoir lequel arrive en premier 
        pairs = sorted(pairs, reverse=True)
        for pos, vit in pairs:
            time = (target - pos) / vit
            stack.append(time)
            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()
        return len(stack)

def gereInput(Input, Output):
    mainSolution = Solution()
    target, position, speed = Input
    outputListe = mainSolution.carFleet(target, position, speed)
    print("Get : ", outputListe, ", Expected : ", Output, end=" ")
    if outputListe == Output:
        print("✅")
    else:
        print("❌")


def main():
    dicoElem = [([12, [10,8,0,5,3], [2,4,1,1,3]], 3), ([10, [3], [3]], 1), ([100, [0,2,4], [4,2,1]], 1) ]
    for input in dicoElem:
        output = input[1]
        input = input[0]
        gereInput(input, output)

if __name__ == "__main__":
    main()