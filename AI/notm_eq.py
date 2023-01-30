import pandas as pd
df=pd.read_csv("BenderlyZwick.csv")
df_scaled = df.copy()
print(df)

for column in df_scaled.columns:
   df_scaled[column] = (df_scaled[column] - df_scaled[column].min()) / (df_scaled[column].max() - df_scaled[column].min())


print(df_scaled)