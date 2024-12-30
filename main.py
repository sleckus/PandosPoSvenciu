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