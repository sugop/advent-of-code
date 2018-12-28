try:
    input_file = open('input.txt','r')
    freq_list = input_file.readlines()
    print(freq_list)
    input_file.close()
except IOError as ioEx:
    print(ioEx)