import mysql.connector
import os
from mysql.connector import Error


class ConnectionWrapper:


    def __init__(self):
        self.con=mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")

        )


    def select(self, sql, param=None):
        try:
            with self.con.cursor() as cur:
                if param is not None:
                    cur.execute(sql, param)
                else:
                    cur.execute(sql)
                myresult = cur.fetchall()
                return myresult
        except Error as e:
            print(f"DB execute error: {e}")