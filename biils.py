import uuid

from conn import ecom_cursor, ecom_db

class Bills:
    def __init__(self):
        self.is_viewed = False
        self.is_bill_genrated = False

    def view_bills(self, user_id):

        sql = f"SELECT id, name from categories;"
        ecom_cursor.execute(sql)
        categories = ecom_cursor.fetchall()
        categories_dict = dict(categories)

        sql = f"SELECT id, name, price from products;"
        ecom_cursor.execute(sql)
        products = ecom_cursor.fetchall()

        products_dict = {}
        for k, *rest in products:
            products_dict.setdefault(k, []).extend(rest)

        self.is_viewed = True
        print(f"self.is_viewed: {self.is_viewed}")
        
        ecom_cursor.execute(f"SELECT DISTINCT transaction_id from bills where user_id={user_id}")
        transactions_ids = ecom_cursor.fetchall()
        print("\n------------Bills-------------\n")

        for transaction_id in transactions_ids:
            sql = "SELECT * from bills where transaction_id=%s"
            val = (str(transaction_id[0]), )
            ecom_cursor.execute(sql, val)
            bills_data = ecom_cursor.fetchall() 

            total_price = 0

            print("\n------------------------------------------------------------------------\n")
            for bill in bills_data:
                print(f"Product: {products_dict[bill[1]][0]}")
                print(f"Category: {categories_dict[bill[2]]}")
                print(f"Price: {bill[4]}")
                print(f"Quantity: {bill[5]}")
                print(f"Total Price: {bill[6]}")
                total_price = total_price + int(bill[6])
                print("\n----------\n")

            print(f"Total Bill: {total_price}")
            if total_price > 10000:
                final_price = total_price - 500
                print("Discounted Amount: 500") 
            else:
                final_price = total_price
            print(f"Final Price: {final_price}")
            print(f"Transaction id: {transaction_id}")

            
            print("\n-------------------------------------------------------------------------------\n")
            
    def genarate_bill(self, user_id):
        ecom_cursor.execute(f"SELECT * from cart where user_id={user_id}")
        result = ecom_cursor.fetchall()

        sql = "DELETE FROM cart WHERE user_id=%s"
        val = (user_id, )
        ecom_cursor.execute(sql, val)
        ecom_db.commit()

        total_price = 0

        print("\n-----------Bill------------\n")

        transaction_id = uuid.uuid4()
        transaction_id = transaction_id.hex

        for cart_item in result:
            product_id = cart_item[1]
            category_id = cart_item[2]
            price = int(cart_item[4])
            quantity = int(cart_item[5])
            total_price = total_price + int(cart_item[6])
            
            sql = "INSERT INTO bills (product_id, category_id, user_id, price, quantity, total_price, transaction_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (product_id, category_id, user_id, price, quantity, cart_item[6], str(transaction_id))
            ecom_cursor.execute(sql, val)
            ecom_db.commit()

            self.is_bill_genrated = True

        print(f"\nYour transaction is successfuly comleted..")
        print(f"Order Bill: {total_price}")
        print(f"Transaction id: {transaction_id}")
        print("\n--------------------\n")
