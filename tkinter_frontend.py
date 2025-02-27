import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Tuple, Any
from db_connection import connect_mysql
from search_engine import search_movies_by_keyword, search_movies_by_genre_and_year
from search_history import get_popular_searches


def search_by_keyword() -> None:
    keyword: str = keyword_entry.get().strip()
    if keyword:
        results: List[Tuple[Any, ...]] = search_movies_by_keyword(keyword)
        display_results(results)
    else:
        messagebox.showwarning("Warning", "Keyword cannot be empty!")


def search_by_genre_and_year() -> None:
    genre: str = genre_entry.get().strip()
    year_input: str = year_entry.get().strip()

    if not genre and not year_input:
        messagebox.showwarning("Warning", "Either genre or year must be provided!")
        return

    results: List[Tuple[Any, ...]] = []

    if genre:
        try:
            year: int = int(year_input) if year_input else None
            results = search_movies_by_genre_and_year(genre, year)
        except ValueError:
            messagebox.showerror("Invalid input", "Year must be a number.")
            return

    display_results(results)


def show_popular_searches() -> None:
    popular_searches: List[Tuple[Any, ...]] = get_popular_searches()
    results_text.delete(1.0, tk.END)

    if not popular_searches:
        results_text.insert(tk.END, "No popular searches found.")
        return

    for search in popular_searches:
        results_text.insert(tk.END, f"{search[0]} ({search[1]} times)\n")


def display_results(results: List[Any]) -> None:
    results_text.delete(1.0, tk.END)

    if not results:
        results_text.insert(tk.END, "Nothing found.")
        return

    for film in results:
        if isinstance(film, dict):
            title = film.get("title", "Unknown Title")
            release_year = film.get("release_year", "Year not specified")
        elif isinstance(film, (list, tuple)) and len(film) >= 3:
            title = str(film[1]) if film[1] else "Unknown Title"
            release_year = str(film[2]) if film[2] else "Year not specified"
        else:
            results_text.insert(tk.END, "Invalid data format.\n")
            continue

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
