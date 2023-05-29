import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
   # Fetch the URL of the movie poster using the TMDb API
   response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
  # Finding the index of the input movie in the 'movies' data frame
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  # Sorting the movies based on similarity scores and selects the top 5 similar movies
  movies_list = sorted(list(enumerate(distances)), reverse= True, key= lambda x:x[1])[1:6]

  recommended_movie = []
  recommended_movie_posters = []
  for i in movies_list:
    movie_id = movies.iloc[i[0]].movie_id
    recommended_movie.append(movies.iloc[i[0]].title)
    recommended_movie_posters.append(fetch_poster(movie_id)) # Fetching the movie poster using the 'fetch_poster' function
  return recommended_movie, recommended_movie_posters

# Load pickled data: 'movies_dict' contains movie information and 'similarity' contains similarity scores
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# Set the title of the web application and create a select_box to allow the user to choose a movie from the list of movie titles
st.title("Movie Recommendation System")

selectMovieName = st.selectbox(
    'Write a movie name or Select from the list',
    movies['title'].values)

st.write('You selected:', selectMovieName)

if st.button('Recommend'):
    names, posters = recommend(selectMovieName)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        # Display the title and poster of the first recommended movie
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])
