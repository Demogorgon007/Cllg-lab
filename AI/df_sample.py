import pandas as sample

data = {
    "rollnumber" : [1,2,3],
    "name" : ["manju","anju","renju"],
    "english" : [56,62,29],
    "malayalam" : [25,47,80],
    "science" : [70,85,75],
    "maths" : [35,43,29],
    "Hindi" : [50,75,90]
}
sub = ["english","malayalam","science","maths","Hindi"]
df = sample.DataFrame(data)
print(df)
for i in sub:
    print(f"highest mark of {i}")
    maxmarkname = df['name'].loc[df[i].idxmax()]
    maxmark = df[i].max()
    print(maxmarkname, maxmark, '\n')
