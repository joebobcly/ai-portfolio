movies = [
     {
        "movie": "Goodfellas",
        "director": "Martin Scorsese",
        "year": 1990,
     },
     {
        "movie": "The Dark Knight",
        "director": "Christopher Nolan",
        "year": 2008,
     },
     {
        "movie": "The Odyssey",
        "director": "Christopher Nolan",
        "year": 2026,
     },
]

for movie in movies:
    print(f"{movie['movie']} was directed by {movie['director']} in {movie['year']}.")