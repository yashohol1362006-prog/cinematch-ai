# import streamlit as st
# import pickle
# import os
# import random 
# import streamlit as st
# import pickle
# import requests

# TMDB_ACCESS_TOKEN = st.secrets["TMDB_ACCESS_TOKEN"]
# def get_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}"

#     headers = {
#         "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}"
#     }

#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         data = response.json()
#         poster_path = data.get("poster_path")

#         if poster_path:
#             return f"https://image.tmdb.org/t/p/w500{poster_path}"

#     return None

# # ============================================================
# # PAGE CONFIG
# # ============================================================

# st.set_page_config(
#     page_title="CineMatch AI",
#     page_icon="🎬",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )


# # ============================================================
# # LOAD DATA
# # ============================================================

# @st.cache_data
# def load_data():
#     movies = pickle.load(open("movies.pkl", "rb"))
#     similarity = pickle.load(open("similarity.pkl", "rb"))
#     return movies, similarity


# movies, similarity = load_data()


# # ============================================================
# # CUSTOM CSS
# # ============================================================

# st.markdown("""
# <style>

#     /* ---------- GLOBAL ---------- */

#     .stApp {
#         background:
#             radial-gradient(circle at 15% 10%, rgba(120, 50, 255, 0.18), transparent 30%),
#             radial-gradient(circle at 85% 20%, rgba(255, 40, 100, 0.12), transparent 30%),
#             linear-gradient(135deg, #07070c 0%, #0b0b14 50%, #050509 100%);
#         color: #ffffff;
#     }

#     .block-container {
#         max-width: 1250px;
#         padding-top: 2rem;
#         padding-bottom: 4rem;
#     }

#     /* ---------- REMOVE STREAMLIT DEFAULT ---------- */

#     #MainMenu {
#         visibility: hidden;
#     }

#     footer {
#         visibility: hidden;
#     }

#     header {
#         visibility: hidden;
#     }

#     /* ---------- HERO ---------- */

#     .hero {
#         text-align: center;
#         padding: 55px 20px 35px 20px;
#     }

#     .hero-badge {
#         display: inline-block;
#         padding: 8px 18px;
#         border-radius: 30px;
#         background: rgba(255,255,255,0.07);
#         border: 1px solid rgba(255,255,255,0.12);
#         color: #b9a7ff;
#         font-size: 14px;
#         font-weight: 600;
#         margin-bottom: 20px;
#         backdrop-filter: blur(10px);
#     }

#     .hero-title {
#         font-size: 64px;
#         line-height: 1.05;
#         font-weight: 800;
#         letter-spacing: -3px;
#         margin: 0;
#         background: linear-gradient(
#             90deg,
#             #ffffff,
#             #c7b8ff,
#             #ff8ab5,
#             #ffffff
#         );
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#     }

#     .hero-subtitle {
#         color: #a7a7b5;
#         font-size: 18px;
#         max-width: 700px;
#         margin: 20px auto 0 auto;
#         line-height: 1.6;
#     }

#     /* ---------- SEARCH BOX ---------- */

#     div[data-baseweb="select"] > div {
#         background: rgba(255,255,255,0.055) !important;
#         border: 1px solid rgba(255,255,255,0.14) !important;
#         border-radius: 16px !important;
#         min-height: 55px !important;
#         backdrop-filter: blur(15px);
#     }

#     div[data-baseweb="select"] span {
#         color: white !important;
#     }

#     /* ---------- BUTTON ---------- */

#     .stButton > button {
#         width: 100%;
#         height: 55px;
#         border-radius: 16px;
#         border: 1px solid rgba(255,255,255,0.15);
#         background: linear-gradient(
#             135deg,
#             #7c3aed,
#             #db2777
#         );
#         color: white;
#         font-size: 16px;
#         font-weight: 700;
#         transition: all 0.25s ease;
#         box-shadow: 0 10px 35px rgba(124,58,237,0.25);
#     }

