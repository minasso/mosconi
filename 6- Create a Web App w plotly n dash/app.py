import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

def get_stats_df():
    import sqlite3
    import pandas as pd
    sql='select * from playerstats'
    con = sqlite3.connect('C://Users//rucku//Desktop//Coding Projects//mosconi//players.db')
    stats = pd.read_sql(sql,con,index_col='index')
    #fix index to start at 1 rather than 0
    stats.index = pd.RangeIndex(start=1, stop=max(stats.index)+2, step=1)
    return stats

df = get_stats_df()
all_stats = df.columns.to_list()[2:]


app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} 
                 for x in all_stats],
        value=all_stats[0],
        multi=False
    ),
    dcc.Dropdown(
        id="dropdown2",
        options=[{"label": x, "value": x} 
                 for x in all_stats],
        value=all_stats[1],
        multi=False
    ),
    dcc.Graph(id="splom"),
])


@app.callback(
    Output("splom", "figure"), 
    [Input("dropdown", "value"),Input("dropdown2", "value")])
def update_chart(x,y):
    fig = px.scatter(data_frame= df, x=x,y=y,text='Player')
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
