from storage_json import StorageJson
from movie_app import MovieApp
from storage_csv import StorageCsv


def main():
    # Create a StorageJson object
    storage = StorageJson('movies.json')
    storage = StorageCsv ('movies.csv')

    # Create a MovieApp object with the Storage object
    movie_app = MovieApp(storage)

    # Run the application
    movie_app.run()


if __name__ == "__main__":
    main()
