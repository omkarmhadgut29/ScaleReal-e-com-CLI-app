import mysql.connector

host="localhost"
user="root"
password="OmkarMysql@123"

# ----------------------------------------------------

ecom_db = mysql.connector.connect(
  host=host,
  user=user,
  password=password,
  database="ecom"
)

ecom_cursor = ecom_db.cursor()

