from admin import Admin
from user import User
from conn import ecom_cursor

def login():
    username = input("Enter user name: ")
    password = input("Enter Password: ")

    sql = "SELECT * from user where username=%s and password=%s"
    val = (username, password)

    ecom_cursor.execute(sql, val)

    result = ecom_cursor.fetchall()

    if len(result) != 0:

        if result[0][4] == 1:
            admin = Admin(result[0])
            admin.main()
        else:
            user = User(result[0])
            user.main()

    else:
        print("Enter Valid Details.\n")
        login()

def main():

    print("................................. MyCart ....................................\n")

    login()
    

if __name__ == "__main__":
    main()

