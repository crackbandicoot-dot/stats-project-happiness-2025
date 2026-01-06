import csv

#Select relevant colmns for the analysis by their indexes

#Country,
#Ladder score,
#Logged GDP per capita,
# Social support,
# Healthy life expectancy,
# Freedom to make life choices,
# Generosity
#Perception of corruption
selected_columns_indexes = [0,1,5,6,7,8,9,10]

with open('../data/happiness-data.csv', 'r') as infile, open('../data/happiness-data-clean.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        writer.writerow(map(lambda col_index: row[col_index],selected_columns_indexes))

