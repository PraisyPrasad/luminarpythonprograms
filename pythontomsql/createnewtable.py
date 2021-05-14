import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="mydb",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
# sql="create table employee(eid int,ename varchar(25),desig varchar(30),salary int)"
# cursor.execute(sql)
# db.close()
# sql="insert into employee(eid,ename,desig,salary) values(100,'ajay','developer',25000)"
# try:
#     cursor.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e.args)
#     db.rollback()
# finally:
#     db.close()
sql="update employee set salary='26000' where eid=100"
cursor.execute(sql)
db.close()