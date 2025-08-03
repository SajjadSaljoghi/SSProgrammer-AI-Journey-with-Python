import os
import time
from tabulate import tabulate

PRODUCTS = []
BUY_BASKET = []

def read_from_file():
    f = open("database.txt","r")
    for line in f:
        result = line.split(",")
        result_to_dict = {
            "id" : result[0],
            "name" : result[1],
            "price" : result[2],
            "count" : result[3].replace("\n","")
        }

        PRODUCTS.append(result_to_dict)
    f.close()

def show_menu():
    print("1.Add")
    print("2.Edit")
    print("3.Remove")
    print("4.Search")
    print("5.Show List")
    print("6.Buy")
    print("7.Exit")

def add():
    os.system("cls")
    id = input("enter your id = ")
    name = input("enter your name = ")
    price = input("enter your price = ")
    count = input("enter your count = ")
    new_product = {"id" : id , "name" : name , "price" : price , "count" : count}
    PRODUCTS.append(new_product)

def edit():
    os.system("cls")
    searchKey = input("Please Enter Your SearchKey (id , name) = ")
    result = search(searchKey)
    if result == 0:
        input("Pleaase Enter a key to continue .... ")
    else:
        for product in PRODUCTS:
            if product["id"] == result["id"]:
                name = input("enter a name = ")
                price = input("enter a price = ")
                count = input("enter a count = ")
                product["name"] = name
                product["price"] = price
                product["count"] = count

        input("Item Edit Succussfully ! enter a key to continue .... ")


def remove():
    os.system("cls")
    searchKey = input("Please Enter Your SearchKey (id , name) = ")
    result = search(searchKey)
    if result == 0:
        input("Pleaase Enter a key to continue .... ")
    else:
        PRODUCTS.remove(result)
        input("Item deleted ! enter a key to continue .... ")

def search_in_menu():
    os.system("cls")
    searchKey = input("Please Enter Your SearchKey (id , name) = ")
    search(searchKey)
    print("")
    input("Pleasae Enter a key To countinue .... ")

def search(searchKey):
    for product in PRODUCTS:
        if product["id"] == searchKey or product["name"] == searchKey:
            print(tabulate({"id":[product["id"]],"name" : [product["name"]] , "price" : [product["price"]] , "count" : [product["count"]]}
                           ,headers=["id","name","price","count"],tablefmt="simple"))
            return product
    else:
        print("Item Not Find !")
        return 0
    

def show_list():
    os.system("cls")
    print(tabulate(PRODUCTS,headers="keys",tablefmt="grid"))
    print("")
    input("Please Enter a key to continue .... ")

def show_buy_basket():
    print(tabulate(BUY_BASKET , headers="keys" , tablefmt="grid"))
    # for item in BUY_BASKET:
    #     print(tabulate({"name":[item[0]] , "total_price" : [item[1]]} , headers=["name","total_price"] , tablefmt="grid"))
    

def buy():
    while(True):
        os.system("cls")
        print("--------------- Items For Sell --------------")
        print(tabulate(PRODUCTS,headers="keys",tablefmt="grid"))
        print("--------------- Buy Basket --------------")
        if show_buy_basket() == 0:
            print("Basket is Empty .... Please Buy a Item ")
        print("----------------------------------")
        buy_id = input("Please Enter a id to Buy = ")
        for p in PRODUCTS:
            if p["id"] == buy_id:
                count = input("How Many Count To Buy ? ")
                final_count = int(p["count"]) - int(count)
                p["count"] = final_count.__str__()
                BUY_BASKET.append({"name" : p["name"] , "total_price" : int(p["price"]) * int(count)})
                print("Do You Want To Continue to Buy ? 1.yes 2.no")
                continue_to_buy = int(input())
                if continue_to_buy == 2:
                    os.system("cls")
                    print("Item that you buy and pay price : ")
                    print("-----------------------------------")
                    show_buy_basket()
                    input("Pay = ")
                    return
                break
        else:
            result = input("Wrong Id , Try Again .... enter exit if you want to back to menu or a key to continue .... ")
            if result == "exit":
                return

def write_to_file():
    f = open("database.txt","w")
    for product in PRODUCTS:
        f.write(f'{product["id"]},{product["name"]},{product["price"]},{product["count"]}\n')
    f.close()

print("Welcome to My App")
print("Loading ......")
read_from_file()
print("Data Loaded!")
# time.sleep(3)

while(True):

    os.system("cls")
    show_menu()
    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search_in_menu()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        print("Do you Want to save the change ? 1.Yes 2.No")
        result = int(input())
        if result == 1:
            write_to_file()
        elif result == 2:
            exit(0)
        exit(0)
    else:
        print("enter a valid number")
