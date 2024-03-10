import json
import click


@click.command()
def movlst():
    """List all movies from the JSON file."""
    movies = load_movies_from_database()
    for movie in movies:
        print("Title:", movie["title"])
        print("Description", movie["description"])
        print("Year:", movie["year"])
        print("Director:", movie["director"])
        print("Genre:", movie["genre"])
        print()


def load_movies_from_database():
    """Load movies from the JSON database."""
    with open("movies.json", "r") as f:
        movies = json.load(f)
    return movies


if __name__ == "__main__":
    movlst()