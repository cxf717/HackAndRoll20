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
        print("========== users =========")
        for user in results:
            print("user_id", user[0])
            print("username", user[1])
            print("role", user[2])
            print("status", user[3])
        print("=========== end ==========")

    def get_usernames(self):
        stmt = "SELECT username FROM users"
        results = self.conn.execute(stmt)
        
        usernames_list = "Players List:"
        index = 1



        print("========== names =========")
        for user in results:
            #print(user[0])
            line = "\n" + str(index) + ". " + user[0]
            usernames_list += line
            index += 1
        print(usernames_list)
        print("=========== end ==========")
        return usernames_list

    def check_user(self, user_id):
        stmt = "SELECT EXISTS (SELECT 1 FROM users WHERE user_id = (?))"
        args = (user_id, )
        result = self.conn.execute(stmt, args).fetchone()[0]
        self.conn.commit()
        return result

    def delete_all_users(self):
        stmt = "DELETE FROM users"
        self.conn.execute(stmt)
        self.conn.commit()