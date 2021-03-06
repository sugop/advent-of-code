def get_freq_changes(filename):
    with open(filename,'r') as f:
        return list(map(int, f))

def find_duplicate_freq(freq_changes):
    freq = 0
    freq_history = {0: True}
    ctr = 0
    while True:
        freq += freq_changes[ctr%len(freq_changes)]
        if freq in freq_history:
            print("First freq reached twice = ", freq)
            break
        freq_history[freq] = True
        ctr += 1

def main():
    changes = get_freq_changes('input1.txt')

    #part 1: Calc sum of frequencies
    print("Sum = ", sum(changes))

    #part 2: find first duplicate instance of calculated frequency
    find_duplicate_freq(changes)
main()