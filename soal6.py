def add(products):
        product=input("product name:")
        if product in products:
            number=int(input("alredy have this product. say the numbers you want to add: "))
            products[product]+=number
        else:
            number=int(input("the numbers you want to add: "))
            products[product]=number
def sell(products):
     product=input("product name:")
     number=int(input("enter the number of this product u want to sell:"))
     if product in products and number<=products[product]:
         products[product]-=number
         print("sold.")
         print(f"the number left of {product} is {products[product]}")
         if products[product]==0:
            del products[product]
     elif product not in products:
            print(f"This product is not in products")
     else:
            print("you asked more than available")
def  search(products):
        product=input("enter the ptoduct name:")
        if product in products:
            print(f"the number left of this product is {products[product]}")
        else:
            print("there is no such a product in the products")
def show(products):
    if len(products)==0:
        print("no products available")
    else:
        for product, number in products.items():
            print( product, "-" , number)
def save (products):
     with open ("soal6list.txt", "w") as file:
        for product, numbers in products.items():
            file.write(f"{product}-{numbers}\n")
     print("saved successfully")
def report(products):
    if not products:
        print("no products available")
        return
    total_products = 0
    maximum = 0
    minimum = 0
    max_products = []
    min_products = []
    for product, number in products.items():
        total_products+=number
        if number>maximum:
            maximum = number
            max_products=[product]
        elif number== maximum:
            max_products.append(product)
        if minimum==0 or number<minimum:
            minimum=number
            min_products=[product]
        elif number==minimum:
            min_products.append(product)
    print("total products are,", len(products))
    print(f"total amount of all of the products is {total_products}")
    print(f"the products with the most numbers are {max_products} with the number of {maximum}")
    print(f"the products with the least numbers are {min_products} with the number of {minimum}")
products = {}
while True:
    command = input("enter command:")
    if command == "add":
        add(products)
    elif command == "sell":
        sell(products)
    elif command == "search":
        search(products)
    elif command == "show":
        show(products)
    elif command == "save":
        save(products)
    elif command=="report":
        report(products)
    elif command == "exit":
        print("bye")
        break
    else:
        print("invalid input")
