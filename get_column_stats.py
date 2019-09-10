import sys
import math
import argparse

file_name = sys.argv[1]
col_num = int(sys.argv[2])

parser = argparse.ArgumentParser(
            description='Pass Parameters')

parser.add_argument('--file_name',
                    type=str,
                    help='Name of the file',
                    required=True)
parser.add_argument('--col_num',
                    type=int,
                    help='Number of column',
                    required=True)

args = parser.parse_args()

f = open(args.file_name, 'r')

V = []

for l in f:
    A = [int(x) for x in l.split()]
    V.append(A[args.col_num])

mean = sum(V)/len(V)

stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

print('mean:', mean)
print('stdev:', stdev)
