#--- Day 3: Toboggan Trajectory ---

from pathlib import Path

def build_full_filepath(filename):
        base_path = Path(__file__).parent
        return (base_path / filename).resolve()

def read_map_grid(filename):
    full_path = build_full_filepath(filename)
    with open(full_path,'r') as textFile:
        lines = [list(line.strip()) for line in textFile] #strip EOLs and convert to list of lists
        return lines

def main():

    map_grid = read_map_grid('day03_input.txt')
    print(map_grid)

main()
