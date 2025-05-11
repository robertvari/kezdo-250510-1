import tmdbsimple as tmdb
import pprint
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'

movies = tmdb.Movies()

for page in range(1, 11):
    print("-"*50, f"Current page: {page}", "-"*50)
    # get popular movies for current page
    popular_movies = movies.popular(page=page)
    
    # get movie list from the dictionary
    movie_list = popular_movies["results"]

    # step through the movie list
    for movie in movie_list:
        # because movie is a dictionary we can get the title
        print(movie["title"])