from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

fig = make_subplots(
    rows=3, cols=9,
    specs=[ [{"secondary_y": True,"colspan": 9},None, None, None, None, None, None, None, None],
            [{"secondary_y": True,"colspan": 3}, None, None, {"secondary_y": True,"colspan": 3}, None, None, {"secondary_y": True,"colspan": 3}, None, None],
            [{"secondary_y": True,"colspan": 3}, None, None, {"secondary_y": True,"colspan": 3}, None, None, {"secondary_y": True,"colspan": 3}, None, None],
            ],
subplot_titles=(
    "Price vs Net Flow",
    "Price vs Cashflow 1-10 Wallets",
    "Price vs Cashflow 10-100 Wallets",
    "Price vs Cashflow 100-1k Wallets",
    "Price vs Cashflow 1k-10k Wallets",
    "Price vs Cashflow 10k-100k Wallets",
    "Price vs Cashflow Plus 100k Wallets",
    ))

#Chart 01

df1 = pd.read_csv("BCHUSDPRICE.csv")
df = pd.read_csv("DashboardData2.csv")

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=1, col=1
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df.iloc[:,19],name=""),
    secondary_y=True,
    row=1, col=1
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False)
fig.update_yaxes(title_text="", secondary_y=True)

#Chart 2

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=2, col=1
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df.iloc[:,13],name=""),
    secondary_y=True,
    row=2, col=1
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False)
fig.update_yaxes(title_text="", secondary_y=True)

#Chart 3

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=2, col=4
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df.iloc[:,14],name=""),
    secondary_y=True,
    row=2, col=4
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False)
fig.update_yaxes(title_text="", secondary_y=True)

#Chart 4

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=2, col=7
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df.iloc[:,15],name=""),
    secondary_y=True,
    row=2, col=7
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False)
fig.update_yaxes(title_text="", secondary_y=True)

#Chart 5

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=3, col=1
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df.iloc[:,16],name=""),
    secondary_y=True,
    row=3, col=1
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False)
fig.update_yaxes(title_text="", secondary_y=True)

#Chart 6

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=3, col=4
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df.iloc[:,17],name=""),
    secondary_y=True,
    row=3, col=4
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False)
fig.update_yaxes(title_text="", secondary_y=True)

#Chart 7

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=3, col=7
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df.iloc[:,18],name=""),
    secondary_y=True,
    row=3, col=7
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False)
fig.update_yaxes(title_text="", secondary_y=True,showgrid = False)

#Plot, Layout & Template

fig.update_layout(height=1080, width=1920, showlegend=False, title_text="BCH Dashboard - Beta")
for template in ["plotly_dark"]:
    fig.update_layout(template=template)

fig.show()