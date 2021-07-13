import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def sentimentAnalysis(inputDf):
    sia = SentimentIntensityAnalyzer()
    neg = []
    neu = []
    pos = []
    compound = []
    num = 1
    for text in inputDf['Text']:
        if isinstance(text, float):
            neg.append(-1.0)
            neu.append(-1.0)
            pos.append(-1.0)
            compound.append(-1.0)
            continue
        score = sia.polarity_scores(text)
        neg.append(score['neg'])
        neu.append(score['neu'])
        pos.append(score['pos'])
        compound.append(score['compound'])
    
    inputDf['Neg'] = neg
    inputDf['Neu'] = neu
    inputDf['Pos'] = pos
    inputDf['Compound'] = compound

def dailySentiment(inputDf):
    date = []
    posCt = []
    neuCt = []
    negCt = []
    posReplyCt = []
    posRetweetCt = []
    posLikeCt = []
    posQuoteCt = []
    neuReplyCt = []
    neuRetweetCt = []
    neuLikeCt = []
    neuQuoteCt = []
    negReplyCt = []
    negRetweetCt = []
    negLikeCt = []
    negQuoteCt = []

    for idx,row in inputDf.iterrows():
        date.append(row['DateTime'][:10])

        if row['Neg'] == -1 and row['Pos'] == -1:
            negCt.append(0)
            neuCt.append(0)
            posCt.append(0)
            posReplyCt.append(0)
            posRetweetCt.append(0)
            posLikeCt.append(0)
            posQuoteCt.append(0)
            neuReplyCt.append(0)
            neuRetweetCt.append(0)
            neuLikeCt.append(0)
            neuQuoteCt.append(0)
            negReplyCt.append(0)
            negRetweetCt.append(0)
            negLikeCt.append(0)
            negQuoteCt.append(0)
            continue

        if row['Neg'] > row['Neu'] and row['Neg'] > row['Pos']:
            negCt.append(1)
            neuCt.append(0)
            posCt.append(0)
            posReplyCt.append(0)
            posRetweetCt.append(0)
            posLikeCt.append(0)
            posQuoteCt.append(0)
            neuReplyCt.append(0)
            neuRetweetCt.append(0)
            neuLikeCt.append(0)
            neuQuoteCt.append(0)
            negReplyCt.append(row['Reply Count'])
            negRetweetCt.append(row['Retweet Count'])
            negLikeCt.append(row['Like Count'])
            negQuoteCt.append(row['Quote Count'])
        elif row['Pos'] > row['Neu'] and row['Pos'] > row['Neg']:
            negCt.append(0)
            neuCt.append(0)
            posCt.append(1)
            posReplyCt.append(row['Reply Count'])
            posRetweetCt.append(row['Retweet Count'])
            posLikeCt.append(row['Like Count'])
            posQuoteCt.append(row['Quote Count'])
            neuReplyCt.append(0)
            neuRetweetCt.append(0)
            neuLikeCt.append(0)
            neuQuoteCt.append(0)
            negReplyCt.append(0)
            negRetweetCt.append(0)
            negLikeCt.append(0)
            negQuoteCt.append(0)
        else:
            negCt.append(0)
            neuCt.append(1)
            posCt.append(0)
            posReplyCt.append(0)
            posRetweetCt.append(0)
            posLikeCt.append(0)
            posQuoteCt.append(0)
            neuReplyCt.append(row['Reply Count'])
            neuRetweetCt.append(row['Retweet Count'])
            neuLikeCt.append(row['Like Count'])
            neuQuoteCt.append(row['Quote Count'])
            negReplyCt.append(0)
            negRetweetCt.append(0)
            negLikeCt.append(0)
            negQuoteCt.append(0)
    
    new_df = pd.DataFrame(
        list(zip(date, posCt,neuCt,negCt,posReplyCt,posRetweetCt,posLikeCt,posQuoteCt,neuReplyCt,neuRetweetCt,neuLikeCt,neuQuoteCt,negReplyCt,negRetweetCt,negLikeCt,negQuoteCt)),
        columns =['Date', 'PosCt', 'NeuCt', 'NegCt', 'posReplyCt', 'posRetweetCt', 'posLikeCt', 'posQuoteCt', 'neuReplyCt', 'neuRetweetCt', 'neuLikeCt', 'neuQuoteCt', 'negReplyCt', 'negRetweetCt', 'negLikeCt', 'negQuoteCt'])
    return new_df

def sentimentCount(df):
    aggregation_functions = {'PosCt': 'sum', 'NeuCt': 'sum', 'NegCt': 'sum', 'posReplyCt': 'sum', 'posRetweetCt': 'sum', 'posLikeCt': 'sum', 'posQuoteCt': 'sum', 'neuReplyCt': 'sum', 'neuRetweetCt': 'sum', 'neuLikeCt': 'sum', 'neuQuoteCt': 'sum', 'negReplyCt': 'sum', 'negRetweetCt': 'sum', 'negLikeCt': 'sum', 'negQuoteCt': 'sum'}
    df_new = df.groupby(df['Date']).aggregate(aggregation_functions)
    totalTweet = []
    for idx,row in df_new.iterrows():
        totalTweet.append(row['PosCt'] + row['NeuCt'] + row['NegCt'])
    df_new['totalDailyTweets'] = totalTweet
    return df_new

def main():
    inputDf = pd.read_csv("twitterScrapeOutput0608.csv")
    sentimentAnalysis(inputDf)
    new_df = dailySentiment(inputDf)
    df1 = sentimentCount(new_df)

    inputDf = pd.read_csv("twitterScrapeOutput0809.csv")
    sentimentAnalysis(inputDf)
    new_df = dailySentiment(inputDf)
    df2 = sentimentCount(new_df)
    
    inputDf = pd.read_csv("twitterScrapeOutput0910.csv")
    sentimentAnalysis(inputDf)
    new_df = dailySentiment(inputDf)
    df3 = sentimentCount(new_df)

    inputDf = pd.read_csv("twitterScrapeOutput1011.csv")
    sentimentAnalysis(inputDf)
    new_df = dailySentiment(inputDf)
    df4 = sentimentCount(new_df)

    inputDf = pd.read_csv("twitterScrapeOutput1112.csv")
    sentimentAnalysis(inputDf)
    new_df = dailySentiment(inputDf)
    df5 = sentimentCount(new_df)
    
    inputDf = pd.read_csv("twitterScrapeOutput1213.csv")
    sentimentAnalysis(inputDf)
    new_df = dailySentiment(inputDf)
    df6 = sentimentCount(new_df)
    
    frames = [df1, df2, df3, df4, df5, df6]
    result = pd.concat(frames)

    result.to_csv("tweetSentimentDaily.csv")
    print(result)

if __name__ == "__main__":
    main()
