import _sqlite3

class favorites:
    def create_table():
        connector = _sqlite3.connect("favorites.db")
        c = connector.cursor()
        c.execute("""CREATE TABLE favorites (
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

    def add_favorite(username, dict):
        connector = _sqlite3.connect("favorites.db")
        c = connector.cursor()
        c.execute(
            "INSERT INTO favorites VALUES ('" + username + "', '" + dict["Title"] + "', '" + dict["Year"] + "', '" +
            dict[
                "Rated"] + "', '" + dict["Released"] + "', '" + dict["Runtime"] + "', '" + dict["Genre"] + "', '" +
            dict[
                "Director"] + "', '" + dict["Writer"] + "', '" + dict["Actors"] + "', '" + dict["Plot"] + "', '" + dict[
                "Language"] + "', '" + dict["Country"] + "', '" + dict["Awards"] + "', '" + dict["Poster"] + "', '" +
            dict[
                "Metascore"] + "', '" + dict["imdbRating"] + "', '" + dict["imdbVotes"] + "', '" + dict[
                "imdbID"] + "', '" + dict["Type"] + "', '" + dict["DVD"] + "', '" + dict["BoxOffice"] + "', '" + dict[
                "Production"] + "', '" + dict["Website"] + "', '" + dict["Response"] + "')")
        connector.commit()
        connector.close()
        return True

    def delete_all_entries(username):
        connector = _sqlite3.connect("favorites.db")
        c = connector.cursor()
        c.execute("DELETE FROM favorites WHERE username = '" + username + "'")
        connector.commit()
        connector.close()
        return True

    def get_all_entries():
        connector = _sqlite3.connect("favorites.db")
        c = connector.cursor()
        c.execute("SELECT * FROM favorites")
        print(str(c.fetchall()))
        connector.commit()
        connector.close()

    # def get_all_users_entries(username):



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
    "Ratings": [{"Source": "Internet Movie Database", "Value": "7.3/10"}, {"Source": "Rotten Tomatoes", "Value": "79%"},
                {"Source": "Metacritic", "Value": "65/100"}],
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
    "Plot": "After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
    "Language": "English, Japanese, Xhosa, German",
    "Country": "United States",
    "Awards": "Nominated for 1 Oscar. 70 wins & 122 nominations total",
    "Poster": "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_SX300.jpg",
    "Ratings": [{"Source": "Internet Movie Database", "Value": "8.4/10"}, {"Source": "Rotten Tomatoes", "Value": "94%"},
                {"Source": "Metacritic", "Value": "78/100"}],
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
# fav = favorites.add_favorite("DillonKooncey", thisdict1)
# fav = favorites.get_all_entries()
# fav2 = favorites.add_favorite("DillonKooncey", thisdict2)
# fav = favorites.delete_all_entries("DillonKooncey")
# fav2 = favorites.get_all_entries()
