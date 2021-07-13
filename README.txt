The project aims to investigate if there is a relationship between NBA results and the US stock market.
Data collected include NBA game attendance and Twitter posts about NBA teams and the league on game day.

How to run:
1. Go to basketball-reference.com to extract game attendance data.
2. To scrape tweets from Twitter, run "snscrape_nba.py" with the files in "attendance_data" as input.
    Scraped tweets are stored in directory "twitter_data".
3. To remove new lines in the Tweet text column, run "removeNewline.java" on the files in "twitter_data".
    Output files are named "twitterScrapeOutputXXXX_nonew.csv".
    A sample file is included in the directory "twitter_data".
4. To remove duplicate tweets, run "removeDuplicateTweets.py" on the "twitterScrapeOutputXXXX_nonew.csv" files.
    Output files are named "twitterScrapeOutputXXXX_ultimate.csv".
    A sample file is included in the directory "twitter_data".
5. To perform sentiment analysis on the tweets, run "sentimentAnalysis.py" on the "twitterScrapeOutputXXXX_ultimate.csv" files.
    Output file is the "tweetSentimentDaily.csv" file in "twitter_data".
6. To merge twitter data and NBA attendance data, run "mergeSentimentAttendance.py".
7. To extract S&P 500 data, run "getYahooSP500.py".
8. To combine all S&P500 data, run "combineSP.py".
9. To get final input matrix: use "buildFinalMatrix.py"

Final Data:
final_input_data/sp500_all.csv: all sp500 from 2006-2020
final_input_data/allDailyData.csv: all sentiment analysis results + NBA structure data

Final input matrix:
final_input_data/input_matrix.csv

The Neural Net Model is then ran on the "input_matrix.csv" file using RapidMiner.

Please see the report for final results and discussion.