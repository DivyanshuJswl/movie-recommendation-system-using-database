import random
import requests
import pickle
import pandas as pd
import streamlit as st

from dotenv import load_dotenv
import os
load_dotenv()  # Load the .env file

api_key = os.getenv('API_KEY')

st.set_page_config(layout="wide",
    page_title="Movie-Thruster",
    page_icon="🎬"
)

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    params = {"api_key": api_key}
    response = requests.get(url, params=params,verify=False)
    
    data = response.json()
    poster_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    overview = data['overview']
    rating = data['vote_average']
    release_date = data['release_date']
    genres = [genre['name'] for genre in data['genres']]
    return poster_path, overview, rating, release_date, genres


def recommend(movie, num_recommendations, genre_filter=None, randomize=False, rating_filter=None):
    if randomize:
        random_movies_list = random.sample(range(len(movies)), num_recommendations)
    else:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:num_recommendations + 1]
        random_movies_list = [x[0] for x in movies_list]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_overviews = []
    recommended_movies_ratings = []
    recommended_movies_genres = []

    for idx in random_movies_list:
        movie_id = movies.iloc[idx].movie_id
        poster, overview, rating, release_date, genres = fetch_movie_details(movie_id)

        # Apply genre filter if specified
        if genre_filter and genre_filter not in genres:
            continue

        # Apply rating filter if specified
        if rating_filter and rating < rating_filter:
            continue

        recommended_movies.append(movies.iloc[idx].title)
        recommended_movies_posters.append(poster)
        recommended_movies_overviews.append(overview)
        recommended_movies_ratings.append(rating)
        recommended_movies_genres.append(genres)

    return recommended_movies, recommended_movies_posters, recommended_movies_overviews, recommended_movies_ratings, recommended_movies_genres


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Advanced Movie Recommender System')

# Searchable input for selecting a movie
selected_movie_name = st.selectbox(
    'Select a movie:', 
    movies['title'].values
)

# Using slider for the number of recommendations
num_recommendations = st.slider('Number of recommendations', min_value=0, max_value=25)

# Checkbox for random recommendations
randomize = st.checkbox('Recommend Random Movies')

# Optional genre filter
available_genres = ['Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Thriller']
genre_filter = st.selectbox('Filter by Genre (optional):', ['None'] + available_genres)
genre_filter = None if genre_filter == 'None' else genre_filter

# Optional rating filter
rating_filter = st.slider('Minimum Rating (optional):', min_value=0.0, max_value=10.0, value=0.0, step=1.0)

if st.button('Recommend'):
    names, posters, overviews, ratings, genres = recommend(
        selected_movie_name, 
        num_recommendations, 
        genre_filter=genre_filter, 
        randomize=randomize, 
        rating_filter=rating_filter
    )

    # Dynamically create columns and display recommended movies
    num_cols_per_row = 6
    for i in range(0, len(names), num_cols_per_row):
        cols = st.columns(min(num_cols_per_row, len(names) - i))
        for idx, col in enumerate(cols):
            with col:
                # st.text(f"{names[i + idx]}")
                st.markdown(f"<h6 style='font-weight: bold;'>{names[i + idx]}</h6>", unsafe_allow_html=True)
                st.text(f"Rating: {ratings[i + idx]}/10")
                st.image(posters[i + idx])
                st.caption(f"Genres: {', '.join(genres[i + idx])}")
                # st.write(overviews[i + idx])
                limited_overview = overviews[i + idx][:100]  # limit overview to 100 characters
                st.write(f"Overview:\n {limited_overview}")
        st.markdown("<br>", unsafe_allow_html=True) 