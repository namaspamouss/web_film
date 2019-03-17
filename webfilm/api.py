import requests

def get_movie(query):
    query = str(query)
    api_key = 'f074b2c32b0b7f0e035b4700ff2364f5'
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}"
    params = {'query': query}
    r = requests.get(url, params=params)
    movies = r.json()
    return movies['results']
    """
    #sauvegarde dans la base de données
    for movie in movies['results']:
        if (query.capitalize() in movie['title']) and (movie['poster_path'] is not None):
            new_movie=Films(titre=movie['title'], affiche="https://image.tmdb.org/t/p/w500"+movie['poster_path'], annee=movie["release_date"][:4])
            new_movie.save()
    """