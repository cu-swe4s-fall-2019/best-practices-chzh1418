pycodestyle style.py

pycodestyle get_column_stats.py

(for i in $(seq 1 100):
    do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM"
    done) > data.txt

python get_column_stats.py --file_name data.txt --col_num 2

V=1
(for i in $(seq 1 100):
    do
    echo -e "$V\t$V\t$V\t$V\t$V"
    done) > data.txt

python get_column_stats.py --file_name data.txt --col_num 2

V=4
(for i in $(seq 1 100):
    do
    echo -e "$V\t$V\t$V\t$V\t$V"
    done) > data.txt

python get_column_stats.py --file_name data.txt --col_num 3
