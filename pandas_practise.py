#coding=utf-8

DETAIL_URL = 'http://blog.csdn.net/hjxzb/article/details/70677483'

import pymysql
import pandas as pd
import trace
import matplotlib.finance
import matplotlib.dates
import talib
pd.DataFrame
con = pymysql.connect(host="127.0.0.1",user="root",password="password",db="world")
data_sql=pd.read_sql("select * from city limit 10",con)
print(data_sql)

def test():
    """Test"""
    talib.SMA()