import csv
from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        """
        Initializes the StorageCsv with the specified file path.
        Args:
            file_path (str): Path to the CSV file to store movie data.
        """
        self.file_path = file_path
        self.movie_list = self.read_storage()  # Load the movie data upon initialization

    def read_storage(self):
        """
        Reads data from the CSV storage file and returns a dictionary of movies.
        """
        movie_list = {}
        try:
            with open(self.file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Check if all required columns are present
                    if 'title' in row and 'rating' in row and 'year' in row:
                        movie_list[row['title']] = {
                            'year': int(row.get('year', 0)),  # Handle missing year
                            'rating': float(row.get('rating', 0)),  # Handle missing rating
                            'poster': row.get('poster', 'N/A'),
                            'imdb_id': row.get('imdb_id', 'N/A')
                        }
                    else:
                        print(f"Missing expected fields in row: {row}")
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found. Creating a new CSV file.")
        except KeyError as e:
            print(f"Error: Missing expected field {e} in the CSV file.")
        return movie_list

    def write_storage(self):
        """
        Writes the current movie list to the CSV storage file.
        """
        try:
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['title', 'year', 'rating', 'poster', 'imdb_id'])
                writer.writeheader()
                for title, details in self.movie_list.items():
                    writer.writerow({
                        'title': title,
                        'year': details.get('year', 0),
                        'rating': details.get('rating', 0),
                        'poster': details.get('poster', 'N/A'),
                        'imdb_id': details.get('imdb_id', 'N/A')
                    })
        except IOError as e:
            print(f"Error writing to CSV file: {e}")

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
            'year': year,
            'rating': round(rating, 1),
            'poster': poster,
            'imdb_id': imdb_id
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
        Updates a movie's information in the movie list by adding a note, then saves it to the CSV file.
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
