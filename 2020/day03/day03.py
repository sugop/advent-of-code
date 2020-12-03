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

def count_trees(values: list, dx: int, dy: int) -> int:
    x, y, cnt, length, mod = 0, 0, 0, len(values) - dy, len(values[0])
    while y < length:
        x = (x + dx) % mod
        y += dy
        if values[y][x] == '#':
            cnt += 1
    return cnt

def solve_part1(area_map: list) -> int:
    return count_trees(area_map, 3, 1)

def solve_part2(area_map: list, sol_part1: int) -> int:
    slopes = ((1, 1), (5, 1), (7, 1), (1, 2))
    product = sol_part1

    for slope in slopes:
        product *= count_trees(area_map, slope[0], slope[1])
    return product

def main():
    area_map = read_map_grid('day03_input.txt')
    sol_part1 = solve_part1(area_map)
    sol_part2 = solve_part2(area_map, sol_part1)

    print('Part 1: Count of Trees = ', sol_part1)
    print('Part 2: Count of Trees = ', sol_part2)

main()
