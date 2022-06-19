from biils import Bills
from cart import Cart
from categories import Categories
from products import Product
from conn import ecom_cursor

class Admin:
    def __init__(self, admin_details):
        self.is_admin = admin_details[4]

    def main(self):
        print("\n--------Welcome to MyCart-------------\n")

        print("What do you wonted to do? ")
        print("1) Add Category")
        print("2) Add Product")
        print("3) View Carts Products")
        print("4) View Bills")

        choice = int(input("\nEnter Your Choice: "))
        match choice:
            case 1:
                self.handle_categories()
            case 2:
                self.handle_add_product()
            case 3:
                self.handle_view_cart()
            case 4:
                self.handle_bills()
            case _:
                pass
        
    def handle_categories(self):
        categories = Categories()
        categories.add_categories()
        print("\n\n")
        self.main()

    def handle_add_product(self):
        categories = Categories()
        categories.list_of_categories()
        list_categories = categories.categories

        print("Categories of produts: ")
        count = 1
        for catogory in list_categories:
            print(f"{count} {catogory[1]}")
            count += 1
        count = 0

        choice_catogory = int(input("Enter product category: "))

        category_id = list_categories[choice_catogory - 1][0]

        products = Product()
        products.add_products(category_id)

        self.main()

    def handle_view_cart(self):

        ecom_cursor.execute("SELECT * from user")

        result = ecom_cursor.fetchall()

        count = 1
        for user in result:
            print(f"{count}) {user[1]}")
            count += 1
        count = 0

        choice = int(input("Which Users Cart you wonted to view: "))

        selected_user = result[choice - 1]
        user_id = selected_user[0]

        cart = Cart()
        cart.view_cart(user_id)

        self.main()

    def handle_bills(self):
        ecom_cursor.execute("SELECT * from user")

        result = ecom_cursor.fetchall()

        count = 1
        for user in result:
            print(f"{count}) {user[1]}")
            count += 1
        count = 0

        choice = int(input("Which Users Cart you wonted to view: "))
        selected_user = result[choice - 1]
        user_id = selected_user[0]

        bills = Bills()
        bills.view_bills(user_id)     

        self.main()   

