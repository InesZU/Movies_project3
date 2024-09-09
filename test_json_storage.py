from movie_app import MovieApp
from storage_json import StorageJson


def test_json_storage():
    # Create an instance of StorageJson
    storage = StorageJson('movies.json')

    # Create an instance of MovieApp with the StorageJson object
    movie_app = MovieApp(storage)

    # Run the movie application
    movie_app.run()


if __name__ == "__main__":
    test_json_storage()
