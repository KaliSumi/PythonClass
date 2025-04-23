# import pandas
# toy = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# table=pandas.DataFrame(toy)
'''
A DataFrame in Pandas is a two-dimensional labeled data structure that can hold data of various types (such as integers, floats, strings, etc.). 
It is essentially a table, similar 
to a spreadsheet or SQL table,
where data is arranged in rows and columns
'''
# print(pandas.__version__) # To Check Pandas Version


'''
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.
'''
#Labels
# import pandas 
# a = ['1', '7', '2']
# myvar = pandas.Series(a)
# print(myvar)

# print(myvar[0])
# print(myvar[1])
# print(myvar[2])




# #Create Labels
# import pandas 
# a = ['1', '7', '2']
# myvar = pandas.Series(a,index=['😀','🫡','😺'])
# print(myvar)

# #Key/Value Objects as Series
# import pandas as pd

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)

# print(myvar)


# #Locate Row
# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data)

# print(df.loc[0])


# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data)

# print(df.loc[[0,1]])

#to read csv file and generate a table with row and col
# import pandas as pd
# df=pd.read_csv('members.csv')
# k=df.to_string()
# print(k)
# pd.options.display.max_rows=100
# print(pd.options.display.max_rows)


# #to read json file and generate a table with row and col
# from pandas import *
# l=read_json('mem.json')
# print(l.to_string())


# from pandas import *
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }


# sumi=DataFrame(data)
# print(sumi)


# #Pandas - Analyzing DataFrames
# from pandas import * 
# p=read_csv('data.csv')
# # print(p.tail(5))
# # print(p.head(20))
# p.info()



import pandas as pd
da=pd.read_csv('\\aptserver\\Aptech\\Python & MySQL\\sumitha\\Pandas\\Loan Data - 2x.csv')
k=da.to_string()
print(k)
pd.options.display.max_rows=25
print(pd.options.display.max_rows)