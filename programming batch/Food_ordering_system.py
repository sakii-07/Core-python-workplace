# Food ordering system

menu = {
    "Pizza":250,
    "Burger":120,
    "Sandwitch":200,
    "Pasta":180,
    "Cold Drink":50,
    "Coffee":100,
    "Korean Buns":140,
    "Chikan 65":170,
    "Biryani":300,
    "Colcalate boul":120
}

order = {}

def add_item():
    try:
        item = input("Enter the item name : ")
        price = float(input("Enter the price : "))
        if item not in menu.items():
            menu[item] = price
        else:
            print("Item already exist ")
        print("\n Menu added successfully ... \n")
        print()
    except Exception as e:
        print(e)

def view_all_items():
    print("\n --------------- Menu --------------- ")
    for item,price in menu.items():
        print(f"{item} - {price}")

def menu_choice():
    i = 0
    for item in menu.keys():
        print(f"{i+1}. {item}")
        i += 1

def place_order():
    try:

        while(True):
            menu_choice()
            ch = int(input("Enter choice : "))
            i = 1
            for item in menu:
                if i == ch:
                    qty = int(input("Enter quantity: "))
                    if qty > 0 :
                        order[item] = qty
                        print("\n Order placed successfully ...\n")
                        break
                    else:
                        print("\n quantity must be greater than 0 \n")
                i += 1
            
            print("Can you continue, if no then enter (n)")
            choice = input("Enter y / n : ").lower()
            if choice == 'n':
                break

        #     if 
        #         quan = int(input(f"Enter the quantity for {item} : "))
        #         flag = False
        #         if item in menu.keys():
        #             if quan > 0:
        #                 order[item] = quan
        #                 flag = True
        #             else:
        #                 print("\n quantity must be greater than 0 \n")
        #         else:
        #             print("\n Sorry, its not avialable in menu .. \n")
        #     if flag:
        #         print("\n Order placed successfully .. \n")
        # else:
        #     print("Invalid number \n")


    except Exception as e:
        print(e)


def remove_item():
    try:
        item = input("Enter the item name to delete : ")
        if item in order.keys():
            order.pop(item)
            print("\n Item removed successfully .. \n")
    except Exception as e :
        print(e)

def view_all_orders():
    print("\n Your Orders : \n")
    for item,quntity in order.items():
        print(f"{item} - {quntity}\n")

def final_bill():
    try:
        final_bill = 0
        for item, quantity in order.items():
            print(item)
            print("Quantity : ", quantity)
            price  = 0
            if item in menu:
                price = menu[item]
                print("Price : ", price)
                total = quantity*price
                print("Total : ",total)

            final_bill += total

        if final_bill > 1000:
            dis = final_bill * 15/100
            final_bill = final_bill - dis
        elif final_bill > 500:
            dis = final_bill * 5 / 100
            final_bill = final_bill - dis
        else:
            final_bill = final_bill
        
        print("\n Final bill : ",final_bill)
        
    except Exception as e:
        print(e)

def item_vise_bill():
    for item, quantity in order.items():
            print(item)
            print("Quantity : ", quantity)
            if item in menu:
                price = menu[item]
                print("Price : ", price)
                total = quantity*price
                print("Total : ",total)
            print()

while True:

    print("__"*15)
    print()
    print("     Food Ordering System ")
    print("__"*15)

    print("""
1. Add food items to menu
2. Display all avilable food "
3. Place order by selecting food items and quantity"
4. remove an items from the order
5. View the current order summery
6. Generate the final bill
7. Diaplay item wise bill details
8. Exit 
          """)
    
    ch = int(input("Enter your choice : "))

    if ch == 1:
        add_item()
    elif ch == 2:
        view_all_items()
    elif ch == 3:
        place_order()
    elif ch == 4:
        remove_item()
    elif ch == 5:
        view_all_orders()
    elif ch == 6:
        final_bill()
    elif ch == 7:
        item_vise_bill()
    elif ch == 8:
        break
    else:
        print("invalid choice")
