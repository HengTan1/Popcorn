import _sqlite3


class users:
    def create_table():
        connector = _sqlite3.connect("Database/users.db")
        c = connector.cursor()
        c.execute("""CREATE TABLE users (
            username text,
            password text
        )""")
        connector.commit()
        connector.close()

    def insert(username, password):
        connector = _sqlite3.connect("Database/users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users WHERE username = '" + username + "'")
        if(c.fetchone()):
            print("User already exists")
            connector.close()
            return False
        else:
            c.execute("INSERT INTO users VALUES ('" + username + "', '" + password + "')")
            print("Username " + username + " added")
            connector.commit()
            connector.close()
            return True


    def find(username, password):
        connector = _sqlite3.connect("Database/users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
        if(c.fetchone()):
            print("User found")
            connector.close()
            return True
        else:
            print("User not found")
            connector.close()
            return False

    def update_username(old_username, new_username):
        connector = _sqlite3.connect("Database/users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users WHERE username = '" + new_username + "'")
        if(c.fetchone()):
            print("Username is already in use")
            connector.close()
            return False
        else:
            c.execute("UPDATE users SET username = '" + new_username + "' where username = '" + old_username + "'")
            print("Username was updated")
            connector.commit()
            connector.close()
            return True

    def update_password(username, new_password):
        connector = _sqlite3.connect("Database/users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users WHERE username = '" + username + "'")
        if(c.fetchone()):
            c.execute("UPDATE users SET password = '" + new_password + "' where username = '" + username + "'")
            print("Password was updated")
            connector.commit()
            connector.close()
            return True
        else:
            print("User was not found")
            connector.close()
            return False

    def delete(username):
        connector = _sqlite3.connect("Database/users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users WHERE username = '" + username + "'")
        if(c.fetchone()):
            c.execute("DELETE FROM users WHERE username = '" + username + "'")
            print("Delete was successful")
            connector.commit()
            connector.close()
            return True
        else:
            print("User was not found")
            connector.close()
            return False

    def get_all():
        connector = _sqlite3.connect("Database/users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users")
        listofUsers = {}
        print(str(c.fetchall()))

# A series of test I ran just to make sure everything worked. Does not include everything i did.
# user = users.create_table()

# user = users.insert("Lewi", "asdfasdf")
# user = users.find("DillonKooncey", "November21998")
# user = users.find("Austinkooncey", "November21998")
# user = users.update_username("DillonKooncey", "Dillonkooncey")
# users = users.update_username("Dillonkooncey", "DillonKooncey")
# user = users.update_password("DillonKooncey", "November21998")
# update_password("Austinkooncey", "Blah")
# delete("DillonKooncey")
# user = users.get_all()

