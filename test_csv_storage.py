from movie_app import MovieApp
from storage_csv import StorageCsv


def test_csv_storage():
    # Create an instance of StorageCsv
    storage = StorageCsv('movies.csv')

    # Create an instance of MovieApp with the StorageCsv object
    movie_app = MovieApp(storage)

    # Run the movie application
    movie_app.run()


if __name__ == "__main__":
    test_csv_storage()
