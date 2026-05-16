
# Built-in imports
from time import sleep

# Local imports
from cq import CircularQueue
from adt import Stack, Queue, IsEmptyError
from maze import Maze

maze = Maze('maze.txt')
maze.import_from()
here = maze.start_coor
options = Queue()

# visited coordinates
visited = set()
seen = set()
step = 1

# This dictionary records the key as the contemporary next coordinates
# and the value as the coordinates from which we come to reach the them
traceback = {}

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
        if coor not in visited and coor not in seen:
            options.push(coor)
            seen.add(coor)
            traceback[coor] = here

    try:
        here = options.pop()
        step += 1
    except IsEmptyError:
        raise IsEmptyError('No solution; no more paths to choose from')
    
    sleep(0.2)
visited.add(here)

# shortest path taken reconstructed
path = []
current = maze.end_coor

while current != maze.start_coor:
    path.append(current)
    current = traceback[current]
    print(current)
path.append(maze.start_coor)
path.reverse()

print(f"PATH: {path}")
print(f'path length: {len(path)}')
print(f'number of visited: {len(visited)}')
print(f'length of seen: {len(seen)}')


reconstructed = Queue()
total_steps_required = len(path)


loading_time = 1.5
dot_count = 3
while loading_time > 0:
    print(f"Loading final path taken {'.' * dot_count}   ", end='\r', flush=True)
    sleep(0.5)
    dot_count -= 1
    loading_time -= 0.5


print(f"========== STEPS REQUIRED TO FINISH: {total_steps_required} ==========")
maze.display(
    here=maze.start_coor,
    options=None,
    visited=set(path)
)

