import pandas as pd

df = pd.read_csv ('Dis.csv')
df = df[df.CountryCode == 'Average']
df = df[df.answer == "Yes"]
df = df[df.subset == "Transgender"]
df.reset_index(drop=True, inplace=True)
for i in range(len(df)):
    print(df['question_label'][i]+'\n'+ df['percentage'][i])
