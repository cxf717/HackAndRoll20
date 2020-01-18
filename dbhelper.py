import sqlite3
from sqlite3 import Error

class DBHelper:
    def __init__(self, dbname="users.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    # create table of all the relevant info on users
    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS users (user_id text NOT NULL, username text NOT NULL, role text, status int NOT NULL)"
        self.conn.execute(tblstmt)
        self.conn.commit()

    def add_user(self, user_id, username, role, status):
        stmt = "INSERT INTO users (user_id, username, role, status) VALUES (?,?,?,?)"
        args = (user_id, username, role, status, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def update_user(self, user_id, username, role, status):
        stmt = "UPDATE users SET user_id = ?, username = ?, role = ?, status = ? WHERE id = ?"
        args = (user_id, username, role, status, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_user(self, user_id):
        stmt = "DELETE FROM users WHERE id = (?)"
        args = (user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_users(self):
        stmt = "SELECT * FROM users"
        results = self.conn.execute(stmt)
        return [results]

    def delete_all_users(self):
        stmt = "DROP TABLE users"
        self.conn.execute(stmt)
        self.conn.commit()