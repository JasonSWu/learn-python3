import os
path = os.path.dirname(os.path.abspath(__file__))
with open(path + "/../data/misc_data1.txt", 'r') as f:
    for line in f:
        print(line)