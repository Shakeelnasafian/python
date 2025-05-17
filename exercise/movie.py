movies = { 'The Shawshank Redemption': 1994,
          'The Godfather': 1972,
          'The Dark Knight': 2008,
          'Pulp Fiction': 1994,
          'Forrest Gump': 1994,
          'Inception': 2010,
          'The Matrix': 1999,
          'Fight Club': 1999,
          'The Lord of the Rings: The Return of the King': 2003
        }
print("Enter the movie name to see release year:")

for key in movies:
    print(key)

selection = input("Enter the movie name? \n")
if selection in movies:
    print(f"{selection} was released in {movies[selection]}")
else:
    print("Movie not found in the list.")