from dataclasses import dataclass
from collections import deque
from typing import List

@dataclass(frozen=True)
class Pos:
    row: int
    col: int

    # def __init__(self, row: int, col: int):
    #     self.row = row
    #     self.col = col

    def __add__(self, other):
        if isinstance(other, Pos):
            return Pos(self.row + other.row, self.col + other.col)

@dataclass
class Trail:
    pos: Pos
    score: int

    def __init__(self, row: int, col: int):
        self.pos = Pos(row, col)
        self.score = 0

def checkbounds(map: List[str], pos: Pos):
    if pos.row < 0 or pos.row >= len(map) or pos.col < 0 or pos.col >= len(map[0]):
        return False
    
    return True

def dfs(map: List[str], trail: Trail):
    return

def bfs(map: List[str], trail: Trail):
    visited = set()
    queue = deque([Pos(trail.pos.row, trail.pos.col)])
    dirs = [Pos(-1, 0), Pos(0, 1), Pos(1, 0), Pos(0, -1)]

    while queue:
        # print(queue)
        node = queue.popleft()
        val = int(map[node.row][node.col])
        if node not in visited:
            visited.add(node)
            if val == 9:
                trail.score += 1
            else:
                for dir in dirs:
                    next_pos = node + dir
                    if checkbounds(map, next_pos) and map[next_pos.row][next_pos.col].isnumeric():
                        next_val = int(map[next_pos.row][next_pos.col])
                        if next_val == val + 1:
                            queue.append(next_pos)

    return

def main():
    # print("Hello from main")
    f = open('./2024/Day10/input.txt', 'r')
    lines = [line.strip('\n') for line in f]
    f.close()

    # Find all 0's
    trails = []
    for row in range(len(lines)):
        line = lines[row]
        # print(line)
        for col in range(len(lines[row])):
           if lines[row][col] == "0": 
            new_trail = Trail(row, col)
            trails.append(new_trail)
            # print(row,col)
            # print(new_trail)
            # print(trails)
            
    total = 0
    for trail in trails:
        # print(trail)
        bfs(lines, trail)
        # print(trail.score)
        total += trail.score

    print(total)
    return

if __name__ == "__main__":
    # print("Hello world")
    main()
    exit(0)