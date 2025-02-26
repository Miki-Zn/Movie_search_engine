import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import connect_mysql
from search_engine import search_movies_by_keyword, search_movies_by_genre_and_year
from search_history import get_popular_searches

def search_by_keyword():
    keyword = keyword_entry.get()
    results = search_movies_by_keyword(keyword)
    display_results(results)

def search_by_genre_and_year():
    genre = genre_entry.get()
    year = year_entry.get()
    results = search_movies_by_genre_and_year(genre, year)
    display_results(results)

def show_popular_searches():
    popular_searches = get_popular_searches()
    results_text.delete(1.0, tk.END)
    for search in popular_searches:
        results_text.insert(tk.END, f"{search['_id']} ({search['count']} times)\n")

def display_results(results):
    results_text.delete(1.0, tk.END)
    if not results:
        results_text.insert(tk.END, "Nothing found.")
        return
    for film in results:
        results_text.insert(tk.END, f"{film['title']} ({film['release_year']})\n")



mysql_conn = connect_mysql()


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
