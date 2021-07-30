import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("pixelMath/data.csv")
print(df.groupby("level")["attempt"].mean())
mean = df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
stddf = df.loc[df["student_id"]=="TRL_rst"]
fig = px.scatter(mean,
    x = "student_id",
    y = ["level"],
    size = "attempt",
    color = "attempt",
)
fig.show()