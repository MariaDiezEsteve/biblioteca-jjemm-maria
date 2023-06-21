#THAT IS THE FILE database.py WHICH CONNECT WITH THE DATABASE

#1. We need is a connector: mysql-conector
import mysql.connector

#2. Set up to connect with database
#create a variable to connect with mysql
database = mysql.connector.connect(
    host = "containers-us-west-59.railway.app",
    user = "root",
    password = "mzj8vF2N8BRe4h8m8cyB",
    database = "railway"
)
