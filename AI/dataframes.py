import pandas as np

data = {
    'name': ["ajay", "sharon", "iqbal", "christy", "shibin", "abhijith"],
    'roll number': ["001", "002", "003", "004", "005", "006"],
    'Maths': [90, 95, 80, 90, 80, 85],
    'English': [40, 50, 70, 46, 25, 70],
    'Science': [80, 30, 10, 50, 70, 90]
}

subject = ['Maths','English','Science']
df = np.DataFrame(data)

for i in subject:
    print(f"Highest mark for {i}")
    maxMarkName = df['name'].loc[df[i].idxmax()]
    maxMark = df[i].max()
    print(maxMarkName, maxMark, '\n')
