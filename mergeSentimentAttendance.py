import pandas as pd

def main():
    sentiment = pd.read_csv("tweetSentimentDaily.csv")
    attend = pd.read_csv("nbaAttendance_edit.csv")
    result = pd.merge(sentiment, attend, how="outer", on="Date")
    result.to_csv("dailyData_06_13.csv")
    

if __name__ == "__main__":
    main()
