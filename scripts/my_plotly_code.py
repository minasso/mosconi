#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import plotly.express as px
import sqlite3

def get_stats_df():
    sql='select * from playerstats'
    con = sqlite3.connect('C://Users//rucku//Desktop//Coding Projects//mosconi//players.db')
    stats = pd.read_sql(sql,con,index_col='index')
    #fix index to start at 1 rather than 0
    stats.index = pd.RangeIndex(start=1, stop=max(stats.index)+2, step=1)
    return stats

def top_n(df, n = 10, stat_col = 'Cwin'):
    '''
    Return df displaying the top n players for a given stat column and generate a plotly image of that data
    '''
    frame = df.nlargest(n, stat_col)
    frame.index= pd.RangeIndex(start=1, stop=len(frame)+1, step=1)
    fig = px.scatter(data_frame=frame,x='Cmp',y='Cwin',text='Player')
    return frame, fig
    


def main():
    stats = get_stats_df()
    frame, fig = top_n(df = stats, n = 10, stat_col = 'Cpct')
    fig.show()

if __name__ == "__main__":
	main()