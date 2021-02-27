# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# https://www.youtube.com/watch?v=R6CCTuHast0

import plotly.express as px
import pandas as pd


df = pd.read_json('http://api.open-notify.org/iss-now.json')
print(df)

df["latitude"] = df.loc["latitude", "iss_position"]
df["longitude"] = df.loc["longitude", "iss_position"]
df.reset_index(inplace=True)

df = df.drop(["index", "message"], axis=1)

print(df)
fig = px.scatter_geo(df, lat="latitude", lon="longitude")
fig.show()