#     .stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 15px 45px rgba(219,39,119,0.35);
#         border-color: rgba(255,255,255,0.35);
#     }

#     /* ---------- SECTION ---------- */

#     .section-title {
#         font-size: 30px;
#         font-weight: 750;
#         margin-top: 45px;
#         margin-bottom: 5px;
#     }

#     .section-subtitle {
#         color: #858592;
#         font-size: 14px;
#         margin-bottom: 25px;
#     }

#     /* ---------- MOVIE CARD ---------- */

#     .movie-card {
#         background: rgba(255,255,255,0.045);
#         border: 1px solid rgba(255,255,255,0.09);
#         border-radius: 20px;
#         padding: 20px;
#         height: 100%;
#         min-height: 190px;
#         transition: all 0.3s ease;
#         backdrop-filter: blur(12px);
#     }

#     .movie-card:hover {
#         transform: translateY(-6px);
#         border-color: rgba(167,139,250,0.45);
#         box-shadow: 0 20px 50px rgba(0,0,0,0.35);
#         background: rgba(255,255,255,0.07);
#     }

#     .rank {
#         font-size: 13px;
#         font-weight: 700;
#         color: #a78bfa;
#         margin-bottom: 10px;
#     }

#     .movie-name {
#         font-size: 19px;
#         font-weight: 700;
#         color: #ffffff;
#         line-height: 1.3;
#         margin-bottom: 12px;
#     }

#     .similarity {
#         display: inline-block;
#         padding: 5px 10px;
#         border-radius: 20px;
#         background: rgba(34,197,94,0.12);
#         color: #86efac;
#         font-size: 12px;
#         font-weight: 700;
#     }

#     /* ---------- INFO CARDS ---------- */

#     .info-card {
#         background: rgba(255,255,255,0.04);
#         border: 1px solid rgba(255,255,255,0.08);
#         border-radius: 18px;
#         padding: 22px;
#         text-align: center;
#         backdrop-filter: blur(12px);
#     }

#     .info-number {
#         font-size: 27px;
#         font-weight: 800;
#         color: white;
#     }

#     .info-label {
#         color: #858592;
#         font-size: 13px;
#         margin-top: 5px;
#     }

#     /* ---------- FOOTER ---------- */

#     .footer {
#         text-align: center;
#         margin-top: 70px;
#         padding-top: 25px;
#         border-top: 1px solid rgba(255,255,255,0.08);
#         color: #666675;
#         font-size: 13px;
#     }

# </style>
# """, unsafe_allow_html=True)


# # ============================================================
# # HERO SECTION
# # ============================================================

# st.markdown("""
# <div class="hero">

#     <div class="hero-badge">
#         ✨ AI POWERED MOVIE DISCOVERY
#     </div>

#     <h1 class="hero-title">
#         CineMatch
#     </h1>

#     <p class="hero-subtitle">
#         Discover movies you'll love using machine learning.
#         Select a movie and let our recommendation engine
#         find films with similar stories, genres, cast and themes.
#     </p>

# </div>
# """, unsafe_allow_html=True)


# # ============================================================
# # SEARCH SECTION
# # ============================================================

# st.markdown("""
# <div class="section-title">
#     🔎 Find your next movie
# </div>

# <div class="section-subtitle">
#     Choose a movie and we'll find the closest matches.
# </div>
# """, unsafe_allow_html=True)


# movie_titles = movies["title"].values

# selected_movie = st.selectbox(
#     "Select a movie",
#     movie_titles,
#     label_visibility="collapsed"
# )


# # ============================================================
# # RECOMMENDATION FUNCTION
# # ============================================================

# def recommend(movie):

#     movie_index = movies[movies["title"] == movie].index[0]

#     distances = similarity[movie_index]

#     movie_list = sorted(
#         list(enumerate(distances)),
#         reverse=True,
#         key=lambda x: x[1]
#     )

#     recommendations = []

#     # Skip index 0 because it is usually the movie itself
#     for i in movie_list[1:6]:

