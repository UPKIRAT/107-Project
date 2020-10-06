import pandas as pd
import plotly.express as px
import csv

read = pd.read_csv("data.csv")
mean = read.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
fig = px.scatter(mean, x = "student_id", y = "level")
print(mean)
fig.show()