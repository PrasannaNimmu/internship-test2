import pandas as pd
import csv
url = 'https://raw.githubusercontent.com/Bungeetech/internship-test2/master/input/question-1/main.csv'
df = pd.read_csv(url,index_col=0)
df = df.drop('Population', 1)
df1 = df[:10]
with open('https://raw.githubusercontent.com/PrasannaNimmu/internship-test2/master/output/answer-1/main.csv', 'w', newline='') as file:
    fieldnames = ['Year','Total,Violent','Property','Murder','Forcible_Rape','Robbery','Aggravated_assault','Burglary','Larceny_Theft','Vehicle_Theft']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
df1 = df.groupby((df.index//10)*10).sum()
df1.to_csv('C:/Users/3567/Documents/Bungee/answer-1.csv')
