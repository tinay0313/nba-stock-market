from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

# 2020
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1601510400&period2=1609372800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1593561600&period2=1601424000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1585699200&period2=1593475200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1577836800&period2=1585612800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2019
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1569888000&period2=1577750400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1561939200&period2=1569801600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1554076800&period2=1561852800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1546300800&period2=1553990400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2018
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1538352000&period2=1546214400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1530403200&period2=1538265600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1522540800&period2=1530316800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1514764800&period2=1522454400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2017
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1506816000&period2=1514678400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1498867200&period2=1506729600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1491004800&period2=1498780800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1483228800&period2=1490918400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2016
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1475280000&period2=1483142400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1467331200&period2=1475193600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1459468800&period2=1467244800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1451606400&period2=1459382400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2015
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1443657600&period2=1451520000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1435708800&period2=1443571200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1427846400&period2=1435622400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1420070400&period2=1427760000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2014
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1412121600&period2=1419984000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1404172800&period2=1412035200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1396310400&period2=1404086400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1388534400&period2=1396224000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2013
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1380585600&period2=1388448000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1372636800&period2=1380499200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1364774400&period2=1372550400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1356998400&period2=1364688000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2012
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1349049600&period2=1356912000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1341100800&period2=1348963200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1333238400&period2=1341014400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1325376000&period2=1333152000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2011
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1317427200&period2=1325289600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1309478400&period2=1317340800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1301616000&period2=1309392000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1293840000&period2=1301529600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2010
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1285891200&period2=1293753600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1277942400&period2=1285804800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1270080000&period2=1277856000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1262304000&period2=1269993600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2009
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1254355200&period2=1262217600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1246406400&period2=1254268800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1238544000&period2=1246320000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1230768000&period2=1238457600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'


# 2008
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1222819200&period2=1230681600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1214870400&period2=1222732800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1207008000&period2=1214784000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1199145600&period2=1206921600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'


# 2007
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1191196800&period2=1199059200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1183248000&period2=1191110400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1175385600&period2=1183161600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1167609600&period2=1175299200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2006
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1159660800&period2=1167523200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1151712000&period2=1159574400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1143849600&period2=1151625600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1136073600&period2=1143763200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'


# 2005
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1128124800&period2=1135987200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1120176000&period2=1128038400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1112313600&period2=1120089600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1104537600&period2=1112227200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'


# 2004
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1096588800&period2=1104451200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1088640000&period2=1096502400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1078099200&period2=1088553600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1072915200&period2=1080691200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2003
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1064966400&period2=1072828800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1057017600&period2=1064880000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1049155200&period2=1056931200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1041379200&period2=1049068800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2002
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1033430400&period2=1041292800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1025481600&period2=1033344000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1017619200&period2=1025395200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1009843200&period2=1017532800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2001
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=1001894400&period2=1009756800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=993945600&period2=1001808000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=986083200&period2=993859200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=978307200&period2=985996800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 2000
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=970358400&period2=978220800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=962409600&period2=970272000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=954547200&period2=962323200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=946684800&period2=954460800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

# 1999
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=938736000&period2=946598400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=930787200&period2=938649600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
# URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=922924800&period2=930700800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
URL = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=915148800&period2=922838400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')


df = pd.DataFrame(columns = ['Date','Close'])
alldata = soup.select('tbody')
alldata = alldata[0].select('tr')

for elm in alldata:
	time = elm.select('td')[0].find('span').text
	datetime_object = datetime.strptime(time, "%b %d, %Y")
	close = elm.select('td')[4].find('span').text
	df = df.append({'Date':datetime_object, 'Close':close}, ignore_index=True)
	# print(time)
	# print(close)

print(df)

file_name = 'test.csv'
with open(file_name, 'a') as f:
    df.to_csv(f, header=False, index=False)

# df.to_csv('test.csv', index=False)



