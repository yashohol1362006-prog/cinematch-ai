# 🎬 CineMatch — AI Movie Recommendation System

CineMatch is a content-based movie recommendation system that recommends movies similar to a movie selected by the user.

The system analyzes movie information such as genres, keywords, overview, cast, and crew, converts this information into numerical vectors using NLP techniques, and uses cosine similarity to find the most similar movies.

The project is built using Python, Pandas, Scikit-learn, NLTK, Streamlit, and the TMDB API.

---

## 🚀 Live Demo

🔗 Coming Soon
 
---

## ✨ Features

- 🎬 Search and select movies
- 🤖 Content-based movie recommendations
- 🎯 Top 5 similar movie recommendations
- 📊 Similarity percentage for each recommendation
- 🖼️ Real movie posters using the TMDB API
- 🧠 NLP-based text processing
- 📐 Cosine similarity recommendation engine
- ⚡ Interactive Streamlit web application
- 📱 Clean and responsive user interface

---

## 🧠 How CineMatch Works

CineMatch uses a content-based filtering approach.

### 1. Data Processing

Movie information is collected from the TMDB 5000 Movies and Credits datasets.

The following features are used:

- Genres
- Keywords
- Movie overview
- Cast
- Crew

These features are combined into a single `tags` column to create a representation of each movie.

### 2. Text Preprocessing

The movie tags are processed using Natural Language Processing techniques.

The project uses the **Porter Stemmer** from NLTK to reduce words to their root form.

### 3. Vectorization

The processed movie tags are converted into numerical vectors using **CountVectorizer** from Scikit-learn.

This allows the system to represent movies mathematically.

### 4. Similarity Calculation

CineMatch uses **Cosine Similarity** to calculate how similar movies are to each other.

A higher similarity score means that two movies have more similar content.

### 5. Recommendation

When a user selects a movie, CineMatch:

```text
Selected Movie
      ↓
Find Movie Vector
      ↓
Compare With Other Movies
      ↓
Calculate Cosine Similarity
      ↓
Sort Similarity Scores
      ↓
Select Top 5 Movies
      ↓
Display Recommendations
