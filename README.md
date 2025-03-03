Movie Search Engine
---------------------------------------------------------------------------
About the Project  
Movie Search Engine is a small yet handy Python application for searching movies in the Sakila database. It works in both console mode and a graphical interface using Tkinter. You can search for movies by keywords, genres, or release year. The app also saves search queries and shows the most popular ones.  

Key Features  

- Search for movies by title, genre, or year
- Display the most popular search queries  
- Save search history in MongoDB  
- User-friendly graphical interface with Tkinter  
---------------------------------------------------------------------------
Installation & Setup  
1. Clone the repository:  
sh
git clone https://github.com/your_username/movie-search-engine.git
cd movie-search-engine
---------------------------------------------------------------------------
Install dependencies:
pip install -r requirements.txt
---------------------------------------------------------------------------
3. Configure database access (create a .env file and add the following parameters):

MYSQL_HOST=MYSQL_HOST

MYSQL_USER=MYSQL_USER

MYSQL_PASSWORD=MYSQL_PASSWORD

MYSQL_DATABASE=MYSQL_DATABASE

MONGO_URL=MONGO_URL

MONGO_DATABASE=MONGO_DATABASE

MONGO_COLLECTION=MONGO_COLLECTION

---------------------------------------------------------------------------

Run the Application:

Console version:
python main.py

Graphical interface:
python tkinter_frontend.py

---------------------------------------------------------------------------
Project Structure

Movie_Search_Engine/

│-- .gitignore              # Git ignore file

│-- db_connection.py        # MySQL database connection

│-- main.py                 # Main entry point for the console version

│-- requirements.txt        # List of dependencies

│-- search_engine.py        # Core movie search logic

│-- search_history.py       # Search history storage in MongoDB

│-- tkinter_frontend.py     # Graphical interface with Tkinter

│-- user_interface.py       # Console interface logic








