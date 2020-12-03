#--- Day 3: Toboggan Trajectory ---

from pathlib import Path

def build_full_filepath(filename: str) -> str:
        base_path = Path(__file__).parent
        return (base_path / filename).resolve()

def read_map_grid(filename: str) -> list:
    full_path = build_full_filepath(filename)
    with open(full_path,'r') as textFile:
        lines = [list(line.strip()) for line in textFile] #strip EOLs and convert to list of lists
        return lines

def count_trees_part1(values: list, dx: int, dy: int) -> int:
    x, y, cnt, length, mod = 0, 0, 0, len(values) - dy, len(values[0])
    while y < length:
        x = (x + dx) % mod
        y += dy
        if values[y][x] == '#':
            cnt += 1
    return cnt

def main():
    map_grid = read_map_grid('day03_input.txt')
    print(count_trees_part1(map_grid, 3, 1))

main()
