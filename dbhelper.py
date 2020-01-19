import sqlite3
from sqlite3 import Error

class DBHelper:

    def __init__(self, dbname="users.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    # create table of all the relevant info on users
    def setup(self, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        tblstmt = "CREATE TABLE IF NOT EXISTS " + table_name + " (user_id text NOT NULL, username text NOT NULL, role text, status int NOT NULL, votes int NOT NULL)"
        self.conn.execute(tblstmt)
        self.conn.commit()

    def add_user(self, user_id, username, role, status, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "INSERT INTO  " + table_name + " (user_id, username, role, status, votes) VALUES (?,?,?,?,0)"
        args = (user_id, username, role, status, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def update_user(self, user_id, username, role, status, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "UPDATE " + table_name + " SET username = ?, role = ?, status = ? WHERE user_id = ?"
        args = (username, role, status, user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def set_role(self, user_id, role, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "UPDATE " + table_name + " SET role = ? WHERE user_id = ?"
        args = (role, user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()        

    def delete_user(self, user_id, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "DELETE FROM " + table_name + " WHERE id = (?)"
        args = (user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_users(self, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "SELECT * FROM " + table_name
        user_list = self.conn.execute(stmt)
        self.conn.commit()
        print("========== " + table_name + " =========")
        for user in user_list:
            print("user_id:", user[0])
            print("username:", user[1])
            print("role:", user[2])
            print("status:", user[3])
        print("=============== end ==============")
        return user_list

    def get_user_info(self, user_id, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "SELECT * FROM " + table_name + " WHERE user_id = (?)"
        args = (user_id, )
        results = self.conn.execute(stmt, args)
        self.conn.commit()

        for user_info in results:
            return user_info

    def get_user_count(self, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "SELECT COUNT(*) FROM " + table_name
        count = self.conn.execute(stmt).fetchone()[0]
        self.conn.commit()
        return count

    # returns a string of the list of users' first_names
    def get_usernames_list(self, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "SELECT username FROM " + table_name
        results = self.conn.execute(stmt)
        self.conn.commit()
        
        usernames_list = ""
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

    def get_userid_arr(self, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "SELECT user_id FROM " + table_name
        results = self.conn.execute(stmt)
        self.conn.commit()
        
        userid_arr = []
        for user in results:
            userid_arr.append(user[0])
        
        for id in userid_arr:
            print(id)
        return userid_arr

    # check if user exists in database already
    # returns true if they exist and false if they don't
    def check_user(self, user_id, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "SELECT EXISTS (SELECT 1 FROM " + table_name + " WHERE user_id = (?))"
        args = (user_id, )
        result = self.conn.execute(stmt, args).fetchone()[0]
        self.conn.commit()
        if result == 0:
            return False
        else:
            return True

    # check if any user already has a particular role
    # returns true if they exist and false if they don't
    def check_role(self, role, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "SELECT EXISTS (SELECT 1 FROM " + table_name + " WHERE role = (?))"
        args = (role, )
        result = self.conn.execute(stmt, args).fetchone()[0]
        self.conn.commit()
        if result == 0:
            return False
        else:
            return True

    def delete_all_users(self, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "DELETE FROM " + table_name
        self.conn.execute(stmt)
        self.conn.commit()

    ############### functions for voting ################

    # returns an array of all the first names except a player's own
    def get_vote_arr(self, user_id, chat_id):
        table_name = "users_" + str(chat_id)[1:]
        stmt = "SELECT * FROM " + table_name
        results = self.conn.execute(stmt)
        self.conn.commit()

        vote_arr = []
        for user in results:
            if user[0] != user_id and user[3] == 0:
                vote_arr.append(user[1])
        print("vote arr:", vote_arr)
        return vote_arr