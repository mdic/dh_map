# import the required modules to read/write jsonl and csv files
import jsonlines
import csv

# create a blank csv output in the current folder, with utf-8 encoding and using the @@@ method
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