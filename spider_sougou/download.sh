start=$1
end=$2

mkdir ciku

for((i=$start;i<=$end;i++));do
    link=`sed -n $i"p" download.list`
    wget -P ciku/ "$link"
    #sleep 1
done
