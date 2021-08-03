import pandas as pd
import csv
import plotly.figure_factory as ff
df=pd.read_csv("data.csv")
rating=df["rating"].tolist()
graph=ff.create_distplot([rating],["rating"],show_hist=False)
graph.show()