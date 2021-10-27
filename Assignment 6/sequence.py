import sys

class Sqdb:

    def __init__(self):
        self.stringA = '-'
        self.stringB = '-'
        self.scoreMatrix = []
        self.resultA = ''
        self.resultB = ''
        self.matrix = []
        self.maxScore = 0

    def printScoreMatrix(self):
        print(*'xACGT-', end=' ')
        print()
        for i in range(len(self.scoreMatrix)):
            print('ACGT-'[i], end=' ')
            print(*self.scoreMatrix[i])

    def printMatrix(self):
        print('x', end=' ')
        print(*self.stringA)
        for i in range(len(self.matrix)):
            print(self.stringB[i], end=' ')
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j].value, end = ' ')
            print()

    def initMatrix(self):
        for i in range(len(self.stringB)):
            self.matrix.append([])
            for j in range(len(self.stringA)):
                self.matrix[i].append(Cell(0, [i, j]))

        self.matrix[0][0] = Cell(0, [0,0])
        for i in range(1, len(self.stringA)):
            self.matrix[0][i].value = self.matrix[0][i - 1].value + int(self.scoreMatrix['ACGT-'.find(self.stringA[i-1])][4])
            self.matrix[0][i].addParent(self.matrix[0][i-1])
        for i in range(1, len(self.stringB)):
            self.matrix[i][0].value = self.matrix[i - 1][0].value + int(self.scoreMatrix[4]['ACGT-'.find(self.stringB[i-1])])
            self.matrix[i][0].addParent(self.matrix[i-1][0])

    def findMax(self, cell1, cell2, cell3, charA, charB):
        temp1 = Cell(cell1.value + self.findScore(charA, charB), cell1.location)
        temp2 = Cell(cell2.value + self.findScore(charA, '-'), cell2.location)
        temp3 = Cell(cell3.value + self.findScore('-', charB), cell3.location)

        if temp1.value >= temp2.value:
            if temp1.value >= temp3.value:
                return temp1
        else:
            if temp2.value >= temp3.value:
                return cell2
        return temp3

    def findScore(self, first, second):
        x = 'ACGT-'.find(first)
        y = 'ACGT-'.find(second)
        return int(self.scoreMatrix[y][x])

    def populateCells(self):
        for j in range(1, len(self.stringB)):
            for i in range(1, len(self.stringA)):
                parent = self.findMax(self.matrix[j-1][i-1], self.matrix[j][i-1], self.matrix[j-1][i], self.stringA[i], self.stringB[j])
                self.matrix[j][i].value = parent.value
                self.matrix[j][i].addParent(parent)
        self.maxScore = self.matrix[len(self.matrix) - 1][len(self.matrix[0]) - 1].value

    def getResults(self):
        current = self.matrix[len(self.matrix) - 1][len(self.matrix[0]) - 1]

        while not(current.location == [0,0]):
            if current.parent.location == [current.location[0] - 1, current.location[1] - 1]:
                self.resultA += self.stringA[-1:] + ' '
                self.resultB += self.stringB[-1:] + ' '
                self.stringA = self.stringA[:-1]
                self.stringB = self.stringB[:-1]
                
            elif current.parent.location == [current.location[0] - 1, current.location[1]]:
                self.resultA += '- '
                self.resultB += self.stringB[-1:] + ' '
                self.stringB = self.stringB[:-1]

            elif current.parent.location == [current.location[0], current.location[1] - 1]:
                self.resultA += self.stringA[-1:] + ' '
                self.resultB += '- '
                self.stringA = self.stringA[:-1]

            current = self.matrix[current.parent.location[0]][current.parent.location[1]]
    
class Cell:
    def __init__(self, value, location):
        self.value = value
        self.location = location
        self.parent = None

    def addParent(self, u):
        self.parent = u
    

def main():

    sqdb = Sqdb()
    counter = 0
    with open(sys.argv[1]) as file: # Read the inputed file
        for lines in file:
            if counter == 0:
                sqdb.stringA += lines.strip().split()[0]
                counter += 1
            elif counter == 1:
                sqdb.stringB += lines.strip().split()[0]
                counter += 1
            elif counter == 2:
                counter += 1
                continue
            else:
                line = lines.strip().split()
                sqdb.scoreMatrix.append(line[1:])

    sqdb.initMatrix()    
    sqdb.populateCells()
    sqdb.getResults()

    print('x:'+ sqdb.resultA[::-1])
    print('y:'+ sqdb.resultB[::-1])
    print('Score:', sqdb.maxScore)
if __name__ == "__main__":
    main()