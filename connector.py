import mysql.connector

conn=mysql.connector.connect(host="localhost",username="root",password="Debashish2001",database="face_recognition")
my_cursor=conn.cursor()

conn.commit()
conn.close()
print("connection sucessfully created!")