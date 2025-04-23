import pandas as pd
import matplotlib.pyplot as plt
# read the csv file:
data=pd.read_csv("C:\\Users\\Administrator\\Desktop\\sumitha\\Pandas\\Loan Data - 2x.csv")
df = pd.DataFrame(data)
# describe the data:
print(df.describe()) 
print(df.describe(include='object'))
# catergory:
print(df.groupby('Loan_Status').size()) 
# plot:
df['Loan_Status'].value_counts().plot(kind='bar')
plt.title("Loan Status Distribution")
plt.xlabel("Status")
plt.ylabel("Count")
plt.show()