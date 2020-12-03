# --- Day 2: Password Philosophy ---

from pathlib import Path

def build_full_filepath(filename):
        base_path = Path(__file__).parent
        return (base_path / filename).resolve()

def main():
    
    file_path = build_full_filepath('day02_input.txt')

    with open(file_path, 'r') as f:
        policy1_count_valid_pwds = 0
        policy2_count_valid_pwds = 0
        for line in f:
            split_line = line.split()
            lower_limit, upper_limit = split_line[0].split('-')
            allowed_char = split_line[1].replace(':','')
            pwd = split_line[2].strip()
            char_repeat_count = pwd.count(allowed_char)

            #first password policy check
            if (char_repeat_count >= int(lower_limit) and char_repeat_count <= int(upper_limit)):
                policy1_count_valid_pwds = policy1_count_valid_pwds + 1

            #Second password policy check
            if (char_repeat_count > 0):
                if ((pwd[int(lower_limit)-1] == allowed_char) ^ (pwd[int(upper_limit)-1] == allowed_char)):    #boolean XOR comparison
                    policy2_count_valid_pwds = policy2_count_valid_pwds + 1
            
    print('Policy # 1: Total valid passwords = ', policy1_count_valid_pwds)
    print('Policy # 2: Total valid passwords = ', policy2_count_valid_pwds)

main()