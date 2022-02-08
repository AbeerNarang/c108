import csv
import pandas as pd
import plotly.figure_factory as gf

data = pd.read_csv("data.csv")
figure = gf.create_distplot([data["Height(Inches)"].tolist()], ["Height"], show_hist=False)
figure.show()