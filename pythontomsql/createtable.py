import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="mydb",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
f=open("employee")
for lines in f:
    data=lines.rstrip("\n").strip(",")
    sql="insert into employee(eid,ename,desig,salary)values(%s,%s,%s,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()
db.close()
