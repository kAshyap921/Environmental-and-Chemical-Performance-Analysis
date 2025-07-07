import pandas as pd

def calculate_score(df):
    df['CHEMFAST_SCORE'] = (df['ECO%']*0.3333) + (df['Ach%']*0.3333) + (df['WOA%']*0.3333)
    return df

# Example usage
data = {'Branch': ['RAJASTHAN'], 'ECO%': [0.9104], 'Ach%': [0.4569], 'WOA%': [0.1244]}
df = pd.DataFrame(data)
print(calculate_score(df))
