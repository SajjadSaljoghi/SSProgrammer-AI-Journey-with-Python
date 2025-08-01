#practice 1
person = {
    "name" : "Sajjad",
    "age" : 27,
    "language" : ["Python","C#","SQlServer"],
    "goal" : "AI Developer"
}

#practice 2
person["age"] = 25

#practice 3
print(person)

languages = person["language"]
flag = False
for i in range(len(person["language"])):
    if languages[i] == "C++":
        flag = True
if flag == True:
    print("Yes , C++ is exist")
else:
    print("No , C++ dosen't exist")

#practice 4
myLanguages = {"C#" , "Python" , "Html" , "Wordpress" , "Css" , "Sql Server"}

#practice 5
futureLanguages = {"Machne Learning" , "Deep Learning" , "Data Science" , "Python" , "Django"}

#practice 6 - union and intersection
allLanguages = myLanguages.union(futureLanguages)
print("Union (All languages):", allLanguages)

commonLanguages = myLanguages.intersection(futureLanguages)
print("Intersection (Common languages):", commonLanguages)