import _sqlite3

class favorites:
    def create_table():
        connector = _sqlite3.connect("Database/favorites.db")
        c = connector.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS favorites (
         Username text,
         Title text,
         Year text,
         Rated text,
         Released text,
         Runtime text,
         Genre text,
         Director text,
         Writer text,
         Actors text,
         Plot text,
         Language text,
         Country text,
         Awards text,
         Poster text,
         Metascore text,
         imdbRating text,
         imdbVotes text,
         imdbID text,
         Type text,
         DVD text,
         BoxOffice text,
         Production text,
         Website text,
         Response text
        )""")
        connector.commit()
        connector.close()

    def add_favorite(username, dict):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute(
          "INSERT INTO favorites VALUES ('" + username + "', '" + dict["Title"] + "', '" + dict["Year"] + "', '" + dict[
             "Rated"] + "', '" + dict["Released"] + "', '" + dict["Runtime"] + "', '" + dict["Genre"] + "', '" + dict[
             "Director"] + "', '" + dict["Writer"] + "', '" + dict["Actors"] + "', '" + dict["Plot"] + "', '" + dict[
             "Language"] + "', '" + dict["Country"] + "', '" + dict["Awards"] + "', '" + dict["Poster"] + "', '" + dict[
             "Metascore"] + "', '" + dict["imdbRating"] + "', '" + dict["imdbVotes"] + "', '" + dict[
             "imdbID"] + "', '" + dict["Type"] + "', '" + dict["DVD"] + "', '" + dict["BoxOffice"] + "', '" + dict[
             "Production"] + "', '" + dict["Website"] + "', '" + dict["Response"] + "')")
       connector.commit()
       connector.close()

    def delete_all_entries(username):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("DELETE FROM favorites WHERE username = '" + username + "'")
       connector.commit()
       connector.close()

    def get_all_entries():
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT * FROM favorites")
       arr = c.fetchall()
       print(str(arr))
       connector.commit()
       connector.close()

    def get_from_user(username, attr):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT ? FROM favorites WHERE Username LIKE ?", (attr, username,))
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2

    def get_genre_from_user(username):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Genre FROM favorites WHERE Username LIKE ?", (username,))
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2

    def get_genre_from_movie(title):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Genre FROM favorites WHERE Title LIKE ?", (title,))
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2
       
    def get_director_from_user(username):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Director FROM favorites WHERE Username LIKE ?", (username,))
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2

    def get_director_from_movie(title):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Director FROM favorites WHERE Title LIKE '" + title + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2

    def get_actors_from_movie(title):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Actors FROM favorites WHERE Title LIKE '" + title + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2
       
    def get_title_from_user(username):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Title FROM favorites WHERE Username LIKE '" + username + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2

    def get_writer_from_movie(title):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Writer FROM favorites WHERE Title LIKE '" + title + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2

    def get_language_from_user(username):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Language FROM favorites WHERE Username LIKE '" + username + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2

    def get_language_from_movie(title):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Language FROM favorites WHERE Title LIKE '" + title + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2

    def get_country_from_user(username):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Country FROM favorites WHERE Username LIKE '" + username + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2

    def get_country_from_movie(title):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Country FROM favorites WHERE Title LIKE '" + title + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2

    def get_awards(title):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Awards FROM favorites WHERE Title LIKE '" + title + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(str(arr))
       connector.commit()
       connector.close()
       return arr2

    def get_view_count(title):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT COUNT(Username) FROM favorites WHERE title LIKE '" + title + "'")
       arr = c.fetchone()[0]
       print(arr)
       connector.commit()
       connector.close()
       return arr

    def get_boxoffice(title):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT BoxOffice FROM favorites WHERE title LIKE '" + title + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(arr)
       connector.commit()
       connector.close()
       return arr2

    def get_production(title):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Production FROM favorites WHERE title LIKE '" + title + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(arr)
       connector.commit()
       connector.close()
       return arr2

    def get_plot(title):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Plot FROM favorites WHERE title LIKE '" + title + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(arr)
       connector.commit()
       connector.close()
       return arr2

    def get_title_from_genre(genre):
       connector = _sqlite3.connect("Database/favorites.db")
       c = connector.cursor()
       c.execute("SELECT Title FROM favorites WHERE genre LIKE '" + '%' +  genre + '%' + "'")
       arr = c.fetchall()
       arr2 = [row[0] for row in arr]
       print(arr)
       connector.commit()
       connector.close()
       return arr2
      


thisdict1 = {
   "Title": "Scream",
   "Year": "1996",
   "Rated": "R",
   "Released": "20 Dec 1996",
   "Runtime": "111 min",
   "Genre": "Horror, Mystery",
   "Director": "Wes Craven",
   "Writer": "Kevin Williamson",
   "Actors": "Neve Campbell, Courteney Cox, David Arquette",
   "Plot": "A year after the murder of her mother, a teenage girl is terrorized by a new killer, who targets the girl and her friends by using horror films as part of a deadly game.",
   "Language": "English",
   "Country": "United States",
   "Awards": "11 wins & 11 nominations",
   "Poster": "https://m.media-amazon.com/images/M/MV5BMjA2NjU5MTg5OF5BMl5BanBnXkFtZTgwOTkyMzQxMDE@._V1_SX300.jpg",
   "Ratings": [{"Source": "Internet Movie Database", "Value": "7.3/10"}, {"Source": "Rotten Tomatoes", "Value": "79%"}, {"Source": "Metacritic", "Value": "65/100"}],
   "Metascore": "65",
   "imdbRating": "7.3",
   "imdbVotes": "299,164",
   "imdbID": "tt0117571",
   "Type": "movie",
   "DVD": "08 Dec 1998",
   "BoxOffice": "$103,046,663",
   "Production": "Dimension Films, Woods Entertainment",
   "Website": "N/A",
   "Response": "True"
}

thisdict2 = {
   "Title": "Avengers: Endgame",
   "Year": "2019",
   "Rated": "PG-13",
   "Released": "26 Apr 2019",
   "Runtime": "181 min",
   "Genre": "Action, Adventure, Drama",
   "Director": "Anthony Russo, Joe Russo",
   "Writer": "Christopher Markus, Stephen McFeely, Stan Lee",
   "Actors": "Robert Downey Jr., Chris Evans, Mark Ruffalo",
   "Plot": "After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos actions and restore balance to the universe.",
   "Language": "English, Japanese, Xhosa, German",
   "Country": "United States",
   "Awards": "Nominated for 1 Oscar. 70 wins & 122 nominations total",
   "Poster": "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_SX300.jpg",
   "Ratings": [{"Source":"Internet Movie Database","Value":"8.4/10"},{"Source":"Rotten Tomatoes","Value":"94%"},{"Source":"Metacritic","Value":"78/100"}],
   "Metascore": "78",
   "imdbRating": "8.4",
   "imdbVotes": "937,294",
   "imdbID": "tt4154796",
   "Type": "movie",
   "DVD": "30 Jul 2019",
   "BoxOffice": "$858,373,000",
   "Production": "Walt Disney Pictures, Marvel Studios",
   "Website": "N/A",
   "Response": "True"
}
# fav = favorites.create_table()
# fav = favorites.add_favorite("Lewi", thisdict1)
# fav = favorites.get_all_entries()
# fav = favorites.add_favorite("DillonKooncey", thisdict2)
# fav = favorites.delete_all_entries("DillonKooncey")
# fav = favorites.get_all_entries()
# fav = favorites.get_genre('DillonKooncey')
# fav = favorites.get_actors('DillonKooncey')
# fav = favorites.get_director('DillonKooncey')

# test = favorites.get_genre_from_movie('Scream')
# test = favorites.get_genre_from_user('Lewi')

# clean strings method test
# fav = favorites.clean_String(thisdict2)