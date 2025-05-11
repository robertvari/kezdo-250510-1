import tmdbsimple as tmdb
import pprint, json, time, os
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'

# check if we have cached data and use that if exists
if os.path.exists("movie_data.json"):
    # open movie_data.json
    with open("movie_data.json") as file:
        movie_data = json.load(file)
        pprint.pprint(movie_data)


# connect to TMDB and cache data
else:    
    movies = tmdb.Movies()

    # empty dictionary that we can fill out in the for loop
    my_movie_db = {}

    for page in range(1, 10):
        print("-"*50, f"Current page: {page}", "-"*50)
        # get popular movies for current page
        popular_movies = movies.popular(page=page)
        
        # get movie list from the dictionary
        movie_list = popular_movies["results"]

        # nested for loop
        # step through the movie list on this page
        for movie in movie_list:
            # because movie is a dictionary we can get the title
            my_movie_db[movie["id"]] = {
                "title": movie["title"], 
                "release_date": movie["release_date"],
                "vote_average": movie["vote_average"],
                "overview": movie["overview"]
                }


    # cache my_movie_db into a file
    with open("movie_data.json", "w") as file:
        json.dump(my_movie_db, file)