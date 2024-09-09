from storage_json import StorageJson
from storage_csv import StorageCsv
from movie_app import MovieApp


def main():
    print("Choose storage method:")
    print("1. JSON")
    print("2. CSV")

    choice = input("Enter choice (1 or 2): ").strip()

    # Create a storage object based on user's choice
    if choice == '1':
        storage = StorageJson('movies.json')
    elif choice == '2':
        storage = StorageCsv('movies.csv')
    else:
        print("Invalid choice. Defaulting to JSON storage.")
        storage = StorageJson('movies.json')

    # Create a MovieApp object with the selected storage object
    movie_app = MovieApp(storage)

    # Run the movie application
    movie_app.run()


if __name__ == "__main__":
    main()
