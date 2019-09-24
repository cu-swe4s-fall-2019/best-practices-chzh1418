import sys
import math
import argparse


# Define function to calculate mean of a vector
def get_mean(V):
    if len(V) == 0:
        raise ValueError('get_mean, empty input')
        sys.exit(1)
    mean = sum(V)/len(V)
    return mean


# Define functions to calculate standard deviation of a vector
def get_stdev(V):
    if len(V) == 0:
        raise ValueError('get_stdev, empty input')
        sys.exit(1)
    mean = get_mean(V)
    stdev = math.sqrt(sum([(mean - x)**2 for x in V]))
    return stdev


# Parsing arguments using argparse
def arguments():
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

    return parser.parse_args()


# Main function to incorprate all the data and outputs
def get_stats():
    args = arguments()
    file_name = args.file_name
    col_num = args.col_num
    mean = None
    stdev = None
    V = []
# check if the file exit
    try:
        input_file = open(file_name, 'r')
    except FileNotFoundError:
        print('Did not find input file')
        sys.exit(1)


# check the colnum number is valid
    if col_num < 0:
        raise ValueError('Column number not correct')
        sys.exit(1)

    for row in input_file:
        try:
            A = [int(x) for x in row.split()]
            V.append(A[col_num])
        except ValueError:
            print('Input file issue')
            sys.exit(1)
    if len(V) == 0:
        raise Exception('length of column is zero')
        sys.exit(1)
    else:
        mean = get_mean(V)
        stdev = get_stdev(V)
    print('mean', mean)
    print('stdev', stdev)


if __name__ == "__main__":
    get_stats()
