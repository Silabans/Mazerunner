
MAZE = {
    "path": "0",
    "wall": "1",
}

# Symbol mapping for maze display
SYMBOLS = {
    "wall": "█",
    "space": " ",
    "here": "H",
    "option": "?",
    "visited": ".",
}


class Maze:
    def __init__(self, filename):
        self.filename = filename

    def import_from(self) -> list[str]:
        self.maze: list[str] = []
        with open(self.filename, 'r', newline='') as f:
            for row in f:
                self.maze.append(row.strip('\n').strip('\r'))
        print(repr(self.maze[0]))
        
        self.ysize = len(self.maze)
        self.xsize = len(self.maze[0])

        self.start_coor = (0, self.maze[0].index(MAZE['path']))
        self.end_coor = (self.ysize - 1, self.maze[self.ysize - 1].index(MAZE['path']))

        return self.maze

    def ispath(self, coor) -> bool:
        y, x = coor
        if not 0 <= y < self.ysize:
            return False
        if not 0 <= x < self.xsize:
            return False
        
        return self.maze[y][x] == MAZE['path']

    def around(self, coor) -> list[tuple[int, int]]:
        y, x = coor
        adj_coors = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
        options = []

        for adj_coor in adj_coors:
            if self.ispath(adj_coor):
                options.append(adj_coor)
        
        return options
    
    def display(self, here, options, visited):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if (y, x) == here:
                    print(SYMBOLS["here"], end='')
                elif visited and (y, x) in visited:
                    print(SYMBOLS["visited"], end='')
                elif options and options.contains((y, x)):
                    print(SYMBOLS["option"], end='')
                elif self.ispath((y, x)):
                    print(SYMBOLS["space"], end='')
                else:
                    print(SYMBOLS["wall"], end='')
            print()
