from omdb import OMDBClient

client = OMDBClient(apikey='8dc708b0')
movie_name = input("Enter movie name: ")

# Enter this movie names
# Guardians of the Galaxy Vol. 2
# wonder girl
# robo

movie_data = client.search_movie(movie_name)
try:
    if movie_data:
        request = {'title': movie_name,
               'fullplot': True,
               'tomatoes': True}
        data = client.get(**request)
        if data['ratings']:
            print('Movie Title:', data['title'])
            if data['ratings'][1]['source']:
                print('Rotten Tomatoes:', data['ratings'][1]['source'])
                print('Value:',data['ratings'][1]['value'])
            else:
                print('There is No Rotten Tomatoes data for this movie')
        else:
            print('Movie Title:', data['title'])
            print('There is No Rotten Tomatoes data for this movie')
    else:
        print('Movie name not found')
except IndexError :
    print('There is No Rotten Tomatoes data for this movie')

