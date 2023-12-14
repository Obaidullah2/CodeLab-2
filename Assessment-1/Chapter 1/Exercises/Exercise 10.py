#Exercise 10 : Film Dictionary
#Create a dictionary that contains relevant data for films (e.g. Title, Director, etc). Display the film details using loop

# Film data dictionary
film_data = [
    {
        "Title": "Inception",
        "Director": "Christopher Nolan",
        "Year": 2010,
        "Genre": "Sci-Fi",
        "Rating": 8.8
    },
    {
        "Title": "The Shawshank Redemption",
        "Director": "Frank Darabont",
        "Year": 1994,
        "Genre": "Drama",
        "Rating": 9.3
    },
    {
        "Title": "Pulp Fiction",
        "Director": "Quentin Tarantino",
        "Year": 1994,
        "Genre": "Crime",
        "Rating": 8.9
    },
    {
        "Title": "The Dark Knight",
        "Director": "Christopher Nolan",
        "Year": 2008,
        "Genre": "Action",
        "Rating": 9.0
    }
]

# Display film details using a loop
for film in film_data:
    print("\nFilm Details:")
    for key, value in film.items():
        print(f"{key}: {value}")
#The End