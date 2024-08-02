import json
from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path=file_path
        self.movies=self._load_data()

    def _load_data(self):
        """Helper method to load data from the JSON file."""
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_data(self, data):
        """Helper method to save data to the JSON file."""
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def list_movies(self):
        """List all movies from the storage."""
        movies=self._load_data()
        return movies
        #return list(self.movies.keys())

    def add_movie(self, title, year, rating):
        """Add a new movie to the storage."""
        movies=self._load_data()
        if title in movies:
            print(f"Movie '{title}' already exists.")
            return

        movies[title]={
            "year": year,
            "rating": rating,
        }
        self._save_data(movies)
        print(f"Movie '{title}' added successfully.")

    def delete_movie(self, title):
        """Delete a movie from the storage."""
        movies=self._load_data()
        if title in movies:
            del movies[title]
            self._save_data(movies)
            print(f"Movie '{title}' deleted successfully.")
        else:
            print(f"Movie '{title}' not found in the storage.")

    def update_movie(self, title, rating):
        """Update the rating of a movie."""
        movies=self._load_data()
        if title in movies:
            movies[title]["rating"]=rating
            self._save_data(movies)
            print(f"Movie '{title}' updated successfully.")
        else:
            print(f"Movie '{title}' not found.")
