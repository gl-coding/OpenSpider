dir="ciku"

rm map.dic
for line in `ls $dir`;do
    python ./sougou_scel_convert.py "$line"
done
