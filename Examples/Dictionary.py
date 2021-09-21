def get_info(dictionary):
    print("Title = " + dictionary["Title"] + "\n")
    print("Year = " + dictionary["Year"] + "\n")
    print("Rated = " + dictionary["Rated"] + "\n")
    print("Released = " + dictionary["Released"] + "\n")
    print("Runtime = " + dictionary["Runtime"] + "\n")
    print("Genre = " + dictionary["Genre"] + "\n")
    print("Director = " + dictionary["Director"] + "\n")
    print("Writer = " + dictionary["Writer"] + "\n")
    print("Actors = " + dictionary["Actors"] + "\n")
    print("Plot = " + dictionary["Plot"] + "\n")
    print("Language = " + dictionary["Language"] + "\n")
    print("Country = " + dictionary["Country"] + "\n")
    print("Awards = " + dictionary["Awards"] + "\n")
    print("Poster = " + dictionary["Poster"] + "\n")
    print("Ratings = " + str(dictionary["Ratings"]) + "\n")
    print("Metascore = " + dictionary["Metascore"] + "\n")
    print("imdbRating = " + dictionary["imdbRating"] + "\n")
    print("imdbVotes = " + dictionary["imdbVotes"] + "\n")
    print("imdbID = " + dictionary["imdbID"] + "\n")
    print("Type = " + dictionary["Type"] + "\n")
    print("DVD = " + dictionary["DVD"] + "\n")
    print("BoxOffice = " + dictionary["BoxOffice"] + "\n")
    print("Production = " + dictionary["Production"] + "\n")
    print("Website = " + dictionary["Website"] + "\n")
    print("Response = " + dictionary["Response"] + "\n")


thisdict = {
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

get_info(thisdict)
