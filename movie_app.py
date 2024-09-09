import statistics
import random
import requests

API_KEY = "5b29f372"
API_URL = "http://www.omdbapi.com/"


def fetch_movie_details(title):
    """
    Fetch movie details from the OMDb API if not found in the local storage.
    This function is primarily used as a backup when a movie is not found in the storage.

    Parameters:
        title (str): The title of the movie to fetch.
        api_key (str): The API key used to access the OMDb API.

    Returns:
        dict or None: A dictionary containing movie details if the movie is found,
                    otherwise None if the movie is not found or if there's an error.
    """
    url = f"{API_URL}?apikey={API_KEY}&t={title}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        if data['Response'] == 'False':
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error accessing the OMDb API: {e}")
        return None


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        """
        Command to list all movies stored.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
            return
        print(f"{len(movies)} movies in total:")
        for title, info in movies.items():
            print(f"{title}: Rating {info['rating']:.1f}")

    def _command_add_movie(self):
        """
        Command to add a new movie by fetching details from the OMDb API.
        """
        title = input("Enter movie title: ").strip()
        if title in self._storage.list_movies():
            print(f"Movie '{title}' already exists.")
            return

        movie_details = fetch_movie_details(title)
        if not movie_details:
            print(f"Movie '{title}' not found in OMDb.")
            return

        year = int(movie_details.get('Year', 0))
        rating = float(movie_details.get('imdbRating', 0))
        poster = movie_details.get('Poster', 'N/A')
        imdb_id = movie_details.get('imdbID', 'N/A')

        self._storage.add_movie(title, year, rating, poster, imdb_id)
        print(f"Movie '{title}' added successfully.")

    def _command_delete_movie(self):
        """
        Command to delete a movie from the storage.
        """
        title = input("Enter movie title to delete: ").strip()
        self._storage.delete_movie(title)

    def _command_update_movie(self):
        """
        Updates a movie's notes in local storage.
        """
        title = input("Enter the movie title to update: ").strip()
        note = input("Enter a note for the movie: ")

        # Call update_movie_in_storage to handle the update
        self._storage.update_movie(title, note)

    def _command_movie_stats(self):
        """
        Command to calculate and display statistics for stored movies.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies to calculate stats for.")
            return

        ratings = [info['rating'] for info in movies.values()]
        avg_rating = statistics.mean(ratings)
        median_rating = statistics.median(ratings)
        best_movie = max(movies, key=lambda x: movies[x]['rating'])
        worst_movie = min(movies, key=lambda x: movies[x]['rating'])

        print(f"Average rating: {avg_rating:.1f}")
        print(f"Median rating: {median_rating:.1f}")
        print(f"Best movie: {best_movie} with rating {movies[best_movie]['rating']}")
        print(f"Worst movie: {worst_movie} with rating {movies[worst_movie]['rating']}")

    def _command_random_movie(self):
        """
        Command to display a random movie from the storage.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available.")
            return

        random_movie = random.choice(list(movies.keys()))
        movie_info = movies[random_movie]
        print(f"Random movie: {random_movie} - Rating: {movie_info['rating']:.1f}")

    def _command_search_movie(self):
        """
        Command to search for movies by title in local storage.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available.")
            return

        search_term = input("Enter part of movie name: ").lower()
        found_movies = [movie for movie in movies.keys() if search_term in movie.lower()]

        if found_movies:
            for movie in found_movies:
                print(f"{movie}: Year {movies[movie]['year']}, Rating {movies[movie]['rating']:.1f}")
        else:
            print("No movies found.")

    def _command_sort_movies_by_rating(self):
        """
        Command to display movies sorted by rating.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available.")
            return

        sorted_movies = sorted(movies.items(), key=lambda x: x[1]['rating'], reverse=True)
        for title, info in sorted_movies:
            print(f"{title}: Rating {info['rating']:.1f}")

    def _generate_website(self):
        """
        Generate a static HTML website showing movies.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available to generate the website.")
            return

        # Load the template and generate the movie grid (same logic as before)
        with open("index_template.html", "r") as template_file:
            template_content = template_file.read()

        # Replace placeholders
        title = "Welcome to GetFlix"
        movie_grid_html = ""
        for title, info in list(movies.items())[:20]:  # Display first 20 movies
            poster = info.get('poster', 'N/A')
            year = info['year']
            rating = info['rating']
            imdb_id = info.get('imdb_id', 'N/A')
            imdb_url = f"https://www.imdb.com/title/{imdb_id}/" if imdb_id != 'N/A' else "#"
            notes = " | ".join(info.get('notes', []))
            movie_grid_html += f"""
<li class="movie-item">
    <a href="{imdb_url}" target="_blank">
        <img src="{poster}" alt="{title} poster" />
        <div class="tooltip">{notes}</div>
    </a>
    <p>{title} - Year: {year} - Rating: {rating:.1f}</p>
</li>
"""

        replaced_content = template_content.replace("__TEMPLATE_TITLE__", title).replace(
            "__TEMPLATE_MOVIE_GRID__", movie_grid_html
        )
        # Write the complete website to index.html
        with open("index.html", "w") as website_file:
            website_file.write(replaced_content)

        print("Website generated successfully!")

    def run(self):
        """
        Runs the main menu loop for the MovieApp.
        """
        while True:
            print("\n********** Welcome to Getflix **********")
            print("0. Exit")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("4. Update movie")
            print("5. Stats")
            print("6. Random movie")
            print("7. Search movie")
            print("8. Movies sorted by rating")
            print("9. Generate website")
            print("Enter choice (0-9): ")

            # Define the dictionary mapping choices to the corresponding command methods
            command_mapping = {
                1: self._command_list_movies,
                2: self._command_add_movie,
                3: self._command_delete_movie,
                4: self._command_update_movie,
                5: self._command_movie_stats,
                6: self._command_random_movie,
                7: self._command_search_movie,
                8: self._command_sort_movies_by_rating,
                9: self._generate_website,
            }

            # Get user command
            choice = input()

            try:
                choice = int(choice)

                # Check for exit condition
                if choice == 0:
                    print("Thanks for choosing Getflix. Goodbye!")
                    break  # This will only break the outer loop and exit the program

                # Fetch and execute the corresponding command
                command = command_mapping.get(choice)
                if command:
                    command()  # Call the function
                else:
                    print("Invalid choice. Please try again.")

            except ValueError:
                print("Invalid input. Please enter a number.")
