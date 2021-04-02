import pandas as p ;
import plotly.express as po ;

df = p.read_csv("data1.csv")

fig = po.scatter(df, x="Per capita", y="Country", size="Percentage",color="Population", size_max=60)

fig.show()                  