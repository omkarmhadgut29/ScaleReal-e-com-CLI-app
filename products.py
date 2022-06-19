from conn import ecom_cursor, ecom_db

class Product:
    def __init__(self):
        self.products = ""
        
        

    def list_of_products(self):

        ecom_cursor.execute("SELECT * from products")

        result = ecom_cursor.fetchall()
        self.products = result

    def add_products(self, category_id):

        product_name = input("Enter Product Name: ")
        description = input("Enter description: ")
        price = input("Enter Price: ")

        sql = "INSERT INTO products (name, categories_id, description, price) VALUE (%s, %s, %s, %s);"
        val = (product_name, int(category_id), description, price)
        ecom_cursor.execute(sql, val)
        ecom_db.commit()

        print("Product added successfuly.")
        
