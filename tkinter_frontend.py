import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Dict, Any
from search_engine import search_movies_by_keyword, search_movies_by_genre_and_year
from search_history import save_search_to_mongo, get_popular_searches


def search_by_keyword() -> None:
    keyword: str = keyword_entry.get().strip()
    if not keyword:
        messagebox.showwarning("Warning", "Keyword cannot be empty!")
        return

    results: List[Dict[str, Any]] = search_movies_by_keyword(keyword)

    if results:
        save_search_to_mongo(keyword, results)

    display_results(results)


def search_by_genre_and_year() -> None:
    genre: str = genre_entry.get().strip()
    year_input: str = year_entry.get().strip()

    if not genre and not year_input:
        messagebox.showwarning("Warning", "Either genre or year must be provided!")
        return

    year = None
    if year_input:
        try:
            year = int(year_input)
        except ValueError:
            messagebox.showerror("Invalid input", "Year must be a number.")
            return

    results: List[Dict[str, Any]] = search_movies_by_genre_and_year(genre, year)

    if results:
        search_query = f"{genre} - {year}" if year else genre
        save_search_to_mongo(search_query, results)

    display_results(results)


def show_popular_searches() -> None:
    popular_searches = get_popular_searches()
    results_text.delete(1.0, tk.END)

    if not popular_searches:
        results_text.insert(tk.END, "No popular searches found.")
        return

    for search in popular_searches:
        query = search.get("_id", "Unknown Query")
        count = search.get("count", 0)
        results_text.insert(tk.END, f"{query} ({count} times)\n")


def display_results(results: List[Dict[str, Any]]) -> None:
    results_text.delete(1.0, tk.END)

    if not results:
        results_text.insert(tk.END, "Nothing found.")
        return

    for film in results:
        title = film.get("title", "Unknown Title")
        release_year = film.get("release_year", "Year not specified")
        results_text.insert(tk.END, f"{title} ({release_year})\n")


root = tk.Tk()
root.title("Movie Search Engine")
root.geometry("500x400")

keyword_label = ttk.Label(root, text="Search by keyword:")
keyword_label.pack()
keyword_entry = ttk.Entry(root, width=40)
keyword_entry.pack()
search_keyword_btn = ttk.Button(root, text="Search", command=search_by_keyword)
search_keyword_btn.pack()

genre_label = ttk.Label(root, text="Genre:")
genre_label.pack()
genre_entry = ttk.Entry(root, width=20)
genre_entry.pack()

year_label = ttk.Label(root, text="Year:")
year_label.pack()
year_entry = ttk.Entry(root, width=10)
year_entry.pack()

search_genre_btn = ttk.Button(root, text="Search by genre and year", command=search_by_genre_and_year)
search_genre_btn.pack()

popular_searches_btn = ttk.Button(root, text="Popular searches", command=show_popular_searches)
popular_searches_btn.pack()

results_text = tk.Text(root, height=10, width=50)
results_text.pack()

root.mainloop()
