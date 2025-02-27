from typing import List, Dict
from search_engine import search_movies_by_keyword, search_movies_by_genre_and_year
from search_history import save_search_query, get_popular_searches


def main_menu() -> None:
    while True:
        print("\nSelect an action:")
        print("1. Search for movies by keyword")
        print("2. Search for movies by genre and year")
        print("3. Show the most popular search queries")
        print("4. Exit")

        choice: str = input("Enter the number: ").strip()

        if choice == "1":
            keyword: str = input("Enter a keyword: ").strip()
            if not keyword:
                print("Error: The keyword cannot be empty.")
                continue
            results: List[Dict] = search_movies_by_keyword(keyword)
            if results:
                save_search_query(keyword, "keyword")
            display_results(results)
        elif choice == "2":
            genre: str = input("Enter genre: ").strip()
            year_input: str = input("Enter year: ").strip()
            try:
                year: int = int(year_input)
            except ValueError:
                print("Error: The year must be a number.")
                continue
            results: List[Dict] = search_movies_by_genre_and_year(genre, year)
            if results:
                save_search_query(f"{genre} - {year}", "genre_year")
            display_results(results)
        elif choice == "3":
            print("\nPopular search queries:")
            popular_searches: List[Dict] = get_popular_searches()
            if not popular_searches:
                print("No popular queries found.")
            else:
                for search in popular_searches:
                    print(f"{search['_id']} ({search['count']} times)")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid input, please try again.")

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
