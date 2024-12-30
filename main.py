import pandas as pd

df = pd.read_csv('employee_data.txt',
                 na_values=['', 'None', ' '],
                 skipinitialspace=True,
                 parse_dates=['JoinDate'],
                 delim_whitespace=True)

df.info()


# 1
missing_columns = df.columns[df.isnull().any()]
print("Columns with missing data:", list(missing_columns))
# 2
missing_count = df.isnull().sum()

print("missing in each collumn")
print(missing_count)

# 3

df_dropr = df.dropna()

print('dropping rows with missing values: ')
print(df_dropr)

# 4
df_dropc = df.dropna(axis=1)
print(df_dropc)

# 5

df_fill = df.fillna('*')

print('after fillinf missing spots with *')
print(df_fill)

# 6

df_ffill = df.fillna(method='ffill')

print("forward fill")
print(df_ffill)


