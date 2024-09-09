import json
from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        """
        Initializes the StorageJson with the specified file path.
        Args:
            file_path (str): Path to the JSON file to store movie data.
        """
        self.file_path = file_path
        self.movie_list = self.read_storage()  # Load the movie data upon initialization

    def read_storage(self):
        """
        Read data from the JSON storage file and return the movie list.
        Returns:
            dict: Dictionary of movies.
        """
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}  # Return an empty dictionary if the file doesn't exist or is corrupted

    def write_storage(self):
        """
        Write the current movie list to the JSON storage file.
        """
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.movie_list, file, indent=4)
        except IOError as e:
            print(f"Error writing to JSON file: {e}")

    def list_movies(self):
        """
        List all movies from the storage.
        Returns:
            dict: Dictionary of movies.
        """
        return self.movie_list

    def add_movie(self, title, year, rating, poster, imdb_id):
        """
        Add a new movie to the storage.
        Args:
            title (str): Movie title.
            year (int): Movie release year.
            rating (float): Movie rating.
            poster (str): URL of the movie poster.
            imdb_id (str): IMDb ID of the movie.
        """
        if title in self.movie_list:
            print(f"Movie '{title}' already exists!")
            return

        self.movie_list[title] = {
            "year": year,
            "rating": round(rating, 1),
            "poster": poster,
            "imdb_id": imdb_id
        }
        self.write_storage()

    def delete_movie(self, title):
        """
        Delete a movie from the storage.
        Args:
            title (str): Movie title to delete.
        """
        if title in self.movie_list:
            del self.movie_list[title]
            self.write_storage()
            print(f"Movie '{title}' deleted successfully.")
        else:
            print(f"Movie '{title}' not found.")

    def update_movie(self, title, note):
        """
        Updates a movie's information in the movie list by adding a note, then saves it to the JSON file.
        Args:
            title (str): Movie title to update.
            note (str): The note to add to the movie.
        """
        if title in self.movie_list:
            if 'notes' not in self.movie_list[title]:
                self.movie_list[title]['notes'] = []
            self.movie_list[title]['notes'].append(note)
            self.write_storage()
            print(f"Note added to '{title}' successfully.")
        else:
            print(f"Movie '{title}' not found.")