#         movie_index = i[0]
#         similarity_score = i[1]

#         title = movies.iloc[movie_index]["title"]

#         recommendations.append(
#             (title, similarity_score)
#         )

#     return recommendations


# # ============================================================
# # RECOMMEND BUTTON
# # ============================================================

# if st.button("🎬 Discover Similar Movies"):

#     recommendations = recommend(selected_movie)

#     st.markdown(f"""
#     <div class="section-title">
#         🎯 Because you liked <span style="color:#a78bfa;">
#         {selected_movie}
#         </span>
#     </div>

#     <div class="section-subtitle">
#         Here are the movies our AI thinks you'll enjoy.
#     </div>
#     """, unsafe_allow_html=True)


#     # ========================================================
#     # RECOMMENDATION CARDS
#     # ========================================================

#     cols = st.columns(5)

#     for index, (title, score) in enumerate(recommendations):

#         percentage = round(score * 100, 1)

#         with cols[index]:

#             st.markdown(f"""
#             <div class="movie-card">

#                 <div class="rank">
#                     #{index + 1} RECOMMENDATION
#                 </div>

#                 <div class="movie-name">
#                     {title}
#                 </div>

#                 <div class="similarity">
#                     {percentage}% similarity
#                 </div>

#             </div>
#             """, unsafe_allow_html=True)


# # ============================================================
# # HOW IT WORKS
# # ============================================================

# st.markdown("""
# <div class="section-title">
#     🧠 How CineMatch works
# </div>

# <div class="section-subtitle">
#     Your recommendation is generated using the movie's content.
# </div>
# """, unsafe_allow_html=True)


# col1, col2, col3 = st.columns(3)


# with col1:

#     st.markdown("""
#     <div class="info-card">

#         <div style="font-size:35px;">🏷️</div>

#         <div class="info-number">
#             Movie Tags
#         </div>

#         <div class="info-label">
#             Genres, keywords, overview,
#             cast and crew are combined.
#         </div>

#     </div>
#     """, unsafe_allow_html=True)


# with col2:

#     st.markdown("""
#     <div class="info-card">

#         <div style="font-size:35px;">🔢</div>

#         <div class="info-number">
#             Vectorization
#         </div>

#         <div class="info-label">
#             Text is converted into
#             numerical vectors using NLP.
#         </div>

#     </div>
#     """, unsafe_allow_html=True)


# with col3:

#     st.markdown("""
#     <div class="info-card">

#         <div style="font-size:35px;">🎯</div>

#         <div class="info-number">
#             Similarity
#         </div>

#         <div class="info-label">
#             Cosine similarity finds
#             movies with similar content.
#         </div>

#     </div>
#     """, unsafe_allow_html=True)


# # ============================================================
# # STATS
# # ============================================================

# st.markdown("""
# <div class="section-title">
#     📊 CineMatch at a glance
# </div>
# """, unsafe_allow_html=True)


# c1, c2, c3 = st.columns(3)


# with c1:

#     st.markdown(f"""
#     <div class="info-card">

#         <div class="info-number">
#             {len(movies):,}
#         </div>

#         <div class="info-label">
#             Movies in Database
#         </div>

#     </div>
#     """, unsafe_allow_html=True)


# with c2:

#     st.markdown("""
#     <div class="info-card">

#         <div class="info-number">
#             5
#         </div>

#         <div class="info-label">
#             Recommendations Per Search
#         </div>

#     </div>
#     """, unsafe_allow_html=True)


# with c3:

#     st.markdown("""
#     <div class="info-card">

#         <div class="info-number">
#             AI
#         </div>

#         <div class="info-label">
#             Recommendation Engine
#         </div>

#     </div>
#     """, unsafe_allow_html=True)


# # ============================================================
# # FOOTER
# # ============================================================

# st.markdown("""
# <div class="footer">

#     🎬 CineMatch AI &nbsp; • &nbsp;
#     Built with Python, Pandas, Scikit-Learn & Streamlit

#     <br><br>

