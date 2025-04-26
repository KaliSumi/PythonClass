import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\\Administrator\\Desktop\\sumitha\\Pandas\\Loan Data - 2x.csv")
df = pd.DataFrame(data)
print(df.describe()) 
print(df.describe(include='object'))
print(df.groupby('Loan_Status').size()) 
df['Loan_Status'].value_counts().plot(kind='bar')
plt.title("Loan Status Distribution")
plt.xlabel("Status")
plt.ylabel("Count")
plt.show()



















