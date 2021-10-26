import _sqlite3

class history:

    def create_table():
        connector = _sqlite3.connect("Database/history.db")
        c = connector.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS history (
            Username text,
            Title text)""")
        connector.commit()
        connector.close()

    def insert(username, title):
        connector = _sqlite3.connect("Database/history.db")
        c = connector.cursor()
        c.execute("INSERT INTO history VALUES ('" + username + "', '" + title + "')")
        connector.commit()
        connector.close()

    def delete(username, title):
        connector = _sqlite3.connect("Database/history.db")
        c = connector.cursor()
        c.execute("DELETE FROM history WHERE (username = '" + username + "' AND title = '" + title + "')")
        print("Delete was successful")
        connector.commit()
        connector.close()

    def get_all():
        connector = _sqlite3.connect("Database/history.db")
        c = connector.cursor()
        c.execute("SELECT * FROM history")
        print(c.fetchall())
        connector.close()

    # Some tests
    # create_table()
    # history = insert("Lewi", "Movie1")
    # history = insert("Lewi", "Movie2")
    # history = delete("Lewi", "Movie1")
    # history = get_all()