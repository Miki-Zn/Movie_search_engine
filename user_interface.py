from search_engine import search_movies_by_keyword, search_movies_by_genre_and_year
from search_history import save_search_query, get_popular_searches


def main_menu():
    while True:
        print("\nSelect an action:")
        print("1. Search for movies by keyword")
        print("2. Search for movies by genre and year")
        print("3. Show the most popular search queries")
        print("4. Exit")

        choice = input("Enter the number: ")

        if choice == "1":
            keyword = input("Enter a keyword: ")
            results = search_movies_by_keyword(keyword)
            save_search_query(keyword, "keyword")
            display_results(results)

        elif choice == "2":
            genre = input("Enter genre: ")
            year = input("Enter year: ")
            results = search_movies_by_genre_and_year(genre, year)
            save_search_query(f"{genre} - {year}", "genre_year")
            display_results(results)

        elif choice == "3":
            print("\nPopular search queries:")
            for search in get_popular_searches():
                print(f"{search['_id']} ({search['count']} times)")

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid input, please try again.")


def display_results(results):
    if not results:
        print("Nothing found.")
        return

    print("\nFound movies:")
    for film in results:
        print(f"{film['title']} ({film['release_year']})")
