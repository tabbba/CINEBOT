import os
import openai
import streamlit as st  
import requests
from collections import defaultdict
import plotly.express as px
from openai import OpenAIError
from dotenv import load_dotenv
from database import submit_survey


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
API_KEY = os.getenv('TMD_API_KEY')
BASE_URL = "https://api.themoviedb.org/3"

def chat_with_gpt4(user_input):
    messages = [
        {"role": "system", "content": "Instructions"},
        {"role": "user", "content": user_input},
    ]
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.3,
            max_tokens=1000  
        )
        response_message = response.choices[0].message.content
        return response_message
    except OpenAIError as e: 
        st.error(f"An error occurred: {e}")
        return "I'm sorry, but I can't process your request right now."
    
    
def get_popular_movies():
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    data = response.json()
    return data['results']

popular_movies = get_popular_movies()
for movie in popular_movies:
    print(movie['title'], movie['release_date'])


def display_popular_movies():
    popular_movies = get_popular_movies()
    st.markdown("## 🎥 Popular Movies")
    
    cols = st.columns(5)  # Adjust the number of columns based on your preference
    for index, movie in enumerate(popular_movies[:10]):  # Display top 10 popular movies
        with cols[index % 5]:
            poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
            st.image(poster_url, caption=movie['title'], width=150)
            
            
def get_movie_genres():
    """Fetch movie genre names from TMDb."""
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    genres = response.json().get('genres', [])
    return {genre['id']: genre['name'] for genre in genres}

def analyze_movie_genres(popular_movies):
    """Analyze the genres of popular movies and return a count of each genre."""
    genre_counts = defaultdict(int)
    movie_genres = get_movie_genres()  # Fetch the mapping of genre IDs to names
    
    for movie in popular_movies:
        for genre_id in movie['genre_ids']:
            genre_name = movie_genres.get(genre_id, "Unknown")
            genre_counts[genre_name] += 1
    return genre_counts


def plot_genre_distribution(genre_counts):
    """Plot the distribution of genres."""
    genres = list(genre_counts.keys())
    counts = list(genre_counts.values())
    
    fig = px.bar(x=genres, y=counts, title="Genre Distribution Among Popular Movies", labels={'x': 'Genre', 'y': 'Number of Movies'}, color=genres)
    return fig

def display_popular_movies_and_genres():
    popular_movies = get_popular_movies()
    genre_counts = analyze_movie_genres(popular_movies)
        
    # Now, display the genre distribution plot
    genre_distribution_fig = plot_genre_distribution(genre_counts)
    st.plotly_chart(genre_distribution_fig)

# Make sure to call this function in your Streamlit app where appropriate

def display_welcome_message():
    st.markdown("# Welcome to the Cinebot Forum! 🎥")
    st.markdown("""
Welcome to this unique forum where you can ask anything about cinema and receive tailored recommendations based on your favorite movies.

Explore the world of films through conversation, or jump into our survey to get personalized movie suggestions. Dive in and let the magic of cinema captivate you! ✨
    """)
    # Call the function to display popular movies
    display_popular_movies()
    display_popular_movies_and_genres()


def display_cinebot_page():
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    st.markdown("## 🎬 Chat with Cinebot")
    
    with st.form("query_form", clear_on_submit=True):
        user_input = st.text_input("Ask me anything about movies:", key="user_query")
        submit_button = st.form_submit_button(label="Submit")
        
    if submit_button:
        response = chat_with_gpt4(user_input)
        st.session_state["chat_history"].append((user_input, response))
        st.markdown("### Here's what I found:")
        st.write(response)

def display_movie_recommendation_page():
    st.markdown("## Movie Recommendation Survey 🍿")
    
    with st.form("movie_ratings_form"):
        st.write("Please rate the following movies:")
        user_name = st.text_input("Enter your name:", key="user_name")
        
        movie_ratings = {}
        for i in range(1, 11):
            movie_name = st.text_input(f"Movie {i} name:", key=f"movie_{i}_name")
            movie_rating = st.slider("Rate this movie:", 1, 10, key=f"movie_{i}_rating")
            movie_ratings[movie_name] = movie_rating
        
        submit_ratings = st.form_submit_button("Submit Ratings")
        if submit_ratings and user_name:
            submit_survey(user_name, movie_ratings)  
            st.success("Thank you for your submission!")

def main():
    # Inject custom CSS for purple submit buttons
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #800080;
        color: white;
    }
    div.stButton > button:hover {
        background-color: #5D005D;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("Navigation 🚀")
    page = st.sidebar.radio("Go to", ["Home 🏠", "Chat with Cinebot 🎬", "Movie Recommendation Survey 🍿"], index=0)

    if page == "Home 🏠":
        display_welcome_message()
    elif page == "Chat with Cinebot 🎬":
        display_cinebot_page()
    elif page == "Movie Recommendation Survey 🍿":
        display_movie_recommendation_page()

if __name__ == "__main__":
    main()