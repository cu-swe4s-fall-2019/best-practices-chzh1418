#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Test code style
run test_style pycodestyle style.py
assert_no_stdout

run test_get_column_stats pycodestyle get_column_stats.py
assert_no_stdout

run test_basics_test pycodestyle basics_test.py
assert_no_stdout

# Test constant 
(for i in `seq 1 100`; do
	echo -e "5\t5\t5\t5\t5";
done)> data.txt

run col_stat_constant python get_column_stats.py --file_name data.txt --col_num 2
assert_stdout
assert_exit_code 0
assert_in_stdout "mean 5"
assert_in_stdout "stdev 0"
assert_no_stderr 

# Test random number
(for i in `seq 1 100`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt
run stats_random_test python get_column_stats.py --file_name data.txt --col_num 2
assert_stdout
assert_exit_code 0
assert_in_stdout "mean"
assert_in_stdout "stdev"
assert_no_stderr


run wrong_file_name python get_column_stats.py --file_name bad_file_name.txt --col_num 2
assert_in_stdout 'Did not find input file'
assert_exit_code 1

run neg_col_num python get_column_stats.py --file_name data.txt --col_num -1
assert_exit_code 1

run test_tood_testcase python get_column_stats.py --file_name data.txt --col_num 3
assert_exit_code 0


