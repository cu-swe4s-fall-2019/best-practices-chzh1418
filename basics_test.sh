#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle style.py
assert_no_stdout


run test_get_column_stats pycodestyle get_column_stats.py
assert_no_stdout

run test_basics_test pycodestyle basics_test.py
assert_no_stdout

run wrong_file_name python get_column_stats.py --file_name=bad_file_name.txt --col_num=2
assert_in_stdout 'FileNotFoundError:'
assert_exit_code 1

run Neg_col_num python get_column_stats.py --file_name=data.txt --col_num=-1
assert_in_stderr 'IndexError:'
assert_stderr

run col_num_wrong python get_column_stats.py --file_name=data.txt --col_num=1000
assert_in_stdout 'IndexError:'
assert_exit_code 2

run Test_Good_testcase python get_column_stats.py --file_name=data.txt --col_num=3
assert_exit_code 0


