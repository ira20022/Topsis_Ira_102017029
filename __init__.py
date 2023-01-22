import pandas as pd
from Topsis_Ira_102017029.topsis import topsis
df=pd.read_csv('data.csv')
topsis(df,"0.25,0.25,0.25,0.25,0.25","-,+,+,+,+")
