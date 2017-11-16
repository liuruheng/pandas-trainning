#coding=utf-8

DETAIL_URL = 'http://blog.csdn.net/hjxzb/article/details/70677483'

import pandas as pd
from pandas import Series,DataFrame
import trace
import matplotlib.finance
import matplotlib.dates
import talib
#pd.DataFrame
#con = pymysql.connect(host="127.0.0.1",user="root",password="password",db="world")
#data_sql=pd.read_sql("select * from city limit 10",con)
#print(data_sql)

#def test():
    #"""Test"""
    #talib.SMA()

def dataframe_trainning():
    """"""
    data = {'state':['1','2'],'year':['a','b'],'pop':['x','y']}
    frame = DataFrame(data)
    print frame

def dataframe_trainning_dict():
    """"""
    data = {'state':{'one':'1'},'year':{'one':'2'},'pop':{'three':'3'}}
    frame = DataFrame(data)
    print frame
    print '=== ==='
    print frame['pop']
    print '=== ==='
    print frame.ix['one']

def dataframe_trainning_append():
    """"""
    data = {'state':{'one':'1'},'year':{'one':'2'},'pop':{'three':'3'}}
    df = DataFrame(data)

    df['william'] = ['korea','china']
    #增加列
    df['spring'] = ['usa','Japan']
    #增加行
    data1 = {'state':{'one':'1','four':'23'},'spring':{'four':'45','two':'2'}}
    df1 = DataFrame(data1)
    df = df.append(df1)
    #print df.index, df.columns
    print df
    print '==== ==== ===='
    print df.ix['one']



if __name__ == '__main__':
    dataframe_trainning_append()