import pandas as pd

data = {
    'Name' : ['Sajjad','AliReza','Amir'],
    'Age' : ['25','27','18'],
    'Job' : ['Developer','Developer','Designer']
}

df = pd.DataFrame(data)

print(df)