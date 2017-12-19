def imp(table):   
    '''import a table from players.db''' 
    import pandas as pd
    import os
    parent = os.path.abspath('../..')
    path = os.path.join(parent,'players.db')
    import sqlite3
    con = sqlite3.connect(path)
    with con:
        df = pd.read_sql('select * from {}'.format(table),con)
    return df
