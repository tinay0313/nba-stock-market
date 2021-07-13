import pandas as pd
from datetime import datetime, timedelta, date
import os.path
import math


filename1 = "2013SP500.csv"
input_df1 = pd.read_csv(filename1)
input_df1 = input_df1.iloc[::-1]
input_df1['Close'] = input_df1['Close'].replace(r',', '', regex=True)
# print(input_df1)

filename2 = "2014SP500.csv"
input_df2 = pd.read_csv(filename2)
input_df2 = input_df2.iloc[::-1]
input_df2['Close'] = input_df2['Close'].replace(r',', '', regex=True)

filename3 = "2015SP500.csv"
input_df3 = pd.read_csv(filename3)
input_df3 = input_df3.iloc[::-1]
input_df3['Close'] = input_df3['Close'].replace(r',', '', regex=True)

filename4 = "2016SP500.csv"
input_df4 = pd.read_csv(filename4)
input_df4 = input_df4.iloc[::-1]
input_df4['Close'] = input_df4['Close'].replace(r',', '', regex=True)

filename5 = "2017SP500.csv"
input_df5 = pd.read_csv(filename5)
input_df5 = input_df5.iloc[::-1]
input_df5['Close'] = input_df5['Close'].replace(r',', '', regex=True)

filename6 = "2018SP500.csv"
input_df6 = pd.read_csv(filename6)
input_df6 = input_df6.iloc[::-1]
input_df6['Close'] = input_df6['Close'].replace(r',', '', regex=True)

filename7 = "2019SP500.csv"
input_df7 = pd.read_csv(filename7)
input_df7 = input_df7.iloc[::-1]
input_df7['Close'] = input_df7['Close'].replace(r',', '', regex=True)

filename8 = "2020SP500.csv"
input_df8 = pd.read_csv(filename8)
input_df8 = input_df8.iloc[::-1]
input_df8['Close'] = input_df8['Close'].replace(r',', '', regex=True)








filename9 = "2012SP500.csv"
input_df9 = pd.read_csv(filename9)
input_df9 = input_df9.iloc[::-1]
input_df9['Close'] = input_df9['Close'].replace(r',', '', regex=True)


filename10 = "2011SP500.csv"
input_df10 = pd.read_csv(filename10)
input_df10 = input_df10.iloc[::-1]
input_df10['Close'] = input_df10['Close'].replace(r',', '', regex=True)


filename11 = "2010SP500.csv"
input_df11 = pd.read_csv(filename11)
input_df11 = input_df11.iloc[::-1]
input_df11['Close'] = input_df11['Close'].replace(r',', '', regex=True)


filename12 = "2009SP500.csv"
input_df12 = pd.read_csv(filename12)
input_df12 = input_df12.iloc[::-1]
input_df12['Close'] = input_df12['Close'].replace(r',', '', regex=True)


filename13 = "2008SP500.csv"
input_df13 = pd.read_csv(filename13)
input_df13 = input_df13.iloc[::-1]
input_df13['Close'] = input_df13['Close'].replace(r',', '', regex=True)


filename14 = "2007SP500.csv"
input_df14 = pd.read_csv(filename14)
input_df14 = input_df14.iloc[::-1]
input_df14['Close'] = input_df14['Close'].replace(r',', '', regex=True)


filename15 = "2006SP500.csv"
input_df15 = pd.read_csv(filename15)
input_df15 = input_df15.iloc[::-1]
input_df15['Close'] = input_df15['Close'].replace(r',', '', regex=True)






filename16 = "2005SP500.csv"
input_df16 = pd.read_csv(filename16)
input_df16 = input_df16.iloc[::-1]
input_df16['Close'] = input_df16['Close'].replace(r',', '', regex=True)

filename17 = "2004SP500.csv"
input_df17 = pd.read_csv(filename17)
input_df17 = input_df17.iloc[::-1]
input_df17['Close'] = input_df17['Close'].replace(r',', '', regex=True)

filename18 = "2003SP500.csv"
input_df18 = pd.read_csv(filename18)
input_df18 = input_df18.iloc[::-1]
input_df18['Close'] = input_df18['Close'].replace(r',', '', regex=True)

filename19 = "2002SP500.csv"
input_df19 = pd.read_csv(filename19)
input_df19 = input_df19.iloc[::-1]
input_df19['Close'] = input_df19['Close'].replace(r',', '', regex=True)

filename20 = "2001SP500.csv"
input_df20 = pd.read_csv(filename20)
input_df20 = input_df20.iloc[::-1]
input_df20['Close'] = input_df20['Close'].replace(r',', '', regex=True)

filename21 = "2000SP500.csv"
input_df21 = pd.read_csv(filename21)
input_df21 = input_df21.iloc[::-1]
input_df21['Close'] = input_df21['Close'].replace(r',', '', regex=True)

filename22 = "1999SP500.csv"
input_df22 = pd.read_csv(filename22)
input_df22 = input_df22.iloc[::-1]
input_df22['Close'] = input_df22['Close'].replace(r',', '', regex=True)




frames = [input_df22, input_df21, input_df20 ,input_df19, input_df18, input_df17, input_df16, input_df15, input_df14, input_df13, input_df12, input_df11, input_df10, input_df9 ,input_df1, input_df2, input_df3, input_df4, input_df5, input_df6, input_df7, input_df8]
result = pd.concat(frames)

print(result)
# result.to_csv("newallsp500_1320.csv", index=False)

result.to_csv("sp500_1999_2020.csv", index=False)