#     Content-based recommendation system powered by
#     cosine similarity.

# </div>
# """, unsafe_allow_html=True)


































import streamlit as st
import pickle
import requests


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CineMatch AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# TMDB API
# ============================================================

TMDB_ACCESS_TOKEN = st.secrets["TMDB_ACCESS_TOKEN"]


@st.cache_data(ttl=86400)
def get_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{int(movie_id)}"

    headers = {
        "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}",
        "accept": "application/json"
    }

    for attempt in range(3):

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            if response.status_code == 200:

                data = response.json()

                poster_path = data.get("poster_path")

                if poster_path:
                    return f"https://image.tmdb.org/t/p/w500{poster_path}"

                return None

            # Authentication problem
            if response.status_code == 401:
                return None

            # Rate limit
            if response.status_code == 429:
                return None

        except requests.exceptions.ConnectionError:
            # Temporary network problem — try again
            continue

        except requests.exceptions.Timeout:
            # TMDB took too long
            continue

        except requests.RequestException:
            return None

    return None


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    with open("movies.pkl", "rb") as file:
        movies = pickle.load(file)

    with open("similarity.pkl", "rb") as file:
        similarity = pickle.load(file)

    return movies, similarity


movies, similarity = load_data()


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(120,50,255,0.18), transparent 30%),
        radial-gradient(circle at 85% 20%, rgba(255,40,100,0.12), transparent 30%),
        linear-gradient(135deg, #07070c 0%, #0b0b14 50%, #050509 100%);
    color: white;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* HERO */

.hero {
    text-align: center;
    padding: 55px 20px 35px;
}

.hero-badge {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 30px;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    color: #b9a7ff;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 20px;
}

.hero-title {
    font-size: 64px;
    line-height: 1.05;
    font-weight: 800;
    letter-spacing: -3px;
    margin: 0;
    background: linear-gradient(
        90deg,
        #ffffff,
        #c7b8ff,
        #ff8ab5,
        #ffffff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #a7a7b5;
    font-size: 18px;
    max-width: 700px;
    margin: 20px auto 0;
    line-height: 1.6;
}


/* SECTION */

.section-title {
    font-size: 30px;
    font-weight: 750;
    margin-top: 45px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #858592;
    font-size: 14px;
    margin-bottom: 25px;
}


/* SELECT BOX */

div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.055) !important;
    border: 1px solid rgba(255,255,255,0.14) !important;
    border-radius: 16px !important;
    min-height: 55px !important;
}

div[data-baseweb="select"] span {
    color: white !important;
}


/* BUTTON */

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.15);
    background: linear-gradient(
        135deg,
        #7c3aed,
        #db2777
    );
    color: white;
    font-size: 16px;
    font-weight: 700;
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 45px rgba(219,39,119,0.35);
}


/* MOVIE INFO */

.rank {
    color: #a78bfa;
    font-size: 13px;
    font-weight: 700;
    margin-top: 12px;
    margin-bottom: 7px;
}

.movie-name {
    color: white;
    font-size: 18px;
    font-weight: 700;
    line-height: 1.3;
    min-height: 48px;
    margin-bottom: 10px;
}

.similarity {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 20px;
    background: rgba(34,197,94,0.12);
    color: #86efac;
    font-size: 12px;
    font-weight: 700;
}


/* POSTER */

.poster-placeholder {
    height: 320px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255,255,255,0.05);
    border-radius: 16px;
    color: #777;
    text-align: center;
}


/* INFO CARDS */

.info-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 22px;
    text-align: center;
}

.info-number {
    font-size: 27px;
    font-weight: 800;
    color: white;
}

.info-label {
    color: #858592;
    font-size: 13px;
    margin-top: 5px;
}


/* FOOTER */

