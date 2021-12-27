import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

def get_df(table):
    import sqlite3
    import pandas as pd
    sql=f'select * from {table}'
    con = sqlite3.connect('C://Users//rucku//Desktop//Coding Projects//mosconi//players.db')
    df = pd.read_sql(sql,con,index_col='index')
    df.index = pd.RangeIndex(start=1, stop=max(df.index)+2, step=1)  #make index start at 1
    return df

playerstats_df = get_df('playerstats')
stat_list = playerstats_df.columns.to_list()[2:]

app = dash.Dash(__name__)

app.layout = html.Div([
     html.H1(children='Use the dropdowns to select x and y axes', style={
        'textAlign': 'center'
    }),
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} 
                 for x in stat_list],
        value=stat_list[0],
        placeholder='x',
        multi=False
    ),
    dcc.Dropdown(
        id="dropdown2",
        options=[{"label": x, "value": x} 
                 for x in stat_list],
        value=stat_list[1],
        placeholder='y',
        multi=False
    ),
    dcc.Graph(id="splom"),
])


@app.callback(
    Output("splom", "figure"), 
    [Input("dropdown", "value"),Input("dropdown2", "value")])
def update_chart(x,y):
    fig = px.scatter(data_frame= playerstats_df, x=x,y=y,text='Player')
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
