from storage_json import StorageJson


def test_storage_json():
    # Create an instance of StorageJson
    storage = StorageJson('movies.json')

    # Print the current list of movies (should be empty or pre-loaded data)
    print("Current movies:", storage.list_movies())

    # Add a new movie
    storage.add_movie("Inception", 2010, 8.8, "https://example.com/inception.jpg", "tt1375666")
    print("Movies after adding Inception:", storage.list_movies())

    # Update the movie
    storage.update_movie("Inception", "Updated note")
    print("Movies after updating Inception:", storage.list_movies())

    # Delete the movie
    storage.delete_movie("Inception")
    print("Movies after deleting Inception:", storage.list_movies())


if __name__ == "__main__":
    test_storage_json()
