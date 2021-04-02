import pandas as p ;
import plotly.express as po ;

df = p.read_csv("data1.csv")

fig = po.pie(df, values="InternetUsers", names='Country', title='Population')

fig.show()