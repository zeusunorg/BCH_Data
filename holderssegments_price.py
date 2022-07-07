from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
import plotly.graph_objs as go
import io
from plotly.offline import plot
import yfinance as yf
pd.options.plotting.backend = "plotly"

fig = make_subplots(rows=4, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.05,
                    subplot_titles=("BCH Price", "10 to 100 Wallets", "100 to 1k Wallets", "1k to 10k Wallets"))

data = yf.download(tickers="BCH-USD", period = "5d", interval = "1H", rounding= True)

fig.add_trace(go.Candlestick(x=data.index,open = data["Open"], high=data["High"], low=data["Low"], close=data["Close"], name = "market data"))
fig.update_layout(title = "BCH Price", yaxis_title = "BCH Price")
fig.update_xaxes(
rangeslider_visible=False,
)
         
df = pd.read_csv("holdaddresses1k10kprice.csv")

fig.add_trace(go.Scatter(x=df.iloc[:,0], y=df.iloc[:,2], name="Coins Held"),
              row=4, col=1)

df = pd.read_csv("holdaddresses10100price.csv")

fig.add_trace(go.Scatter(x=df.iloc[:,0], y=df.iloc[:,2], name="Coins Held"),
              row=2, col=1)

df = pd.read_csv("holdaddresses1001000price.csv")

fig.add_trace(go.Scatter(x=df.iloc[:,0], y=df.iloc[:,2], name="Coins Held"),
              row=3, col=1)

fig.update_layout(height=600, width=1200,
                  title_text="BCH Price & Wallets Segments", title_x=0.5)
                  
for template in ["plotly_dark"]:
    fig.update_layout(template=template)
fig.show()
