from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import yfinance as yf

fig = make_subplots(
    rows=3, cols=6,
    specs=[ [{"colspan": 3}, None, None, {"colspan": 3}, None, None],
            [{},{},{},{},{},{}],
            [{},{},{},{},{},{}],
            ],
    subplot_titles=("Binance Price","Volume", "1-10 Addresses", "10-100 Addresses", "100-1k Addresses", "1-10 Cash Flow", "10-100 Cash Flow", "100-1k Cash Flow","1k-10k Addresses", "10k-100k Addresses", "Plus 100k Addresses", "1k-10k Cash Flow","10k-100k Cash Flow","Plus 100k Cash Flow"))

#PriceChart from Binance

data = yf.download(tickers="BCH-USD", period = "7d", interval = "1H", rounding= True)

fig.add_trace(go.Candlestick(x=data.index,open = data["Open"], high=data["High"], low=data["Low"], close=data["Close"], name = "market data"),
row=1, col=1),
fig.update_layout(title = "BCH Price", yaxis_title = "BCH Price")
fig.update_xaxes(
rangeslider_visible=False,
)
df = yf.download(tickers="BCH-USD", period = "7d", interval = "1H", rounding= True)
#Volume Chart on Binance
fig.add_trace(go.Bar(x=df.index, 
                     y=df['Volume']),
                     row=1, col=4)

#Wallets Coins and Addresses source CSV File

df = pd.read_csv("DashboardData.csv")

#Wallets Coins and Addresses charts

fig.add_trace(go.Scatter(x=df.iloc[:,0], y=df.iloc[:,3], name="..."),
                 row=2, col=3)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=df.iloc[:,2], name="..."),
                 row=2, col=2)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=df.iloc[:,1], name="..."),
              row=2, col=1)

fig.add_trace(go.Scatter(x=df.iloc[:,0], y=df.iloc[:,4], name="..."),
                 row=3, col=3)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=df.iloc[:,5], name="..."),
                 row=3, col=2)
fig.add_trace(go.Scatter(x=df.iloc[:,0], y=df.iloc[:,6], name="..."),
                 row=3, col=1)

#NetFlows on USD Daily

fig.add_trace(go.Bar(x=df.iloc[:,0], y=df.iloc[:,15],name="100-1k"),
                 row=2, col=6)
fig.add_trace(go.Bar(x=df.iloc[:,0], y=df.iloc[:,14],name="10-100"),
                 row=2, col=5)
fig.add_trace(go.Bar(x=df.iloc[:,0], y=df.iloc[:,13],name="1-10"),
                 row=2, col=4)
fig.add_trace(go.Bar(x=df.iloc[:,0], y=df.iloc[:,18],name="Plus 100k"),
                 row=3, col=6)
fig.add_trace(go.Bar(x=df.iloc[:,0], y=df.iloc[:,17],name="10k-100k"),
                 row=3, col=5)
fig.add_trace(go.Bar(x=df.iloc[:,0], y=df.iloc[:,16],name="1k-10k"),
                 row=3, col=4)


fig.update_layout(height=2160, width=3840, showlegend=False, title_text="BCH Dashboard Beta")
for template in ["plotly_dark"]:
    fig.update_layout(template=template)
fig.show()