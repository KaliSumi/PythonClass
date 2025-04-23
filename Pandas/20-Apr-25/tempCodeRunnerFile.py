import pandas as pd
da=pd.read_csv('Loandata-2x.csv')
k=da.to_string()
print(k)
pd.options.display.max_rows=25
print(pd.options.display.max_rows)