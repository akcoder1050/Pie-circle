import pandas as p ;
import plotly.express as po ;

df = p.read_csv("data2.csv")

fig = po.line(df, x="Year", y="Per capita income", color="Country", title='Per Capita Income')

fig.show()