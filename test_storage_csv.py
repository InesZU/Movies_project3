from storage_csv import StorageCsv


def test_storage_csv():
    # Create an instance of StorageCsv
    storage = StorageCsv('movies.csv')

    # Print the current list of movies (should be empty or pre-loaded data)
    print("Current movies:", storage.list_movies())

    # Add a new movie
    storage.add_movie("The Matrix", 1999, 8.7, "https://example.com/matrix.jpg", "tt0133093")
    print("Movies after adding The Matrix:", storage.list_movies())

    # Update the movie
    storage.update_movie("The Matrix", "Updated note")
    print("Movies after updating The Matrix:", storage.list_movies())

    # Delete the movie
    storage.delete_movie("The Matrix")
    print("Movies after deleting The Matrix:", storage.list_movies())


if __name__ == "__main__":
    test_storage_csv()
