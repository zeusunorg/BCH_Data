import defi.defi_tools as dft
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('dark_background')
plt.rcParams['grid.color'] = "#666"
fig, ax = plt.subplots(figsize=(14,7), nrows=2)

coin = 'bitcoin-cash'
df = dft.geckoHistorical(coin)
df['variacion_diaria'] = df.price.pct_change() *100
df['volatilidad'] = df['variacion_diaria'].rolling(30).std()
df.dropna(inplace=True)
df['percentil'] = df.volatilidad.rank(pct=True) *100
mediana = df.volatilidad.median()

df.volatilidad.hist(bins=100, width=0.5, ax=ax[0])
ax[0].set_title(f'Volatility Histogram {coin.upper()}', fontsize=15)
ax[0].set_xlim(0,10)
ax[0].axvline(mediana, color='white', lw=3)
ax[0].annotate(f'Mediana: {mediana:.2f}', xy=(mediana, 50), color='k', 
               rotation=90,  va='center', ha='right', fontsize=16)

ax[1].plot(df['percentil'].iloc[-365:])
ax[1].set_title(f'Volatility Percentile last 365 days for {coin.upper()} ', fontsize=15)
ax[1].set_ylim(0,100)
ax[1].grid(True)

plt.subplots_adjust(wspace=None, hspace=0.3)
print('')
plt.show()