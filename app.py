from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


API_KEY = '7a12e2d96fbe8abfcef5581fc05cec97'
BASE_URL = 'https://api.themoviedb.org/3'

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/api/movies/<genre>')
def get_movies(genre):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={get_genre_id(genre)}"
    response = requests.get(url)
    data = response.json()
    movies = [movie['title'] for movie in data['results']]
    return jsonify(movies)

@app.route('/api/tvshows/<genre>')
def get_tvshows(genre):
    url = f"{BASE_URL}/discover/tv?api_key={API_KEY}&with_genres={get_genre_id(genre)}"
    response = requests.get(url)
    data = response.json()
    tvshows = [show['name'] for show in data['results']]
    return jsonify(tvshows)

def get_genre_id(genre):
    genre_mapping = {
        'horror': 27,
        'action': 28,
        'comedy': 35,
        'drama': 18,
        'biopic': 99  # There is no exact genre for biopics, so we used the 'Documentary' genre as an approximation
    }
    return genre_mapping.get(genre.lower(), None)

if __name__ == '__main__':
    app.run(debug=True)
