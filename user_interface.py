from typing import List, Dict
from search_engine import search_movies_by_keyword, search_movies_by_genre_and_year
from search_history import save_search_to_mongo, get_popular_searches

def main_menu() -> None:
    while True:
        print("\nSelect an action:")
        print("1. Search for movies by keyword")
        print("2. Search for movies by genre and year")
        print("3. Show the most popular search queries")
        print("4. Exit")

        choice: str = input("Enter the number: ").strip()

        if choice == "1":
            search_by_keyword()
        elif choice == "2":
            search_by_genre_and_year()
        elif choice == "3":
            show_popular_searches()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid input, please try again.")

def search_by_keyword() -> None:
    keyword: str = input("Enter a keyword: ").strip()
    if not keyword:
        print("Error: The keyword cannot be empty.")
        return

    results: List[Dict] = search_movies_by_keyword(keyword)
    if results:
        save_search_to_mongo(keyword, results)

    display_results(results)

def search_by_genre_and_year() -> None:
    genre: str = input("Enter genre: ").strip()
    year_input: str = input("Enter year: ").strip()

    if not genre and not year_input:
        print("Error: Either genre or year must be provided!")
        return

    year = None
    if year_input:
        try:
            year = int(year_input)
        except ValueError:
            print("Error: The year must be a number.")
            return

    results: List[Dict] = search_movies_by_genre_and_year(genre, year)
    if results:
        search_query = f"{genre} - {year}" if year else genre
        save_search_to_mongo(search_query, results)

    display_results(results)

def show_popular_searches() -> None:
    print("\nPopular search queries:")
    popular_searches: List[Dict] = get_popular_searches()
    if not popular_searches:
        print("No popular queries found.")
    else:
        for search in popular_searches:
            print(f"{search['_id']} ({search['count']} times)")

def display_results(results: List[Dict]) -> None:
    if not results:
        print("No results found.")
        return

    print("\nFound movies:")
    for film in results:
        title: str = film.get('title', 'Unknown Movie')
        release_year: str = film.get('release_year', 'Year not specified')
        print(f"{title} ({release_year})")

if __name__ == "__main__":
    main_menu()
