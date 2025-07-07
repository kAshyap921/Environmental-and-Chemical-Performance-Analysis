import pandas as pd

data = {
    'Branch': ['DELHI 1', 'GUWAHATI', 'VIZAG'],
    'Enrolled': [190, 9, 31],
    'Visited': [190, 9, 13]
}

df = pd.DataFrame(data)
df['ECO%'] = df['Visited']/df['Enrolled']
print(df.sort_values('ECO%', ascending=False))
