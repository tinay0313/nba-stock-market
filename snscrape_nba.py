import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list = []

inputDf = pd.read_csv("twitterScrapeInput0910.csv")

for idx in inputDf.index:
    since = "since:{}".format(inputDf['Start Date'][idx])
    until = "until:{}".format(inputDf['End Date'][idx])
    visitor = "\"{}\"".format(inputDf['Visitor/Neutral'][idx])
    home = "\"{}\"".format(inputDf['Home/Neutral'][idx])
    query = "{} OR {} OR nba lang:en exclude:retweets {} {}".format(home, visitor, since, until)
    print(query)
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i > 5000:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount])

print("making df")
# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['DateTime', 'Tweet Id', 'Text', 'Username', 'Reply Count', 'Retweet Count', 'Like Count', 'Quote Count'])
tweets_df.to_csv("twitterScrapeOutput0910.csv",index=False)
print(tweets_df)
