import time
import sys, os
from collections import deque
from tracker import Tracker #time tracker

class UnreachableExitError(BaseException):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return 'They\'re all gonna die :('

with Tracker() as t: #time tracker

    maze = [] #create any maze you want where "O" - Start; "X" - Finish
    maze.append(['X',' ',' ','#','#','#'])
    maze.append(['#','#',' ',' ',' ',' '])
    maze.append(['#',' ','#','#','#',' '])
    maze.append([' ',' ',' ',' ','#',' '])
    maze.append(['#',' ','#',' ',' ',' '])
    maze.append(['#','#','#',' ','#','#'])
    maze.append(['#','#',' ',' ','#','#'])
    maze.append(['#',' ',' ',' ',' ',' '])
    maze.append([' ',' ',' ','#','#',' '])
    maze.append([' ','#','#',' ','#',' '])
    maze.append(['#',' ',' ',' ',' ',' '])
    maze.append(['#','#','#',' ','#','#'])
    maze.append(['#','#','#',' ',' ','#'])
    maze.append(['O',' ',' ',' ','#',' '])
    maze.append(['#',' ','#','#','#',' '])
    maze.append(['#',' ',' ',' ',' ',' '])
    maze.append(['#',' ','#',' ',' ',' '])
    maze.append(['#','#','#',' ','#',' '])
    maze.append(['#','#','#',' ','#',' '])
    maze.append(['#',' ',' ',' ','#',' '])
    maze.append(['#',' ','#','#','#',' '])
    maze.append(['#',' ','#','#','#',' '])
    maze.append(['#',' ',' ',' ',' ',' '])
    maze.append(['#','#','#','#','#',' '])
  

    path = deque() #main queue
    been_here = {} #to avoid jumping to the squares which has already been checked

    #printing the path to the exit of the maze simply and nicely
    def print_maze(start_coords, final_coords, fin_direction, maze):
        line = start_coords[0]
        step = start_coords[1]
        for direction in fin_direction:
            
            if direction == 'L': 
                step -= 1
                if maze[line][step] != ' ':
                    for row in maze:
                        print(row)
                    return

                maze[line][step] = 'o'
                for row in maze:
                    print(row)

            if direction == 'R': 
                step += 1
                if maze[line][step] != ' ':
                    for row in maze:
                        print(row)
                    return

                maze[line][step] = 'o'
                for row in maze:
                    print(row)

            if direction == 'U': 
                line -= 1
                if maze[line][step] != ' ':
                    for row in maze:
                        print(row)
                    return

                maze[line][step] = 'o'
                for row in maze:
                    print(row)

            if direction == 'D': 
                line += 1
                if maze[line][step] != ' ':
                    for row in maze:
                        print(row)
                    return

                maze[line][step] = 'o'
                for row in maze:
                    print(row)

            time.sleep(0.3)
            os.system('cls') #for window cmd to clear the console before printing the next maze

    def find_start(maze):
        for line in range(len(maze)):
            for step in range(len(maze[line])): 
                if maze[line][step] == 'O': 
                    return [line, step]

    def finding_path(maze, line, step, direction=''):
        been_here[(line, step)] = 'START' #first square is checked now
        while True:
            if not line - 1 < 0: #invalid move, coz it goes outside the maze
                if maze[line - 1][step] == ' ': #valid move
                    if not been_here.get((line - 1, step)): #if the squared is saved, we're too late, someone got here faster, but if not: 
                        path.append([direction + 'U', [line - 1, step]])#check UP later
                        been_here[(line - 1, step)] = direction + 'U'#okay, UP square will be checked 100%, so we save it
                elif maze[line - 1][step] == 'X':#the destination point, first to this place is the fastest(shortest in this case)
                    return [direction + 'U', [line - 1, step]] #return the results

            #others directions are getting checked just the same as the UP
            if not line + 1 > len(maze) - 1:
                if maze[line + 1][step] == ' ': 
                    if not been_here.get((line + 1, step)):
                        path.append([direction + 'D', [line + 1, step]])
                        been_here[(line + 1, step)] = direction + 'D'
                elif maze[line + 1][step] == 'X': 
                    return [direction + 'D', [line + 1, step]]

            if not step - 1 < 0:
                if maze[line][step - 1] == ' ': 
                    if not been_here.get((line, step - 1)):
                        path.append([direction + 'L', [line, step - 1]])
                        been_here[(line, step - 1)] = direction + 'L'
                elif maze[line][step - 1] == 'X': 
                    return [direction + 'L', [line, step - 1]]

            if not step + 1 > len(maze[line]) - 1:
                if maze[line][step + 1] == ' ':
                    if not been_here.get((line, step + 1)):
                        path.append([direction + 'R', [line, step + 1]])
                        been_here[(line, step + 1)] = direction + 'R'
                elif maze[line][step + 1] == 'X': 
                    return [direction + 'R', [line, step + 1]]

            try: #if path is empty it means that the destination is not reachable
                direction, coords = path.popleft() #won't be able to pop from the empty array
                line, step = coords
            except IndexError as err: 
                raise UnreachableExitError('The exit is unreachable') from err 

    start = find_start(maze)
    try:
        try:
            fin_direction, fin_coords = finding_path(maze, *start)
            print_maze(start, fin_coords, fin_direction, maze)
        except UnreachableExitError as err: 
            print(err.msg)
            print(err)
            print(f'Python to blame, it says => {err.__cause__}')
    except Exception: 
        print('Something\'s really dumb just happened')