.footer {
    text-align: center;
    margin-top: 70px;
    padding-top: 25px;
    border-top: 1px solid rgba(255,255,255,0.08);
    color: #666675;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

    <div class="hero-badge">
        ✨ AI POWERED MOVIE DISCOVERY
    </div>

    <h1 class="hero-title">
        CineMatch
    </h1>

    <p class="hero-subtitle">
        Discover movies you'll love using machine learning.
        Select a movie and let our recommendation engine
        find films with similar stories, genres, cast and themes.
    </p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SEARCH
# ============================================================

st.markdown("""
<div class="section-title">
    🔎 Find your next movie
</div>

<div class="section-subtitle">
    Choose a movie and we'll find the closest matches.
</div>
""", unsafe_allow_html=True)


movie_titles = movies["title"].values

selected_movie = st.selectbox(
    "Select a movie",
    movie_titles,
    label_visibility="collapsed"
)


# ============================================================
# RECOMMENDATION FUNCTION
# ============================================================

def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in movie_list[1:6]:

        movie_index = i[0]
        similarity_score = i[1]

        title = movies.iloc[movie_index]["title"]
        movie_id = movies.iloc[movie_index]["id"]

        poster = get_poster(movie_id)

        recommendations.append(
            (title, similarity_score, poster)
        )

    return recommendations


# ============================================================
# BUTTON
# ============================================================

if st.button("🎬 Discover Similar Movies"):

    recommendations = recommend(selected_movie)

    st.markdown(
        f"""
        <div class="section-title">
            🎯 Because you liked
            <span style="color:#a78bfa;">
                {selected_movie}
            </span>
        </div>

        <div class="section-subtitle">
            Here are the movies our AI thinks you'll enjoy.
        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # MOVIE POSTERS
    # ========================================================

    cols = st.columns(5)

    for index, (title, score, poster) in enumerate(recommendations):

        percentage = round(score * 100, 1)

        with cols[index]:

            # POSTER
            if poster:

                st.image(
                    poster,
                    use_container_width=True
                )

            else:

                st.markdown(
                    """
                    <div class="poster-placeholder">
                        🎬<br>
                        Poster unavailable
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # RANK
            st.markdown(
                f"""
                <div class="rank">
                    #{index + 1} RECOMMENDATION
                </div>
                """,
                unsafe_allow_html=True
            )


            # TITLE
            st.markdown(
                f"""
                <div class="movie-name">
                    {title}
                </div>
                """,
                unsafe_allow_html=True
            )


            # SIMILARITY
            st.markdown(
                f"""
                <div class="similarity">
                    {percentage}% similarity
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# HOW IT WORKS
# ============================================================

st.markdown(
    """
    <div class="section-title">
        🧠 How CineMatch works
    </div>

    <div class="section-subtitle">
        Your recommendation is generated using the movie's content.
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("### 🏷️ Movie Tags")

    st.write(
        "Genres, keywords, overview, cast and crew "
        "are combined into one movie profile."
    )


with col2:

    st.markdown("### 🔢 Vectorization")

    st.write(
        "The movie text is converted into numerical "
        "vectors using NLP."
    )


with col3:

    st.markdown("### 🎯 Similarity")

    st.write(
        "Cosine similarity compares movies and finds "
        "the ones with the most similar content."
    )


# ============================================================
# CINE MATCH AT A GLANCE
# ============================================================

st.markdown("## 📊 CineMatch at a glance")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("### 🎬")
        st.metric(
            label="Movies in Database",
            value="4,803"
        )

with col2:
    with st.container(border=True):
        st.markdown("### 🎯")
        st.metric(
            label="Recommendations Per Search",
            value="5"
        )

with col3:
    with st.container(border=True):
        st.markdown("### 🤖")
        st.metric(
            label="Recommendation Engine",
            value="AI"
        )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; padding:25px 10px;">

        <h4>🎬 CineMatch AI</h4>

        <p>
            Built with Python, Pandas, Scikit-learn & Streamlit
        </p>

        <p>
            Content-based recommendation system powered by
            cosine similarity.
        </p>

        <p style="font-size:13px;">
            This product uses the TMDB API but is not endorsed
            or certified by TMDB.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)
