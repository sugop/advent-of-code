def read_integers(filename):
    with open(filename,'r') as f:
        return list(map(int, f))

def read_freq(filename):
        with open(filename,'r') as f:
            return map(int,f) 

def main():
    freqs = read_integers('input.txt')

    #part 1: Calc sum of frequencies
    print(sum(freqs))

main()