from google.colab import files
upload=files.upload()


import csv
import pandas as pd
import plotly.express as px



df=pd.read_csv("main.csv")
gre=df["GRE Score"].tolist()
chance_of_admission=df["Chance of Admit "].tolist()
fig=px.scatter(x=gre,y=chance_of_admission)
fig.show()

m=1
c=0
y=[]

for x in gre:
  y_value=m*x+c
  y.append(y_value)

fig=px.scatter(x=gre,y=chance_of_admission)
fig.update_layout(shapes=[
                          dict(
                              type="line",
                               y0=min(y),y1=max(y),
                               x0=min(gre),x1=max(gre)
                          )
])
fig.show()

m=0.01
c=-2.5
y=[]

for x in gre:
  y_value=m*x+c
  y.append(y_value)

fig=px.scatter(x=gre,y=chance_of_admission)
fig.update_layout(shapes=[
                          dict(
                              type="line",
                               y0=min(y),y1=max(y),
                               x0=min(gre),x1=max(gre)
                          )
])
fig.show()


x=350
y=m*x+c
print(f"chances of admit of {y} will have a gre of {x}")

import numpy as np
gre_array=np.array(gre)
chance_of_admit_array=np.array(chance_of_admission)
m,c=np.polyfit(gre_array,chance_of_admit_array,1)

y=[]
for x in gre_array:
  y_value=m*x+c
  y.append(y_value)

fig=px.scatter(x=gre_array,y=chance_of_admit_array)
fig.update_layout(shapes=[
                          dict(
                              type="line",
                               y0=min(y),y1=max(y),
                               x0=min(gre_array),x1=max(gre_array)
                          )
])
fig.show()


x=5000
y=m*x+c
print(f"chances of admit of {y} will have a gre of {x}")
