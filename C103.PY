import pandas as pd
#data=[1,2,3,4,5]
#df=pd.DataFrame()
import plotly.express as px
df=pd.read_csv('line_chart.csv')
print(df)
fig=px.line(df,x='Year',y='Per capita income',color='Country',title='Per capita income')
fig.show()