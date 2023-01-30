from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = pd.read_csv("Affairs.csv")
age = data["age"]

scaler = MinMaxScaler()

normalized_data = scaler.fit_transform(age)

print(normalized_data)

