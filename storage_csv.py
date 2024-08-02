from istorage import IStorage
import csv


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = self._load_data()

    def _load_data(self):
        """
        Loads movie data from the CSV file.

        Returns:
            A dictionary containing movie data or an empty dictionary if the file doesn't exist.
        """
        movies = {}
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row['title']] = {
                        "year": int(row['year']),
                        "rating": float(row['rating']),
                    }
        except (FileNotFoundError, csv.Error):
            # Handle file not found or invalid CSV data
            pass
        return movies

    def _save_data(self):
        """
        Saves movie data to the CSV file.
        """
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = ["title", "year", "rating"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, movie_data in self.movies.items():
                writer.writerow({**movie_data, "title": title})

    def list_movies(self):
        """
        Returns a dictionary of movie details.

        Returns:
            A dictionary containing movie information with title as the key.
        """
        return self.movies.copy()

    def add_movie(self, title, year, rating):
        """
        Adds a new movie to the storage.

        Args:
            title: The title of the movie.
            year: The release year of the movie.
            rating: The rating of the movie.
        """
        if title not in self.movies:
            self.movies[title] = {
                "year": year,
                "rating": rating,
            }
            self._save_data()
            print(f"Movie '{title}' added successfully.")
        else:
            print(f"Movie '{title}' already exists.")

    def delete_movie(self, title):
        """
        Deletes a movie from the storage.

        Args:
            title: The title of the movie to delete.
        """
        if title in self.movies:
            del self.movies[title]
            self._save_data()
            print(f"Movie '{title}' deleted successfully.")
        else:
            print(f"Movie '{title}' not found.")

    def update_movie(self, title, rating):
        """
        Updates the rating of a movie.

        Args:
            title: The title of the movie to update.
            rating: The new rating of the movie.
        """
        if title in self.movies:
            self.movies[title]["rating"] = rating
            self._save_data()
            print(f"Rating for '{title}' updated successfully.")
        else:
            print(f"Movie '{title}' not found.")
