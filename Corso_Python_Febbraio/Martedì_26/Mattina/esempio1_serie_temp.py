import pandas as pd
import numpy as np

# Generazione delle date
date_range = pd.date_range(start='2021-01-01', periods=10, freq='M')

# Creazione DataFrame
df = pd.DataFrame({
    'date': date_range
}, index=date_range)

# Resampling mensile
s_resampled = df.resample('M').mean()
print(s_resampled)


# esempio: colonna “date” in stringhe → datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# oppure per creare un indice
df.index = pd.to_datetime(df['date'])

# partendo da un DataFrame con indice DatetimeIndex:
df_daily = df.resample('D').mean() # media giornaliera
df_monthly = df.resample('M').sum() # somma mensile

