import streamlit as st
import pandas as pd
import pickle
import requests
import numpy as np

st.title('Welcome to Movies Recommender')
st.markdown('🍿 - Popcorn 🎥 - Movie camera 🎬 - Clapper board 🎞️ - Film frames 🎭 - Theater masks 🎦 - Cinema 🍫 - Chocolate 🎵 - Musical note  📽️ - Film projector 🔍 - Magnifying glass  👻 - Ghost')

with open('final.pkl', 'rb') as file:
    final = pickle.load(file)
    
with open('similarity_scores.pkl', 'rb') as file:
    similarity_scores = pickle.load(file)
    
movies = pd.DataFrame(final)

book_name = st.selectbox(
'Kindly select the Movie?', movies.title.values)


def recommend(movie):
    movies_list = []
    index = np.where(movies['title'] == movie)[0][0]
    similar_movies = sorted(list(enumerate(similarity_scores[index])), key = lambda x:x[1], reverse=True)[1:6]
    for i in similar_movies:
        movies_list.append(movies.iloc[i[0], 0])
        
    return movies_list

def movie_image(movie):
    endpoint = 'https://api.themoviedb.org/3/search/movie'
    api_key = '6c84fc163dfeaf4b8172205c5e07e0b1'
    query = movie

    response = requests.get(endpoint, params={'api_key': api_key, 'query': query})

    results = response.json()['results']
    movie_id = results[0]['id']

    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}'
    response = requests.get(endpoint, params={'api_key': api_key})

    poster_path = response.json()['poster_path']
    base_url = 'https://image.tmdb.org/t/p/w500'
    poster_url = base_url + poster_path
    
    return poster_url

if st.button('Recommend Movies'):
    movies_list = recommend(book_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

        
    with col1:
        st.markdown(movies_list[0])
        st.image(movie_image(movies_list[0]))
            
    with col2:
        st.markdown(movies_list[1])
        st.image(movie_image(movies_list[1]))
        
    with col3:
        st.markdown(movies_list[2])
        st.image(movie_image(movies_list[2]))
        
    with col4:
        st.markdown(movies_list[3])
        st.image(movie_image(movies_list[3]))
            
    with col5:
        st.markdown(movies_list[4])
        st.image(movie_image(movies_list[4]))     
        
st.markdown('''
----
Created with ❤️ by [Neil Kulkarni](https://www.linkedin.com/in/neilkulkarni17)
''')
