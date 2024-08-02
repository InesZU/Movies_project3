from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self) -> dict:
        pass

    @abstractmethod
    def add_movie(self, title, year, rating):
        """

        :rtype: object
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        pass
