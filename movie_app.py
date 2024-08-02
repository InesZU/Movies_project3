from istorage import IStorage


class MovieApp:
    """A class representing the Movie App with functionalities for managing movies."""

    def __init__(self, storage: IStorage):
        """
        Initializes the MovieApp with an IStorage object.

        Args:
            storage: An IStorage object for movie data persistence.
        """
        if not isinstance(storage, IStorage):
            raise TypeError("storage must be an IStorage object")
        self._storage=storage

    def _command_list_movies(self):
        """List all movies."""
        movies=self._storage.list_movies()
        if not movies:
            print("No movies found.")
        else:
            for title, info in movies.items():
                try:
                    year=info['year']
                    rating=info.get('rating')  # Get rating with default None if not present
                    if year and rating:
                        print(f"{title}: Year {year}, Rating {rating:.1f}")
                except KeyError:
                    print(f"{title}: (Missing information)")

    def _command_add_movie(self):
        """Add a new movie."""
        title=input("Enter movie title: ")
        year=int(input("Enter movie year: "))
        rating=float(input("Enter movie rating: "))
        self._storage.add_movie(title, year, rating)

    def _command_delete_movie(self):
        """Delete a movie."""
        title=input("Enter the movie title to delete: ")
        self._storage.delete_movie(title)

    def _command_update_movie(self):
        """Update a movie rating."""
        title=input("Enter the movie title to update: ")
        rating=float(input("Enter new rating: "))
        self._storage.update_movie(title, rating)

    def _command_movie_stats(self):
        """Calculate and display movie statistics."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies to calculate statistics.")
            return

        ratings=[info.get('rating') for info in movies.values() if info.get('rating')]
        if not ratings:
            print("No ratings available to calculate statistics.")
            return

        # Average rating
        average_rating = sum(ratings) / len(ratings)
        print(f"Average rating: {average_rating:.2f}")

        # Median rating
        sorted_ratings=sorted(ratings)
        mid=len(sorted_ratings) // 2
        median_rating=(sorted_ratings[mid] if len(sorted_ratings) % 2 == 1
                       else (sorted_ratings[mid - 1] + sorted_ratings[mid]) / 2)
        print(f"Median rating: {median_rating:.2f}")

        # Best movies
        max_rating=max(ratings)
        best_movies=[title for title, info in movies.items() if info['rating'] == max_rating]
        print(f"Best movies: {', '.join(best_movies)}")

        # Worst movies
        min_rating=min(ratings)
        worst_movies=[title for title, info in movies.items() if info['rating'] == min_rating]
        print(f"Worst movies: {', '.join(worst_movies)}")

    def _generate_website(self):
        """Generate a static website for the movies."""
        movies_list=self._storage.list_movies()
        movies_to_display=list(movies_list.items())[:20]

        # Read the template content
        with open("index_template.html", "r") as template_file:
            template_content=template_file.read()

        # Replace placeholders
        title="Welcome to GetFlix"  # Adjust the title
        movie_grid_html=""
        for title, info in movies_to_display:
            year=info['year']
            rating=info['rating']
            imdb_id=info.get('imdb_id', 'N/A')
            imdb_url=f"https://www.imdb.com/title/{imdb_id}/" if imdb_id != 'N/A' else "#"
            notes=" | ".join(info.get('notes', []))  # Join notes with a separator
            movie_grid_html+=f"""
        <li class="movie-item">
            <a href="{imdb_url}" target="_blank">
                <div class="tooltip">{notes}</div>
            </a>
            <p>{title} - Year: {year} - Rating: {rating}</p>
        </li>
        """

        replaced_content=template_content.replace("__TEMPLATE_TITLE__", title).replace(
            "__TEMPLATE_MOVIE_GRID__", movie_grid_html
        )

        # Write the complete website to index.html
        with open("index.html", "w") as website_file:
            website_file.write(replaced_content)
        print("Website generated successfully!")

    def run(self):
        """Run the movie app."""
        while True:
            print("\n********** Welcome to Getflix **********")
            print("Menu:")
            print("0. Exit")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("4. Update movie")
            print("5. Stats")
            print("6. Generate website")
            print("Enter choice (0-6): ")

            choice=input()
            try:
                choice=int(choice)
                if choice == 1:
                    self._command_list_movies()
                elif choice == 2:
                    self._command_add_movie()
                elif choice == 3:
                    self._command_delete_movie()
                elif choice == 4:
                    self._command_update_movie()
                elif choice == 5:
                    self._command_movie_stats()
                elif choice == 6:
                    self._generate_website()
                elif choice == 0:
                    print("Thanks for choosing Getflix. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
