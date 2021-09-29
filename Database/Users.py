import _sqlite3


class users:

    connector = _sqlite3.connect("users.db")
    c = connector.cursor()

    def create_table():
        connector = _sqlite3.connect("users.db")
        c = connector.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users (
            username text,
            password text
        )""")
        connector.commit()
        connector.close()

    def insert(username, password):
        connector = _sqlite3.connect("users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users WHERE username = '" + username + "'")
        if(c.fetchone()):
            print("User already exists")
            connector.close()
        else:
            c.execute("INSERT INTO users VALUES ('" + username + "', '" + password + "')")
            print("Username " + username + " added")
            connector.commit()
            connector.close()


    def find(username, password):
        connector = _sqlite3.connect("users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
        if(c.fetchone()):
            print("User found")
            connector.close()
        else:
            print("User not found")
            connector.close()

    def update_username(old_username, new_username):
        connector = _sqlite3.connect("users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users WHERE username = '" + new_username + "'")
        if(c.fetchone()):
            print("Username is already in use")
            connector.close()
        else:
            c.execute("UPDATE users SET username = '" + new_username + "' where username = '" + old_username + "'")
            print("Username was updated")
            connector.commit()
            connector.close()

    def update_password(username, new_password):
        connector = _sqlite3.connect("users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users WHERE username = '" + username + "'")
        if(c.fetchone()):
            c.execute("UPDATE users SET password = '" + new_password + "' where username = '" + username + "'")
            print("Password was updated")
            connector.commit()
            connector.close()
        else:
            print("User was not found")
            connector.close()

    def delete(username):
        connector = _sqlite3.connect("users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users WHERE username = '" + username + "'")
        if(c.fetchone()):
            c.execute("DELETE FROM users WHERE username = '" + username + "'")
            print("Delete was successful")
            connector.commit()
            connector.close()
        else:
            print("User was not found")
            connector.close()

    def get_all():
        connector = _sqlite3.connect("users.db")
        c = connector.cursor()
        c.execute("SELECT * FROM users")
        print(c.fetchall())
        connector.close()

    # create_table()
    # user = insert("Lewi", "12345678")
    # user = insert("Test", "12345678")
    # user = find("Lewi", "12345678")
    # user = find("Asdf", "12345678")
    delete("Test")
    user = get_all()

# A series of test I ran just to make sure everything worked. Does not include everything i did.
# create_table()
# user = Users.insert("DillonKooncey", "November21998")
# user = Users.find("DillonKooncey", "November21998")
# user = Users.find("Austinkooncey", "November21998")
# user = Users.update_username("DillonKooncey", "Dillonkooncey")
# users = Users.update_username("Dillonkooncey", "DillonKooncey")
# user = Users.update_password("DillonKooncey", "November21998")
# update_password("Austinkooncey", "Blah")
# delete("DillonKooncey")
# user = Users.get_all()


