
# Built-in imports
from time import sleep

# Local imports
from cq import CircularQueue
from adt import Stack, Queue, IsEmptyError
from maze import Maze

maze = Maze('maze.txt')
maze.import_from()
here = maze.start_coor
options = Stack()

# visited coordinates
visited = set()

step = 1

while here != maze.end_coor:
    print(f"========== STEP {step} ==========")
    maze.display(
        here=here,
        options=options,
        visited=visited
    )
    print(f'CURRENT: {here}')
    print(F'VISITED: {visited}')
    
    visited.add(here)
    around = maze.around(here)

    for coor in around:
        if coor not in visited:
            options.push(coor)

    try:
        here = options.pop()
        step += 1
    except IsEmptyError:
        raise IsEmptyError('No solution; no more paths to choose from')
    

    sleep(0.5)