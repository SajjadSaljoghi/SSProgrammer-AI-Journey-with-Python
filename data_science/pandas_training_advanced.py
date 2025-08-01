import pandas as pd

studentData = {
    "Name" : ["Sajjad","Amir","Alireza","Zahra","Ariyan"],
    "Age" : [25,18,27,21,20],
    "GPA" : [19.5,18,17.75,15,20],
    "Field" : ["AI Developer","Designer","Speech AI","literature","AI Developer"]
}

Student_df = pd.DataFrame(studentData)

print("-----------------------Practice 1 --------------------------")

print(Student_df[Student_df["GPA"] > 17])

Student_df["Result"] = ["Pass" if x > 15 else "Fail" for x in Student_df["GPA"]]

print("---------------------------------------------------------")
print(Student_df)
print("---------------------------------------------------------")

#end of Practice 1
print("-----------------------Practice 2 --------------------------")
bookData = {
    "Name" : ["Little Women","The Scarlet Letter","The Magic","One Hundred Years of Solitude","The Little Prince"],
    "Author" : ["Louisa May Alcott","Nathaniel Hawthorne","Rhonda Byrne","Gabriel García Márquez","Antoine de Saint-Exupéry"],
    "Publication" : [1868,1850,2025,2022,2023]
}

book_df = pd.DataFrame(bookData)

print(book_df[book_df["Publication"] > 2015])
print("---------------------------------------------------------")

book_df["Classic"] = ["Yes" if x < 2010 else "No" for x in book_df["Publication"]]
print(book_df)
print("---------------------------------------------------------")

#end of Practice 2
print("-----------------------Practice 3 --------------------------")

storeData = {
    "Month" : ["Farvardin","Ordibehesht","Khordad","Tir"],
    "Sale" : [200000,250000,150000,300000],
    "AdvertisingCost" : [30000,40000,25000,50000]
}

store_df = pd.DataFrame(storeData)

store_df["Profit"] = store_df["Sale"] - store_df["AdvertisingCost"]
print(store_df)
print("---------------------------------------------------------")

#--------- My Pattern ------------------------------------
# maxProfit = []
# for i in range(len(store_df)):
#     if store_df["Profit"].loc[i] == store_df["Profit"].max():
#         maxProfit = store_df.loc[i]

#------------ AI Pattern (1) ------------------------------------
maxProfit = store_df[store_df["Profit"] == store_df["Profit"].max()]

print(maxProfit)

#------------ AI Pattern (2) ------------------------------------
# print(store_df.loc[store_df["Profit"].idxmax()])

#end of Practice 3