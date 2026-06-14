import pickle
import streamlit as st
import pandas as pd




def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []

    for i in distances[1:6]:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


st.header('Movie Recommender System')
movies = pickle.load(open('movies_dict.pkl','rb'))

movies = pd.DataFrame(movies)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values,
)

if st.button('Show Recommendation'):
    recommendations = recommend(selected_movie)
    for recommendation in recommendations:
        st.write(recommendation)






