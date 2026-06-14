# 🎬 Movie Recommender System

A content-based movie recommendation system built using Python, Streamlit, NLTK, and Scikit-Learn. The application recommends movies similar to a selected movie by analyzing movie metadata and calculating similarity between movies.

## Overview

This project uses movie data from the TMDB dataset. Various movie attributes such as genres, keywords, cast, crew, and overview are combined to create a feature representation for each movie. Natural Language Processing (NLP) techniques are then applied to generate meaningful recommendations.

## Features

* Content-based movie recommendations
* Interactive Streamlit web interface
* NLP-based feature engineering
* Fast similarity search using cosine similarity
* Recommendations based on movie content rather than ratings

## Dataset

The project uses the TMDB 5000 Movies Dataset.

### Attributes Used

* Movie ID
* Title
* Overview
* Genres
* Keywords
* Cast(top 3)
* Crew (Director)

These features are processed and combined into a single text representation for each movie.

## Methodology

1. Data Cleaning and Preprocessing
2. Feature Extraction from:

   * Genres
   * Keywords
   * Cast
   * Crew
   * Overview
3. Text Processing using NLTK

   * Tokenization
   * Stemming
4. Vectorization using CountVectorizer
5. Similarity Computation using Cosine Similarity
6. Recommendation Generation

## Tech Stack

* Python
* Pandas
* NumPy
* NLTK
* Scikit-Learn
* Streamlit

## Project Structure

```text
movie-recommender/
│
├── app.py
├── movies_dict.pkl
├── requirements.txt
├── README.md
└── dataset/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Abhilash9391/movie-recommender.git
cd movie-recommender
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Future Improvements

* Display movie posters using TMDB API
* Hybrid recommendation system
* Genre-based recommendations
* User accounts and personalized suggestions
* Model optimization for larger datasets

## Author

**J Abhilash Reddy**

**20/05/2026**
