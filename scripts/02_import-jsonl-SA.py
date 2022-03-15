import jsonlines
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# initiate the Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

#create CSV output
csvfile = open("snscrape_out.csv",'a',encoding='utf-8')
csvfile_writer = csv.writer(csvfile, delimiter='\t')

#write csv header
csvfile_writer.writerow(['lat', 'long', 'name', 'description'])

with jsonlines.open('snscrapetest.json') as reader:
    for obj in reader:
# get the content (text) of the tweet
        tweetContent = obj['renderedContent']
# apply the analyzer on it
        tweetContent = analyzer.polarity_scores(tweetContent)
# build the output row
        csv_line = []
# and write it to the output file
        csvfile_writer.writerow(csv_line)