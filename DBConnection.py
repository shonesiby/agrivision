import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


class Db:
    def __init__(self):
        # Local database connection loaded from environment/.env:
        self.cnx = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            charset="utf8",
            database=DB_NAME,
        )
        self.cur = self.cnx.cursor(dictionary=True)


    def select(self, q, val=None):
        if val:
            self.cur.execute(q, val)
        else:
            self.cur.execute(q)
        return self.cur.fetchall()

    def selectOne(self, q):
        self.cur.execute(q)
        return self.cur.fetchone()


    def insert(self, q, val=None):
        if val:
            self.cur.execute(q, val)
        else:
            self.cur.execute(q)
        self.cnx.commit()
        return self.cur.lastrowid

    def update(self, q, val=None):
        if val:
            self.cur.execute(q, val)
        else:
            self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount

    def delete(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount