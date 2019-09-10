import sys
import math
import argparse
# parsing arguments
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

file_name = args.file_name
col_num = args.col_num
#open file and test exceptions
f = None
try:
    f = open(file_name, 'r')
except FileNotFoundError:
    print('Could not find ' + file_name)
except PermissionError:
    print('Could not open ' + file_name)

#readlines in the file and then split intergers in line then append
V = []
for line in f.readlines():
    A = [int(x) for x in line.split()]
    try:
        V.append(A[col_num])
    except IndexError:
        print('Index out of range')
    except ValueError:
        print('Error value')

try:
    mean = sum(V)/len(V)
    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
except ZeroDivisionError:
    print('Length of column is zero, somthing is wrong')

print('mean:', mean)
print('stdev:', stdev)
