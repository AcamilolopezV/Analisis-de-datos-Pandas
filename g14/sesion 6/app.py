import pandas as pd

notas = [3.5,4,5,3.2,4.6,3.5]
series = pd.Series(notas)

df = pd.DataFrame(notas)
print(df)
print(notas)
#muestra la media de las ntoas
print(series.mean())
#muestra y describe el data set, muestra valores minimos, maximos , cuenta cuantos ahi, muetra la media
print(series.describe())
#elemento que mas se repite
print(series.mode())

