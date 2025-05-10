import tmdbsimple as tmdb
import pprint
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'

movies = tmdb.Movies()
pprint.pprint(movies.popular())