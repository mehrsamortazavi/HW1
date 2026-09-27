total_products=0
number_products=0
products={}
maximum=0
minimum=0
while True:
    command=input("enter command:")
    if command=="add":
        product=input("product name:")
        if product in products:
            number=int(input("alredy have this product. say the numbers you want to add: "))
            products[product]+=number
        else:
            number=int(input("the numbers you want to add: "))
            products[product]=number
    elif command=="sell":
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
    elif command=="search":
        product=input("enter the ptoduct name:")
        if product in products:
            print(f"the number left of this product is {products[product]}")
        else:
            print("there is no such a product in the products")
    elif command=="show":
         
        if len(products)==0:
            print("no products available")
        else:
            for product, number in products.items():
                print( product, "-" , number)
    elif command=="save":
        with open ("soal6list.txt", "w") as file:
            for product, numbers in products.items():
                file.write(f"{product}-{numbers}\n")
        print("saved successfully")

    elif command == "report":

        if len(products) == 0:
            print("no products available")

        else:
            total_products = 0
            number_products = 0
            maximum = 0
            minimum = 0
            max_products = []
            min_products = []

            for product, number in products.items():

                total_products += number
                number_products += 1

                if number > maximum:
                    maximum = number
                    max_products = [product]

                elif number == maximum:
                    max_products.append(product)

                if minimum == 0 or number < minimum:
                    minimum = number
                    min_products = [product]

                elif number == minimum:
                    min_products.append(product)

            print("total products are,", number_products)
            print(f"total amount of all of the products is {total_products}")
            print(f"the product with the most numbers is {max_products} with the number of {maximum}")
            print(f"the product with the least numbers is {min_products} with the number of {minimum}")
    elif command=="exit":
        print("bye")
        break
    else:
        print("invalid input")
