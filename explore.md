how big is the dataset? 
1. wc -l clean_dialog.csv
# 36860 lines

what's the structure of the dataset? 
1. head -n 1 clean_dialog.csv
# title, writer, pony, dialog 
2. head -n 5 clean_dialog.csv

how many episodes does it cover? 
1. csvtool col 1 clean_dialog.csv | sort | uniq | wc -l
# 198 episodes

unexpected feature? 
- not sure