from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """
        List all movies from the storage.
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster, imdb_id):
        """
        Add a new movie to the storage.
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Delete a movie from the storage.
        """
        pass

    @abstractmethod
    def update_movie(self, title, note):
        """
        Update a movie by adding a note.
        """
        pass

    @abstractmethod
    def read_storage(self):
        """
        Read data from the storage.
        """
        pass

    @abstractmethod
    def write_storage(self):
        """
        Write data to the storage.
        """
        pass
