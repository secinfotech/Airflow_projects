import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="hit-db-demo")
            self.mycursor = self.conn.cursor()
        except:
            print("Connection Error")
            sys.exit(0)
        else:
            print("Connected to Database")
    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
            INSERT into `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(name, email, password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
        