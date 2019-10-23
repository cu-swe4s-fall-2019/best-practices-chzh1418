# Best Practices
[![Build Status](https://travis-ci.com/cu-swe4s-fall-2019/best-practices-chzh1418.svg?branch=master)](https://travis-ci.com/cu-swe4s-fall-2019/best-practices-chzh1418)

## Description
The main function is get_column_stats.py, it can take a file name and column number an output the mean and standard deviation of the column.
- `basics_test.sh`: functional test of get_column_stats.py
- `basics_test.py`: unit test of get_column_stats.py

## Usage
`
python get_column_stats.py -file_name [file_name] -col_num [column_number]
`
To run functional test:
`
bash basics_test.sh
`
To run unit test:
`
python basics_test.py
`
## Continuous integration
Modify the .travis.yml file to run continuous integration
    * wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    * bash Miniconda3-latest-Linux-x86_64.sh -b
    * . /home/travis/miniconda3/etc/profile.d/conda.sh
    * conda update --yes conda
    * conda config --add channels r
    * conda create --yes -n test
    * conda activate test
    * conda install -y pycodestyle
    * conda install --yes python=3.6
    * conda install -y numpy 
script:
    * bash basics_test.sh
    * python basics_test.py
    * pycodestyle get_column_stats.py
    * pycodestyle basics_test.py
    * pycodestyle style.py

## Functional test and unit test
* For functional test, use bash script to generate new data.txt file with both constant and random value.
* Use the newly generated file to test the function of get_column_stats.py
* For unit test, test contant and random value along with some exceptions





