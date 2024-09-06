# Movie Recommendation System

This is a simple movie recommendation system that suggests similar movies based on cosine similarity. You can select a movie, and the system will recommend up to 5 similar movies, along with their posters.

### Features:
- **Movie Recommendations**: Recommends up to 5 similar movies based on cosine similarity.
- **Movie Posters**: Fetches and displays posters for recommended movies using The Movie Database (TMDB) API.
- **Deployed Version**: Try out the live app here: [Movie Recommendation System](https://myrecommendersystem.streamlit.app)

### Tools and Libraries:
- **Pandas**: For handling the movie data (titles and tags).
- **Numpy**: For efficient array computations.
- **Scikit-learn**: Cosine similarity is used to find movies similar to the selected one.
- **Pickle**: To load the pre-trained similarity model and dataset.
- **Streamlit**: Provides the user interface for interacting with the app.
- **TMDB API**: Used to retrieve movie posters.

### How It Works:
1. **Cosine Similarity**: The system uses cosine similarity to compute the closeness between movies based on their tags. This gives you movies that are thematically close to the one you select.
2. **Recommendations**: Based on the selected movie, the system suggests the top 5 similar movies.
3. **Posters**: For each recommended movie, the system fetches the poster from the TMDB API and displays it.

### How to Run Locally:
1. Clone this repository:
   ```bash
   git clone https://github.com/MuhammadArslan007/recommender_system.git
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app with Streamlit:
   ```bash
   streamlit run app.py
   ```
4. Open the app in your browser at `http://localhost:8501`.

### Deployed Version:
You can access the live version of this project here: [Movie Recommendation System](https://myrecommendersystem.streamlit.app)



