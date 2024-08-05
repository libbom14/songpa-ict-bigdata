import pandas as pd

# cdc csv 불러오기
cdc = pd.read_csv('cdc.txt')
cdc

# cars93 csv 불러오기
cars = pd.read_csv('cars93.csv')
cars

# test excel 형식의 외부파일 불러오기
test = pd.read_excel('test.xlsx')
test
