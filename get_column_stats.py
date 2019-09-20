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
# open file and test exceptions
f = None


def get_mean(file_name, col_num):
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find ' + file_name)
    except PermissionError:
        print('Could not open ' + file_name)

# readlines in the file and then split intergers in line then append
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
    except ZeroDivisionError:
        print('Length of column is zero, somthing is wrong')
    return mean


def get_stdev(file_name, col_num):
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find ' + file_name)
    except PermissionError:
        print('Could not open ' + file_name)
    V = []
    for line in f.readlines():
        A = [int(x) for x in line.split()]
        try:
            V.append(A[col_num])
        except IndexError:
            print('Index out of range')
        except ValueError:
            print('Error value')
    mean = get_mean(file_name, col_num)
    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
    return stdev


if __name__ == '__main__':
    get_mean(file_name, col_num)
    get_stdev(file_name, col_num)
    print('mean:', get_mean(file_name, col_num))
    print('stdev:', get_stdev(file_name, col_num))

# modify the get column stats file to be testable for the unit test
# mainly by make functions available to run and return
