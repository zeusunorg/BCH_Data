import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
from datetime import datetime, time, timedelta
import threading

def historico(symbol, interval='1d', startTime=None, endTime=None, limit=1000):
    
    url = 'https://api.binance.com/api/v3/klines'
    
    params = {'symbol':symbol, 'interval':interval, 
              'startTime':startTime, 'endTime':endTime, 'limit':limit}
        
    r = requests.get(url, params=params)
    js = r.json()
    
    # Armo el dataframe
    cols = ['openTime','Open','High','Low','Close','Volume','cTime',
            'qVolume','trades','takerBase','takerQuote','Ignore']
    
    df = pd.DataFrame(js, columns=cols)
    
    #Convierto los valores strings a numeros
    df = df.apply(pd.to_numeric)
    
    # Le mando indice de timestamp
    df.index = pd.to_datetime(df.openTime, unit='ms')
    
    # Elimino columnas que no quiero
    df =df.drop(['openTime','cTime','takerBase','takerQuote','Ignore'],axis=1)
    
    return df

def historico_binance(par, inicio, timeframe_minutos=1, n_threads=30):

    ts = int(datetime.timestamp(inicio))*1000
    fechas = []
    while ts < int(datetime.timestamp(datetime.now()))*1000:
        fechas.append((ts, ts+60*1000*1000*timeframe_minutos))
        ts += 60*1000*1000*timeframe_minutos
    
    intervalos = {1:'1m',5:'5m',15:'15m',30:'30m',60:'1h',1440:'1d'}
    interval = intervalos.get(timeframe_minutos)
    subs = np.array_split(fechas, n_threads)
    dfs = []
    def worker(fechas):
        for fecha in fechas:
            try:
                df = historico(par, interval=interval, startTime=fecha[0])
            except:
                time.sleep(0.05)
                df = historico(par, interval=interval, startTime=fecha[0])
            dfs.append(df)
        return df


    threads = []
    for i in range(n_threads):
        t = threading.Thread(target=worker, args=(subs[i],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    data = pd.concat(dfs).sort_index()
    data.index = pd.to_datetime(data.index)
    
    return data.dropna()

inicio = datetime(2020,10,10)
par = 'BCHUSDT'

df = historico_binance(par, inicio, timeframe_minutos=1, n_threads=8)   

len(df)
df['hf_sigma'] = df.Close.pct_change().rolling(60).std() * (365*24*60)**0.5*100
df['hf_sigma_zscore'] = (df.hf_sigma - df.hf_sigma.mean()) / df.hf_sigma.std()

plt.style.use('dark_background')
plt.rcParams['figure.dpi'] = 120

fig, ax = plt.subplots(figsize=(12,6))

highs = df.loc[df.hf_sigma_zscore > df.hf_sigma_zscore.quantile(0.95)]
l= 'Quantile 0.95 for HF Volatility (1 min candle)'
ax.scatter(highs.index, highs.hf_sigma_zscore, s=highs.hf_sigma_zscore, color='g', label=l)
ax.set_ylabel('Z-Score for high frequency volatility')
ax.grid(ls='--', color='gray', alpha=0.8)
ax.legend(loc='upper left', markerscale=4, frameon=False)

ax2 = ax.twinx()
ax2.plot(df.Close, lw=0.5, color='w', label='Price')
ax2.set_yscale('log')
ax2.set_ylabel('BCH Spot price (Binance)')

ax.set_title('\nBCH High Frequency Volatility vs Price\n')
plt.show()
print('\n')

df.iloc[-200000:].hf_sigma_zscore.plot(figsize=(8,4), title='HF Volatility')

fig, ax = plt.subplots(figsize=(8,4))
df.hf_sigma_zscore.hist(bins=100, range=(-2,5), ax=ax)
ax.set_title('High Freq Volatility Distribution')
ax.grid(color='silver')

fig, ax = plt.subplots(figsize=(8,4))
df.hf_sigma.hist(bins=100, range=(-2,5), ax=ax)
ax.set_title('High Freq Volatility Distribution')
ax.grid(color='silver')