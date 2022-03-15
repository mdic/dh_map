import jsonlines
import csv

# create CSV output
csvfile = open("snscrape_out.csv",'a',encoding='utf-8')
csvfile_writer = csv.writer(csvfile, delimiter='\t')

# define and write csv header
csvfile_writer.writerow([])

with jsonlines.open('snscraptest.json') as reader:
    for obj in reader:
# first, define which values should be extracted
        coord_lat = obj['coordinates']['latitude']
# then construct the output row
        csv_line = []
# and write it to the output file
        csvfile_writer.writerow(csv_line)