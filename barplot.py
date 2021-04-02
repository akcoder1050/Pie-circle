import pandas as p ;
import plotly.express as po ;

df = p.read_csv("data1.csv")

fig = po.bar(df, x="Country", y="InternetUsers", color="Per capita", title='Population')

fig.show()                  