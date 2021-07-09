
import mysql.connector
#This is a SQL query commands file used to connect and manage database in your system or server
#This uses mysql.connector to connect the database in your system or server
# and perform SQL Query Commands 


mydb = mysql.connector.connect(
    host = 'your localhost', user = 'your user', password = 'your password', database = "your database name")

mycur = mydb.cursor()

#-------Create & Show Databases
#to execute below query remove the database name passed in above connect() as the database doesnt exist.

#mycur.execute("CREATE DATABASE contact")
# mycur.execute("SHOW DATABASES")
# for db in mycur:
#     print(db)




#-------Create & Show Table

# mycur.execute(
#     "CREATE TABLE users (user_id INTEGER AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), subject VARCHAR(310), message varchar(510))")
# mycur.execute("SHOW TABLES")
# for table in mycur:
#     print(table)

#-------Delete data from table
# mycur.execute("DELETE FROM users WHERE user_id = 1")
# mydb.commit()

#Do not forget the close connection and cursor

mycur.close()
mydb.close()
