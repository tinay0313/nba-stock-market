import pandas as pd
import re 

def removeDuplicateTweetId(input):
    formatInput = input.drop_duplicates(subset=['Tweet Id'], keep='first', ignore_index=True)
    return formatInput

def removeDuplicateText(input):
    formatInput = input.drop_duplicates(subset=['Text','Username'], keep='first', ignore_index=True)
    return formatInput

def removeUrl(input):
    input['Text'] = input['Text'].replace(r'http\S+', '', regex=True).replace(r'www\S+', '', regex=True)

def main():
    inputDf = pd.read_csv("twitterScrapeOutput0608_ultimate.csv", engine='python')
    formatInputDf = removeDuplicateTweetId(inputDf)
    removeUrl(formatInputDf)
    formatInputDf = removeDuplicateText(formatInputDf)
    formatInputDf.to_csv("twitterScrapeOutput0608_ultimate.csv", index=False)
    print(formatInputDf)

    inputDf = pd.read_csv("twitterScrapeOutput0608_ultimate.csv", engine='python')
    formatInputDf = removeDuplicateTweetId(inputDf)
    removeUrl(formatInputDf)
    formatInputDf = removeDuplicateText(formatInputDf)
    formatInputDf.to_csv("twitterScrapeOutput0608_ultimate.csv", index=False)
    print(formatInputDf)

if __name__ == "__main__":
    main()