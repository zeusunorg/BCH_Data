from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import io
from plotly.offline import plot
from sqlalchemy import true
import yfinance as yf
pd.options.plotting.backend = "plotly"

fig = make_subplots(rows=4, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.10,
                    subplot_titles=("Price", "100-1k", "1k-10k", "10k-100k"))

data = yf.download(tickers="BCH-USD", period = "15d", interval = "1H", rounding= True)

fig.add_trace(go.Candlestick(x=data.index,open = data["Open"], high=data["High"], low=data["Low"], close=data["Close"], name = "market data"))
fig.update_layout(title = "BCH Price", yaxis_title = "BCH Price")
fig.update_xaxes(
rangeslider_visible=False,
)

df = pd.read_csv("CashFlowSegm.csv")
fig.add_trace(go.Bar(x=df.iloc[:,0], y=df.iloc[:,3],name="10k-100k"),
              row=4, col=1)

df = pd.read_csv("CashFlowSegm.csv")
fig.add_trace(go.Bar(x=df.iloc[:,0], y=df.iloc[:,2],name="1k-10k"),
              row=3, col=1)

df = pd.read_csv("CashFlowSegm.csv")
fig.add_trace(go.Bar(x=df.iloc[:,0], y=df.iloc[:,1],name="100-1k"),
              row=2, col=1)



fig.update_layout(height=600, width=1200,
                  title_text="BCH NetFlows", title_x=0.5)
                  
for template in ["plotly_dark"]:
    fig.update_layout(template=template)
fig.show()