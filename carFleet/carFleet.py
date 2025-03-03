#! /usr/bin/env python3

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = []
        stack = []
        
        for x in range(len(speed)):
            pairs.append([position[x], speed[x]])
        
        pairs = sorted(pairs)[::-1]
        print(pairs)
        
        for p, s in pairs:
            # SI il est proche de la sortie alors pour ne pas avoir a faire a un car fleet alors il doit prendre moins de temps pour arriver. Sinon conflit et on retire un élément
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack) # On cherche ici le nombre de temps mmis diffeerents pour arriver a la fin

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