import pandas as pd
import numpy as np
import sklearn 
import pickle
import streamlit as st
import requests


with open('tags_df.pkl', 'rb') as data:
    df_dict = pickle.load(data)
tags_df = pd.DataFrame(df_dict)

with open('model.pkl', 'rb') as model:
    similartiy = pickle.load(model)

movies_title = tags_df.iloc[:,1]


def fetch_poster(movie_id):
    data = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=9c6f76b357e18f401a1969abd7b4f7b2').json()
    incomplet_path = data['poster_path']
    complete_path = f'http://image.tmdb.org/t/p/w500{incomplet_path}'
    return complete_path 
def recommend(movie):
    recommend_movies_ids = []
    recommended_movies_names = []
    movies_index = int(np.where(tags_df['title'] == movie)[0][0])
    distances = similartiy[movies_index]
    similar_movies = sorted(list(enumerate(distances)), key=lambda x:x[1], reverse=True)[1:6]
    for i in similar_movies:
         recommended_movies_names.append(tags_df.iloc[i[0],1])
         recommend_movies_ids.append(tags_df.iloc[i[0],0])
    return recommend_movies_ids, recommended_movies_names


st.title("Wellcome to the Movies Show")

selected_movie = st.selectbox("See Movie", movies_title)
recommend_movies_ids, recommend_movies_names = recommend(selected_movie)

if st.button('Recommend'):
    # Create columns for each card
    cols = st.columns(5)

    # Loop through each movie and display them in respective columns
    for i, movie in enumerate(recommend_movies_names):
        with cols[i]:
            # Display the movie poster
            st.image(fetch_poster(recommend_movies_ids[i]), caption= movie, use_column_width=True)



      
