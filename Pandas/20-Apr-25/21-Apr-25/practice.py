
# # stu={}
# # temp={}
# # for x in range(6):
# #     for y in range(6):
# #         temp[y]=input(f'Enter the values[{x,y}]:')
# #     stu[x]=temp
# #     temp={}
# # for x in stu:
# #     for y in stu[x]:
# #         print(stu[x][y],end=" ")
# #     print()

# import pandas as pd
# student={
#     'sumi':{
#         "tamil":89,
#         "english":96,
#         "maths":78,
#         "accounts":99,
#         "commerce":87
#     },
#     'kalis':{
#         "tamil":87,
#         "english":85,
#         "maths":95,
#         "accounts":68,
#         "commerce":97
#     },
#     'jovitha':{
#            "tamil":97,
#         "english":78,
#         "maths":76,
#         "accounts":97,
#         "commerce":91
#     },
#     'srinesh':{
#             "tamil":93,
#         "english":97,
#         "maths":82,
#         "accounts":79,
#         "commerce":88
#     }
# }
# marks=pd.DataFrame(student)
# print(marks)




# stu={}
# temp={}
# mark={}

# for x in range(1):
#     for y in range(1):
#         temp[input("Enter the Key:")]=input("Enter the Name:")
#         for z in range(5):
#             mark[input("Enter the Subject:")]=int(input("Enter the Marks:"))
#         temp[input("Enter The Key:")]=mark
#         mark={}
#     stu[input("Enter The Key:")]=temp
#     temp={}

# print(stu)

# print(pd.DataFrame(stu))


# import pandas as pd
# df = pd.read_excel('C:\\Users\\administrator\\Desktop\\sumitha\Pandas\\20-Apr-25\\21-Apr-25\\Data.xlsx',
# usecols='A:C',skiprows=2, nrows=5)
# print(df.head(5))
# # print(df.tail(5))