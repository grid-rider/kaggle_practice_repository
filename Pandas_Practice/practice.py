import pandas as pd 
from sklearn.impute import SimpleImputer

def returner(x):
    print(x.Jens)
    return 0 

df = pd.DataFrame({"Armin": [1,None,None], "Jens":[2,3,4]}, index=["one","two","three"])

imputer = SimpleImputer()

print(imputer.fit_transform(df))



