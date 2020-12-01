from pathlib import Path

def get_expenses_from_file(filename):
    base_path = Path(__file__).parent
    file_path = (base_path / filename).resolve()
    with open(file_path,'r') as f:
        return list(map(int, f))

def main():
    expenses = get_expenses_from_file('day01_input.txt')
    for entry in expenses:
        if 2020 - entry in expenses:
            answer_one = entry * (2020 - entry)
            break


    for entry1 in expenses:
        for entry2 in expenses:
            target = 2020 - entry1 - entry2
            if target in expenses:
                answer_two = entry1 * entry2 * target
                break

    print(answer_one, answer_two)

main()