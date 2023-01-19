import dash
import pandas as pd
from dash import html
import dash_bootstrap_components as dbc
from pages.side_bar import sidebar

dash.register_page(__name__)
lfs=pd.read_excel(r'C:\Users\ENVY\PycharmProjects\Censusdash2\assets\LFS_Participation.xlsx')
#import datasets

layout=html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2)
        ]
    )
    ]
)
