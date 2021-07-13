import pandas as pd
from datetime import datetime, timedelta, date
import os.path




def getSPIndex(time, df):
    if time.strftime("%Y-%m-%d") in df['Date']:
    	return df.loc[df['Date'] == time.strftime("%Y-%m-%d")].iloc[0]['Close']
    else:
    	for i in range(df.shape[0]):
    		currDate = datetime.strptime(df.iloc[i]['Date'], "%Y-%m-%d").date()
    		if currDate > time:
    			return df.loc[df['Date'] == currDate.strftime("%Y-%m-%d")].iloc[0]['Close']


    	



sp500 = "sp500_all.csv"
DF_sp500 = pd.read_csv(sp500)
# DF_sp500.drop(['Unnamed: 0', 'DailyChange'], inplace=True, axis =1)

data = "allDailyData.csv"
DF_data = pd.read_csv(data, index_col=0)



# DF_data.drop(['posReplyCt', 'posRetweetCt', 'posLikeCt', 'posQuoteCt',
#  'neuReplyCt', 'neuRetweetCt', 'neuLikeCt', 'neuQuoteCt',
#  'negReplyCt', 'negRetweetCt', 'negLikeCt', 'negQuoteCt', 
#  'totalDailyTweets', 'Avg Attendance Per Game'], inplace=True, axis=1)

DF_data.drop(['totalDailyTweets', 'Avg Attendance Per Game'], inplace=True, axis=1)
# df.drop('a', inplace=True, axis=1)

# print(DF_data)





time = DF_data.iloc[0]['Date']
date1 = datetime.strptime(time, "%Y-%m-%d").date()

# print(date1.isocalendar().week)



targetWeek = date1.isocalendar().week
# print(date1.isocalendar())
offsetthisweek = date1.isocalendar().weekday-1
offsetnextweek = 8 - date1.isocalendar().weekday

targetWeekCurrMon = date1 - timedelta(days=offsetthisweek)
targetWeekNextMon = date1 + timedelta(days=offsetnextweek)
# print(targetWeekCurrMon)
# print(targetWeekNextMon)
currPos = 0
currNeu = 0
currNeg = 0
currGames = 0
currAtt = 0

posReplay = 0
posRetweet = 0
posLike = 0
posQuote = 0

neuReplay = 0
neuRetweet = 0
neuLike = 0
neuQuote = 0

negReplay = 0
negRetweet = 0
negLike = 0
negQuote = 0


# df.loc[df['column_name'] == some_value]
# print(DF_sp500)
# row = DF_sp500.loc[DF_sp500['Date'] == targetWeekCurrMon.strftime("%Y-%m-%d")]
# print(type(row))
# print(row.index.values[0])
# idx = row.index.values[0]
# for i in range(idx, idx+10 , 1):
# 	print(i)
# print(row.iloc[0]['Close'])


resultList = []
for i in range(DF_data.shape[0]):
	currDate = datetime.strptime(DF_data.iloc[i]['Date'], "%Y-%m-%d").date()
	currWeek = currDate.isocalendar().week

	if(currWeek == targetWeek):
		# add counts when same week
		currPos = currPos + DF_data.iloc[i]['PosCt']
		currNeu = currNeu + DF_data.iloc[i]['NeuCt']
		currNeg = currNeg + DF_data.iloc[i]['NegCt']
		currGames = currGames + DF_data.iloc[i]['Number Games']
		currAtt = currAtt + DF_data.iloc[i]['Total Attendance']

		posReplay = posReplay + DF_data.iloc[i]['posReplyCt']
		posRetweet = posRetweet + DF_data.iloc[i]['posRetweetCt']
		posLike = posLike + DF_data.iloc[i]['posLikeCt']
		posQuote = posQuote + DF_data.iloc[i]['posQuoteCt']

		neuReplay = neuReplay + DF_data.iloc[i]['neuReplyCt']
		neuRetweet = neuRetweet + DF_data.iloc[i]['neuRetweetCt']
		neuLike = neuLike + DF_data.iloc[i]['neuLikeCt']
		neuQuote = neuQuote + DF_data.iloc[i]['neuQuoteCt']

		negReplay = negReplay + DF_data.iloc[i]['negReplyCt']
		negRetweet = negRetweet + DF_data.iloc[i]['negRetweetCt']
		negLike = negLike + DF_data.iloc[i]['negLikeCt']
		negQuote = negQuote + DF_data.iloc[i]['negQuoteCt']

	elif(currWeek != targetWeek):

		#insert to new DF
		currClose = getSPIndex(targetWeekCurrMon, DF_sp500)
		nextClose = getSPIndex(targetWeekNextMon, DF_sp500)
		# print('----')
		# print(currClose)
		# print(nextClose)
		# print('----')
		# print(nextClose - currClose)
		label = -1
		if(nextClose - currClose > 0):
			label = 1
		else:
			label = 0
		totalCt = currPos + currNeu + currNeg
		posPer = 0
		neuPer = 0
		negPer = 0

		if totalCt != 0:
			posPer = currPos/totalCt
			neuPer = currNeu/totalCt
			negPer = currNeg/totalCt
		
		resultList.append([currPos, currNeu, currNeg, posPer, neuPer, negPer, posReplay, posRetweet, posLike, posQuote, neuReplay, neuRetweet, neuLike, neuQuote, negReplay, negRetweet, negLike, negQuote, currGames, currAtt, targetWeekCurrMon, targetWeekNextMon, currClose, nextClose, label])

		#reset counts
		targetWeek = currWeek
		offsetthisweek = currDate.isocalendar().weekday-1
		offsetnextweek = 8 - currDate.isocalendar().weekday

		targetWeekCurrMon = currDate - timedelta(days=offsetthisweek)
		targetWeekNextMon = currDate + timedelta(days=offsetnextweek)
		currPos = 0
		currNeu = 0
		currNeg = 0
		currGames = 0
		currAtt = 0

		posReplay = 0
		posRetweet = 0
		posLike = 0
		posQuote = 0

		neuReplay = 0
		neuRetweet = 0
		neuLike = 0
		neuQuote = 0

		negReplay = 0
		negRetweet = 0
		negLike = 0
		negQuote = 0


# resultList.append([currPos, currNeu, currNeg, posPer, neuPer, negPer, currGames, currAtt, targetWeekCurrMon, targetWeekNextMon, currClose, nextClose, label])
resultList.append([currPos, currNeu, currNeg, posPer, neuPer, negPer, posReplay, posRetweet, posLike, posQuote, neuReplay, neuRetweet, neuLike, neuQuote, negReplay, negRetweet, negLike, negQuote, currGames, currAtt, targetWeekCurrMon, targetWeekNextMon, currClose, nextClose, label])


resultDF = pd.DataFrame(resultList, columns = ['PosCt', 'NeuCt', 'NegCt', 'PosPer', 'NeuPer', 'NegPer', 'PosReplay', 'PosRetweet', 'PosLike', 'PosQuote', 'NeuReplay', 'NeuRetweet', 'NeuLike', 'NeuQuote', 'NegReplay', 'NegRetweet', 'NegLike', 'NegQuote', 'Number Games', 'Total Attendance', 'MonDate_current', 'MonDate_next', 'Close_current', 'CLose_next', 'Label'])


resultDF.to_csv("new3_weekData.csv", index=False)

print(resultDF)






