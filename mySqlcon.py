import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.cwfontt3bgap.us-east-1.rds.amazonaws.com",
  user="admin",
  password="shrey2502"
)

print(mydb)