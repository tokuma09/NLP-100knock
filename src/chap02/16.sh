n=$(wc -l data/chap02/popular-names.txt | awk '{print $1}')
ln=$(expr $n / $1)
split -l $ln data/chap02/popular-names.txt output/chap02/ans016
