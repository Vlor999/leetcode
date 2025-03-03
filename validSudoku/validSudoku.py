#! /usr/bin/env python3

class Solution:
    def __init__(self):
        pass

    def isRedondantSquare(self, square:list[list[str]]) -> bool:
        isRedondant = False
        currentDico = {i : 0 for i in range(10)}
        currentDico["."] = 0
        for line in square:
            print(line)
            for elem in line : 
                if elem == ".":
                    currentDico[elem] += 1
                    continue
                else:
                    valElem = int(elem)
                    if valElem in currentDico:
                        if currentDico[valElem] == 1:
                            isRedondant = True
                            break
                        else: 
                            currentDico[valElem] += 1
                    else:
                        print("the value is not a digit in : 1-9")
                        return False
        print(currentDico)
        return isRedondant

    def isRedondant(self, line:list[str]) -> bool:
        isRedondant = False
        currentDico = {i : 0 for i in range(10)}
        currentDico["."] = 0
        for elem in line : 
            if elem == ".":
                continue
            else:
                valElem = int(elem)
                if valElem in currentDico:
                    if currentDico[valElem] == 1:
                        isRedondant = True
                        break
                    else: 
                        currentDico[valElem] += 1
                else:
                    print("the value is not a digit in : 1-9")
                    return False
        return isRedondant
    
    def byColumn(self, board: list[list[str]]) -> list[list[str]]:
        newBoard = [["" for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                newBoard[i][j] = board[j][i]
        return newBoard
    
    def getListSquare(self, board:list[list[int]]) -> list[list[list[int]]]:
        listSquare = []
        for i in range(0, len(board), 3):
            currentSquare = [["" for _ in range(3)] for _ in range(3)]
            for j in range(0, len(board[i]), 3):
                for i0 in range(3):
                    for j0 in range(3):
                        currentSquare[i0][j0] = board[i+i0][j+j0]
                copieSquare = []
                for i0 in range(3):
                    copieSquare.append([])
                    for j0 in range(3):
                        copieSquare[i0].append(currentSquare[i0][j0])
                listSquare.append(copieSquare)
        return listSquare

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        isValid = True
        
        for ligne in board:
            redondantLine = self.isRedondant(ligne)
            if redondantLine:
                return False
        
        transposeBoard = self.byColumn(board)
        for ligne in transposeBoard:
            redondantCol = self.isRedondant(ligne)
            if redondantCol : 
                return False
            
        listSquare = self.getListSquare(board)
        for square in listSquare:
            isRedondantSquare = self.isRedondantSquare(square)
            if isRedondantSquare :
                return False
        return isValid
        

def main():
    mainSolution = Solution()
    boardInput = [
        [".","4",".",".",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."],
        [".",".",".","1",".",".","7",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".","3",".",".",".","6","."],
        [".",".",".",".",".","6",".","9","."],
        [".",".",".",".","1",".",".",".","."],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","8",".",".",".",".","."]]
    isValid = mainSolution.isValidSudoku(boardInput)
    return isValid

if __name__ == "__main__":
    output = main()
    print(output)