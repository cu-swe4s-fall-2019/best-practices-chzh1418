import sys
import math
import argparse
# parsing arguments


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

    args = parser.parse_args()

    file_name = args.file_name
    col_num = args.col_num


def get_mean(V):
    mean = sum(V)/len(V)
    return mean


def get_stdev(V):
    mean = get_mean(V)
    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
    return stdev


if __name__ == "__main__":
    args = arguments()
    try:
        file = open(args.file_name, 'r')
    except FileNotFoundError as error:
        print('FileNotFoundError: {}'.format(error))
        sys.exit(1)

    V = []
    mean = None
    stdev = None

    for line in file:
        A = [int(x) for x in line.split()]
        try:
            V.append(A[args.col_num])
        except IndexError as error:
            print('IndexError: {}'.format(error))
            sys.exit(1)

    # calculate result
    mean = sum(V) / len(V)
    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    # print result
    print('mean:', mean)
    print('stdev:', stdev)
# modify the get column stats file to be testable for the unit test
# mainly by make functions available to run and return
