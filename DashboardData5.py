from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

fig = make_subplots(
    rows=2, cols=9,vertical_spacing = 0.15,horizontal_spacing = 0.07,
    specs=[ [{"secondary_y": True,"colspan": 3}, None, None, {"secondary_y": True,"colspan": 3}, None, None, {"secondary_y": True,"colspan": 3}, None, None],
            [{"secondary_y": True,"colspan": 3}, None, None, {"secondary_y": True,"colspan": 3}, None, None, {"secondary_y": True,"colspan": 3}, None, None],
            ],
subplot_titles=(
    "Price vs Daily % Change on 1-10 Wallets",
    "Price vs Daily % Change on 10-100 Wallets",
    "Price vs Daily % Change on 100-1k Wallets",
    "Price vs Daily % Change on 1k-10k Wallets",
    "Price vs Daily % Change on 10k-100k Wallets",
    "Price vs Daily % Change on Plus 100k Wallets",
    ))

#Chart 01

df1 = pd.read_csv("BCHUSDPRICE.csv")
df2 = pd.read_csv("Porcentajes.csv")
df = pd.read_csv("DashboardData2.csv")

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=1, col=1
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df2.iloc[:,1],name=""),
    secondary_y=True,
    row=1, col=1
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False,ticksuffix=" USD")
fig.update_yaxes(title_text="", secondary_y=True,ticksuffix="%")

#Chart 2

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=1, col=4
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df2.iloc[:,2],name=""),
    secondary_y=True,
    row=1, col=4
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False,ticksuffix="USD")
fig.update_yaxes(title_text="", secondary_y=True,ticksuffix="%")

#Chart 3

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=1, col=7
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df2.iloc[:,3],name=""),
    secondary_y=True,
    row=1, col=7
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False)
fig.update_yaxes(title_text="", secondary_y=True)

#Chart 4

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=2, col=1
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df2.iloc[:,4],name=""),
    secondary_y=True,
    row=2, col=1
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False)
fig.update_yaxes(title_text="", secondary_y=True)

#Chart 5

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=2, col=4
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df2.iloc[:,5],name=""),
    secondary_y=True,
    row=2, col=4
    )
fig.update_xaxes(title_text="")

# Set y-axes titles
fig.update_yaxes(title_text="", secondary_y=False)
fig.update_yaxes(title_text="", secondary_y=True)

#Chart 6

fig.add_trace(
    go.Scatter(x=df.iloc[:,0], y=df1.iloc[:,1],name=""),
    secondary_y=False,
    row=2, col=7
)

fig.add_trace(
    go.Bar(x=df.iloc[:,0], y=df2.iloc[:,6],name=""),
    secondary_y=True,
    row=2, col=7
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