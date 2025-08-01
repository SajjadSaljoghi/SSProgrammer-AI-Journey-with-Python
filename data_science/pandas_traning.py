import pandas as pd

data = {
    "Name" : ["Sara","Ali","Nima","Zahra","Sajjad"],
    "Age" : [22,30,19,25,27],
    "Gender" : ['F','M','M','F','M'],
    "Score" : [88,74,90,68,95]
}

df = pd.DataFrame(data)

print(df)
print("---------------------------")
print(df['Age'])
print("---------------------------")
print(df.loc[2])

#--------End Practice 1

print(df[df['Score'] > 80])
print("---------------------------")
print(df[df['Gender'] == 'F'])
print("---------------------------")
print(df[(df['Age'] > 24) & (df["Score"] > 80)])

#--------End Practice 2

print("Average is = ",df['Score'].mean())
print("---------------------------")
print("Max is = ",df['Score'].max())
print("---------------------------")
print("Count of the rows is = ",len(df))
print("---------------------------")

#--------End Practice 3

df['Grade'] = ['A' if x > 85 else 'B' for x in df['Score']]
print(df)

#--------End Practice 4

print(df.sort_values(by='Score' , ascending=False))


#--------End Practice 5