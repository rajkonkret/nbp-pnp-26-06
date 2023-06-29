import pandas as pd

excel_data = pd.read_excel("sales.xlsx")
data = pd.DataFrame(excel_data)

print("The content is:\n", data)
