import pandas as pd


a = pd.DataFrame({"Coloumn_1": [1,2], "Coloumn_2": [3,4]})
b = pd.DataFrame({"Coloumn_1": [1,2], "Coloumn_2": [3,4]}, index = ["row1","row2"])

print(a)
print(b)