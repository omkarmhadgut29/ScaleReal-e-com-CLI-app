from conn import ecom_cursor, ecom_db

class Categories:
    def __init__(self):
        self.categories = ""

    def list_of_categories(self):
        ecom_cursor.execute("SELECT * from categories")

        result = ecom_cursor.fetchall()
        self.categories = result


    def add_categories(self):

        category_name = input("Enter Category Name: ")

        sql = "INSERT INTO categories (name) VALUE (%s);"
        val = (category_name, )
        ecom_cursor.execute(sql, val)
        ecom_db.commit()

        print("Category added successfuly.")

