#import jsonlines
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# initiate the Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

#create CSV output
csvfile = open("snscrape_out.csv",'a',encoding='utf-8')
csvfile_writer = csv.writer(csvfile, delimiter='\t')

#write csv header
csvfile_writer.writerow(['lat', 'long'])

with open('snscrape-since-20220316-json.tsv', 'r', newline='\n') as csvdata:
# read the content of the file, where each value is separated from the others by a tab (\t) character
    csvdata_reader = csv.reader(csvdata, delimiter='\t')
# skip the first row, containing the header
    next(csvdata_reader, None)
# create a list of all the rows and store it in the variable 'rows'
    rows = [r for r in csvdata_reader]
# for each row in the list of rows
    for row in rows:

# extract each relevant value and store it inside of a single variable, by indicating the 
# column number where the value is stored in the original data. Python counts from 0, so e.g. column
# number 7 is read as number 6
        tweet_id = row[0]
        tweet_date = row[2]
        tweet_username = row[6]
        tweet_user_realname = row[7]
        tweet_content = row[4]
        tweet_SA = analyzer.polarity_scores(tweet_content)

# the following variables should contain the value 0 if no urls are included or the tweet is not a retweet,
# and the value 1 when links are present or the tweet is a retweet. for urls, the script checks whether the length
# of the original value is shorter than 3 characters (i.e. it only contains the empty square brackets), in which
# case it assigns the value 0 as no value is present in the data. for 'isretweet' it checks if the word 'False'
# appears in the data and assigns 0 if it does or 1 otherwise.
        tweet_urls_present = 0 if len(row[13]) < 3 else 1
        tweet_isretweet = 0 if row[21] == "False" else 1
        print(tweet_content + ' ' + str(tweet_SA))

# build the output row
        csv_line = []
# and write it to the output file
        csvfile_writer.writerow(csv_line)