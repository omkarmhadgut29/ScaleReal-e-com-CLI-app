from categories import Categories
from products import Product
from biils import Bills
from cart import Cart

class User:
    def __init__(self, user_details):
        self.user_details = user_details
        

    def main(self):
        print("------------------------ Welcome to MyCart -------------------------------")
    
        print(f"Hi {self.user_details[1]}.")
        print("Enter your operation: ")
        print("1) Product Catogories")
        print("2) Cart")
        print("3) Exit")

        choice = int(input("\nEnter your choice(1/2/3): "))
        match choice:
            case 1:
                self.handle_categories()
            case 2:
                self.handle_cart()
            case 3:
                print("\nThank You....")
            case default:
                print("\nEnter right choice........... ")
                next = input("Do you wonted to continue(yes/no): ")
                if next == "yes":
                    print()
                    self.main()

    def handle_categories(self):
        categories = Categories()
        categories.list_of_categories()
        list_categories = categories.categories
        
        print("Categories of produts: ")
        count = 1
        for catogory in list_categories:
            print(f"{count} {catogory[1]}")
            count += 1
        count = 0

        print("\nPress any other number to exit ")

        choice = input("Do you wonted to continue? (yes/no): ")

        if choice == "yes":
            self.handle_produts()
        else:
            self.main()
            
        
    def handle_produts(self):
        print("Enter any other number to exit.")
        categories_choice = int(input("\nEnter your choice: "))

        products = Product()
        products.list_of_products()
        products = products.products
        search_paramiter = False

        print("\n-----------------Products: ----------------")
        new_product_list = []
        count = 1
        for product in products:
            if product[2] == categories_choice:
                print(f"{count} {product[1]}")
                count += 1
                search_paramiter = True
                new_product_list.append(product)
        
        if not search_paramiter:
            self.main()
        else: 
            self.handle_product_detail(new_product_list, categories_choice)

    def handle_product_detail(self, products, categories_choice):
        product_choice = int(input("Enter product (number): ")) - 1

        print(f"Product Name: {products[product_choice][1]}")
        print(f"Product Details: {products[product_choice][3]}")
        print(f"Price: {products[product_choice][4]}")

        print("\n\n1) Add to Cart")
        print("2) Go to products")
        print("3) Go to categories ")
        print("press any other number to exit")

        choice = int(input("Enter your choice(1/2/3): "))

        match choice:
            case 1:
                self.add_product_to_cart(products[product_choice], categories_choice)
            case 2:
                self.handle_produts()
            case 3:
                self.handle_categories()
            case _:
                self.main()

    def add_product_to_cart(self, product, categories_choice):
        cart = Cart()
        cart.view_cart(user_id=self.user_details[0])
        cart.add_to_cart(product, categories_choice, user_id=self.user_details[0])   
        self.handle_cart()

    def handle_cart(self):
        cart = Cart()
        cart.view_cart(user_id=self.user_details[0])
        print("\n\n1) By Now")
        print("2) Delete Product From Cart")
        print("Enter any number to exit\n")

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                bill = Bills()
                bill.genarate_bill(user_id=self.user_details[0])
                self.main()

            case 2:
                product_name = input("\nEnter Product Name: ")
                cart.remove_product(product_name=product_name, user_id=self.user_details[0])
                self.main()

            case _:
                self.main()

