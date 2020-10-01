# Полигон N на M метров разбит на клетки со стороной равной одному метру. 
# Для каждой клетки полигона нам известна средняя высота, выраженная в сантиметрах. 
# В центре одной из клеток стоит робот, который может двигаться только из центра одной клетки 
# в центр другой, и только в том случае, если эти клетки имеют общую сторону. 
# Еще одно ограничение, которое наложено конструкцией робота — невозможность перемещаться между 
# клетками, если их средние высоты отличаются более, чем на 100 сантиметров.

# Также нам интересны на этом полигоне две другие клетки — в одной из них лежит груз, в другую должен прибыть робот 
# после того, как заберет груз. Для того чтобы забрать груз, роботу нужно просто заехать в клетку, в которой он находится.

# Какой минимальный путь должен пройти робот, чтобы попасть из начальной клетки в конечную, забрав перед этим груз? 
# Груз не влияет на движение робота. Гарантируется, что искомый путь существует.

# Очереди с приоритетами
import heapq
from math import sqrt

class AlgorithmOnGraphs:
    def __init__ (self, heightDelta):
        #  Невозможность перемещаться между клетками, если их средние высоты отличаются более, чем на 100 сантиметров.
        self.heightDelta = heightDelta

    def getDistance(self, A, B):
        if abs(matrix[A[0]][A[1]] - matrix[B[0]][B[1]]) > self.heightDelta:
            return 5000000
        return sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

    # Алгоритм
    def core(self, algorithm, matrix, start, end):
        n = len(matrix)
        m = len(matrix[1])
        
        matrixOfDistances = [0] * n
        matrixOfVisitedPlaces = [0] * n

        for i in range(n):
            matrixOfDistances[i] = [5000000] * m
            matrixOfVisitedPlaces[i] = [False] * m

        for i in range(m):
            matrixOfVisitedPlaces[0][i] = True
            matrixOfVisitedPlaces[n - 1][i] = True

        for i in range(n):
            matrixOfVisitedPlaces[i][0] = True
            matrixOfVisitedPlaces[i][m - 1] = True

        queue = []
        visitedСells = 0
        matrixOfDistances[start[0]][start[1]] = 0
        # Всего вершин
        totalCells = (m-2) * (n-2)
        # Ставит робота в начальную позицию
        heapq.heappush(queue, (0, [start[0], start[1]]))

        while totalCells > visitedСells:
            node = heapq.heappop(queue)
            x = node[1][0]
            y = node[1][1]

            if end[0] == y and end[1] == x:
                return matrixOfDistances

            if not matrixOfVisitedPlaces[x - 1][y]:
                if abs(matrix[x][y] - matrix[x - 1][y]) < self.heightDelta:
                    matrixOfDistances[x - 1][y] = min(matrixOfDistances[x - 1][y], matrixOfDistances[x][y] + 1)
                if (algorithm == "dijkstra"):
                    heapq.heappush(queue, (matrixOfDistances[x - 1][y], [x - 1, y]))
                elif (algorithm == "AStar"):
                    heapq.heappush(queue, (self.getDistance([x - 1, y], [x, y]), [x - 1, y]))

            if not matrixOfVisitedPlaces[x + 1][y]:
                if abs(matrix[x][y] - matrix[x + 1][y]) < self.heightDelta:
                    matrixOfDistances[x + 1][y] = min(matrixOfDistances[x + 1][y], matrixOfDistances[x][y] + 1)
                if (algorithm == "dijkstra"):
                    heapq.heappush(queue, (matrixOfDistances[x + 1][y], [x + 1, y]))
                elif (algorithm == "AStar"):
                    heapq.heappush(queue, (self.getDistance([x + 1, y], [x, y]), [x + 1, y]))

            if not matrixOfVisitedPlaces[x][y - 1]:
                if abs(matrix[x][y] - matrix[x][y - 1]) < self.heightDelta:
                    matrixOfDistances[x][y - 1] = min(matrixOfDistances[x][y - 1], matrixOfDistances[x][y] + 1)
                if (algorithm == "dijkstra"):
                    heapq.heappush(queue, (matrixOfDistances[x][y - 1], [x, y - 1]))
                elif (algorithm == "AStar"):
                    heapq.heappush(queue, (self.getDistance([x, y - 1], [x, y]), [x, y - 1]))

            if not matrixOfVisitedPlaces[x][y + 1]:
                if abs(matrix[x][y] - matrix[x][y + 1]) < self.heightDelta:
                    matrixOfDistances[x][y + 1] = min(matrixOfDistances[x][y + 1], matrixOfDistances[x][y] + 1)
                if (algorithm == "dijkstra"):
                    heapq.heappush(queue, (matrixOfDistances[x][y + 1], [x, y + 1]))
                elif (algorithm == "AStar"):
                    heapq.heappush(queue, (self.getDistance([x, y + 1], [x, y]), [x, y + 1]))

            matrixOfVisitedPlaces[x][y] = True
            visitedСells += 1

        return matrixOfDistances

def say(what):
    phrases = {
        '1': "dijkstra",
        '2': "AStar",
    }

    result = algorithmOnGraphs.core(phrases[what], matrix, start=[coordinatesOfTheRobot_X, coordinatesOfTheRobot_Y], end=[coordinatesOfTheCargo_X, coordinatesOfTheCargo_Y])[coordinatesOfTheCargo_X][coordinatesOfTheCargo_Y]
    result += algorithmOnGraphs.core(phrases[what], matrix, start=[coordinatesOfTheCargo_X, coordinatesOfTheCargo_Y], end=[coordinatesOfTheEndPoint_X, coordinatesOfTheEndPoint_Y])[coordinatesOfTheEndPoint_X][coordinatesOfTheEndPoint_Y]
    
    outputFile = open('output.txt', 'w', encoding='utf-8')
    outputFile.write("Расстояние в метрах, которое необходимо проехать\n")
    outputFile.write("роботу, чтобы доставить груз в конечную клетку ===> " + str(result))
    outputFile.close()
    
    print("----------------------------------")
    print("Ответ записан в output.txt")

if __name__ == "__main__":
    algorithmOnGraphs = AlgorithmOnGraphs(100)

    print("Какой использовать алгоритм? (Введите цифру)\n1 → Дейкстры\n2 → A star")
    whichAlgorithmToUse = input()

    inputFile = open('input.txt', 'r')

    inputVariable = inputFile.readline().split()
    n = int(inputVariable[0])
    m = int(inputVariable[1])

    matrix = [0] * (n + 2)
    for i in range(n + 2):
        matrix[i] = [5000000] * (m + 2)

    for i in range(n):
        inputVariable = inputFile.readline().split()
        for j in range(m):
            matrix[i+1][j+1] = int(inputVariable[j])

    inputVariable = inputFile.readline().split()
    coordinatesOfTheRobot_X = int(inputVariable[0]) + 1
    coordinatesOfTheRobot_Y = int(inputVariable[1]) + 1

    inputVariable = inputFile.readline().split()
    coordinatesOfTheCargo_X = int(inputVariable[0]) + 1
    coordinatesOfTheCargo_Y = int(inputVariable[1]) + 1

    inputVariable = inputFile.readline().split()
    coordinatesOfTheEndPoint_X = int(inputVariable[0]) + 1
    coordinatesOfTheEndPoint_Y = int(inputVariable[1]) + 1

    say(whichAlgorithmToUse)