
"""
This class is the template class for the Maze solver
"""

import sys
from math import sqrt
import numpy
import queue

EMPTY = 0       # empty cell
OBSTACLE = 1    # cell with obstacle / blocked cell
START = 2       # the start position of the maze (red color)
TARGET = 3      # the target/end position of the maze (green color)

class MazeSolverAlgoTemplate:

    

    def __init__(self):
        # TODO: this is you job now :-)
        self.rows = 0
        self.columns = 0
        self.dimCols = 0
        self.dimRows = 0
        self.setStartCol = 0
        self.setStartRow = 0
        self.setEndCol = 0
        self.setEndRow = 0
        self.grid = [[]]

        print("just initialized yess")

    # Setter method for the maze dimension of the rows
    def setDimRowsCmd(self, rows):
        # TODO: this is you job now :-)
        self.rows = rows
        self.dimRows = rows

    # Setter method for the maze dimension of the columns
    def setDimColsCmd(self, cols):
        # TODO: this is you job now :-)
        self.columns = cols
        self.dimCols = cols
        
    # Setter method for the column of the start position 
    def setStartColCmd(self, col):
        # TODO: this is you job now :-)
        self.setStartCol = col

    # Setter method for the row of the start position 
    def setStartRowCmd(self, row):
        # TODO: this is you job now :-)
        self.setStartRow = row

    # Setter method for the column of the end position 
    def setEndColCmd(self, col):
        # TODO: this is you job now :-)
        self.setEndCol = col

    # Setter method for the row of the end position 
    def setEndRowCmd(self, row):
        # TODO: this is you job now :-)
        self.setEndRow = row
    
    # Setter method for blocked grid elements
    def setBlocked(self,row ,col):
        # TODO: this is you job now :-)
        self.grid[row][col] = OBSTACLE


    # Start to build up a new maze
    # HINT: don't forget to initialize all member variables of this class (grid, start position, end position, dimension,...)
    def startMaze(self, rows, columns):
        # TODO: this is you job now :-)
        #HINT: populate grid with dimension row,column with zeros
        self.dimCols = columns
        self.dimRows = rows
        self.setStartCols = 0
        self.setStartRows = 0
        self.setEndCols = 0
        self.setEndRows = 0
        self.grid = [[]]

        print("rows: ", rows)
        print("columns: ", columns)
        
        if rows>0 and columns>0:
            
            self.grid = numpy.empty((rows, columns), dtype=int)
            print("sollte ein grid mit nuller erstellen")
            for i in range(rows):
                for j in range(columns):
                    self.grid[i][j]=0


    # Define what shall happen after the full information of a maze has been received
    def endMaze(self):
        # TODO: this is you job now :-)
        # HINT: did you set start position and end position correctly?

        print("this is the end.")
        self.grid[self.setStartRow][self.setStartCol] = START
        self.grid[self.setEndRow][self.setEndCol] = TARGET
        
        print(" the maze is done.")
        self.printMaze()

    # just prints a maze on the command line
    def printMaze(self):
        print("kurz vorm drucken")
        # TODO: this is you job now :-)
        print(self.grid)
    
        print("gedruckt")

    # loads a maze from a file pathToConfigFile
    def loadMaze(self,pathToConfigFile):
        # check whether a function numpy.loadtxt() could be useful
        # TODO: this is you job now :-)
        self.grid=numpy.loadtxt(pathToConfigFile, delimiter=',',dtype=int)
        self.setDimCols=self.grid.shape[0]
        self.setDimRows=self.grid.shape[1]
        self.dimCols=self.grid.shape[0]
        self.dimRows=self.grid.shape[1]

        start_arr = numpy.where(self.grid == 2)
        self.setStartRow=int(start_arr[0][0])
        self.setStartCol=int(start_arr[1][0])

        end_arr = numpy.where(self.grid == 3)
        self.setEndRow=int(end_arr[0][0])
        self.setEndCol=int(end_arr[1][0])

    # clears the complete maze 
    def clearMaze(self):
        # TODO: this is you job now :-)
        self.startMaze(0,0)
  
    # Decides whether a certain row,column grid element is inside the maze or outside
    def isInGrid(self,row,column):
        # TODO: this is you job now :-)
        if (row>=0 and column>=0 and row<self.dimRows and column<self.dimCols):
            return True
        else:
            return False



    # Returns a list of all grid elements neighboured to the grid element row,column
    def getNeighbours(self,row,column):
        # TODO: this is you job now :-)
        # TODO: Add a Unit Test Case --> Very good example for boundary tests and condition coverage
        neighbors = []

        top=(row+1, column)
        bottom=(row-1, column)
        left=(row, column-1)
        right=(row, column+1)
        

        if self.isInGrid(row, column) == False:
            print("not in grid")
            return neighbors
        if self.grid[row][column] == OBSTACLE:
            print("OBISTICAL")
            return neighbors
        if self.isInGrid(top[0], top[1]) == True and self.grid[top[0]] [top[1]] != OBSTACLE:
            neighbors.append(top)
        if self.isInGrid(bottom[0], bottom[1]) == True and self.grid[bottom[0]] [bottom[1]] != OBSTACLE:
            print("bottom")
            neighbors.append(bottom)
        if self.isInGrid(left[0], left[1]) ==True and self.grid[left[0]][left[1]] != OBSTACLE:
            neighbors.append(left)
        if self.isInGrid(right[0],right[1]) == True and self.grid[right[0]] [right[1]] != OBSTACLE:
            print("right")
            neighbors.append(right)

        

        return neighbors

    # Gives a grid element as string, the result should be a string row,column
    def gridElementToString(self,row,col):
        # TODO: this is you job now :-)
        # HINT: this method is used as primary key in a lookup table
        res = ""
        res += str(row)
        res += ","
        res += str(col)
        return res
        
    
    # check whether two different grid elements are identical
    # aGrid and bGrid are both elements [row,column]
    def isSameGridElement(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        if self.grid[aGrid[0],aGrid[1]]==self.grid[bGrid[0],bGrid[1]]:
            return True
        return False

        


    # Defines a heuristic method used for A* algorithm
    # aGrid and bGrid are both elements [row,column]
    def heuristic(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        # HINT: a good heuristic could be the distance between to grid elements aGrid and bGrid
        pass

    # Generates the resulting path as string from the came_from list
    def generateResultPath(self,came_from):
        # TODO: this is you job now :-)
        # HINT: this method is a bit tricky as you have to invert the came_from list (follow the path from end to start)
        pass


    #############################
    # Definition of Maze solver algorithm
    #
    # implementation taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html
    #############################
    
    def myMazeSolver(self):
        # TODO: this is you job now :-)
        print("this is the solver method")
        start = (self.setStartRow, self.setStartCol)
        frontier=queue.Queue()
        frontier.put(start)
 
        visited = [] ## ersten 2 werte sind coordinaten, zweiten 2 werte sind came from
        #visited.append([start, None])


        while not frontier.empty():
            
            current = frontier.get()
            for next in self.getNeighbours(current[0], current[1]):
                notFound=True
                print(next)
                for v in visited:
                    print("next: {} v: {}".format(next,v))
                    
                    if next in v:
                        notFound=False
                        break
                if notFound:
                    frontier.put(next)
                    visited.append([next, current])        
         
        print(visited)
        

    # Command for starting the solving procedure
    def solveMaze(self):
        
        


        return self.myMazeSolver()


##BREADTH FIRST traversal
 



if __name__ == '__main__':
    mg = MazeSolverAlgoTemplate()


    # HINT: in case you want to develop the solver without MQTT messages and without always
    #       loading new different mazes --> just load any maze you would like from a file

    mg.loadMaze("..\\MazeExamples\\Maze1.txt")
    mg.printMaze()
    neighbours = mg.getNeighbours(0,0)

    myList=[1,(1,2), (1,2,3)]
    test=(1,2)
    if test in myList:
        print("test in List")

    print("list done")

    print(neighbours)
    print(mg.gridElementToString(1,2))

    print(mg.isSameGridElement([0,1],[0,3]))

    mg.myMazeSolver()
    #solutionString = mg.solveMaze()
    #print(solutionString)
   
