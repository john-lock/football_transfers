import csv
import pandas as pd


infile = 'result.csv'
outfile = open('clean.csv', 'w')
write_outfile = csv.writer(outfile)


players = []

with open(infile, 'r') as rdr:
    reader = csv.reader(rdr)
    for row in reader:
        if '€' in row:
            # write_outfile.writerow(row)
            players.append(row)

df = pd.DataFrame(players)
df.to_csv('clean.csv', index=False)
#data = df[0][1]
#print("1:", len(df))
#print("2:", len(df))
#print(data)
