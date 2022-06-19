from conn import ecom_cursor, ecom_db

class Cart:

    def view_cart(self, user_id):
        ecom_cursor.execute(f"SELECT * from cart where user_id={int(user_id)}")
        result = ecom_cursor.fetchall()

        total_price = 0

        print("\n\n--------------------Cart-------------------------\n")

        for cart_item in result:
            sql = f"SELECT categories.name AS category, products.name AS product FROM products INNER JOIN categories ON products.categories_id = categories.id where products.id={cart_item[1]};"
            ecom_cursor.execute(sql)
            new_result = ecom_cursor.fetchall()
            print("--------------")
            print(f"Product: {new_result[0][1]}")
            print(f"Category: {new_result[0][0]}")
            print(f"Price: {cart_item[4]}")
            print(f"Quantity: {cart_item[5]}")
            print(f"Total Price: {cart_item[6]}")
            total_price = total_price + int(cart_item[6])

            print("\n--------------\n")

        print(f"Total Bill: {total_price}")
        
        if total_price > 10000:
            final_price = total_price - 500
            print("Discounted Amount: 500") 
        else:
            final_price = total_price
        
        print(f"Final Price: {final_price}")

        print("-----------------------\n")


    def add_to_cart(self, product, category_id, user_id):
        product_id = product[0]
        price = product[4]
        quantity = 1
        total_price = price

        ecom_cursor.execute(f"SELECT * from cart where user_id={user_id} and product_id={product_id}")
        result = ecom_cursor.fetchall()
        
        if len(result) == 0:
            sql = "INSERT INTO cart (product_id, category_id, user_id, price, quantity, total_price) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (product_id, category_id, user_id, price, quantity, total_price)
            ecom_cursor.execute(sql, val)

            ecom_db.commit()

        else:
            result = result[0]
            quantity = int(result[5]) + 1
            total_price = int(quantity) * int(price)
            sql = "UPDATE cart SET quantity = %s, total_price = %s"
            val = (quantity, str(total_price))
            ecom_cursor.execute(sql, val)

            ecom_db.commit()

        print("\n------Product Added to Cart.----------\n")


    def remove_product(self, product_name, user_id):
        sql = f"SELECT name, id from products;"
        ecom_cursor.execute(sql)
        products = ecom_cursor.fetchall()

        products_dict = dict(products)

        if product_name in products_dict:
            product_id = products_dict[product_name]
            sql = "DELETE FROM cart WHERE user_id=%s and product_id=%s"
            val = (user_id, product_id)
            ecom_cursor.execute(sql, val)
            ecom_db.commit()

            print("Product Delete From Cart\n")

        else:
            print("Wrong Details Enterd...\n")

