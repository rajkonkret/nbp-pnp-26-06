import pandas as pd

# pip install pandas

data = pd.read_csv('records.csv', delimiter=";")
print(data)

#     name branch  year  cgpa
# 0  Radek    COE     2   9.1
# 1  Radek    COE     2   9.1
# 2  Radek    COE     2   9.1
# 3  Radek    COE     2   9.1
# 4  Radek    COE     2   9.1

print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['Radek' 'COE' 2 9.1]
#  ['Radek' 'COE' 2 9.1]
#  ['Radek' 'COE' 2 9.1]
#  ['Radek' 'COE' 2 9.1]
#  ['Radek' 'COE' 2 9.1]]

print(data.values[0])
# ['Radek' 'COE' 2 9.1]
print(data.items)

# <bound method DataFrame.items of     name branch  year  cgpa
# 0  Radek    COE     2   9.1
# 1  Radek    COE     2   9.1
# 2  Radek    COE     2   9.1
# 3  Radek    COE     2   9.1
# 4  Radek    COE     2   9.1>