# Beats Binder: Your Personal Music Inventory

## Project Description
Beats Binder is an app that allows you to view the latest charting artists, albums, and songs, as well as to save these information in your inventory. Upon landing on the home page, you will see a navigation bar that has the title of the application, the different inventories (artists, albums, songs), and a search bar to lookup music information. When you use the search bar, you will be redirected to a results page that displays all the results to your search. Besides each result is an option to add it to your respective inventory. On the artists inventory page, you will see all of your saved artists, and vice versa for your other inventories, and you have the option to delete entries from your inventory. The navigation bar will remain in place regardless of which page you are redirect to, so you are able to add information to your inventory anywhere, any time. 

## Project Launch Code
In order to access this project, following these directions:

#### Clone the project
1. Open up the project on GitHub 
2. Under <> Code then SSH, copy the URL
3. In your terminal, enter `git clone copied_url`
4. Open up the project in your preferred IDE

#### Set up your Python environment
1. `pyenv local 3.11.5`
2. `python -m venv env_3.11.5`
3. `source env_3.11.5/bin/activate`

#### Set up your modules
The modules you need are nodeenv, pygraphviz, pgadmin4, and django-extensions
1. You can choose to use `pip install` to install your modules individually
2. OR use the requirements_env folder: `pip-sync requirements_env/main.txt requirements_env/dev.txt`

#### Connecting to your local database
1. Move into the second `Beats_Binder` folder and create a file named `secrets.json`
2. Copy and paste the following code into the file, replacing the data with information about your own database
   
   ```
   {
    "environment": "development",
    "movie_theater_url": "http://localhost:8000",
    "database_name": "moron",
    "database_user": "huiwen",
    "database_pwd": "111111",
    "database_host": "localhost",
    "database_port": "5432"
   }
   ```

#### Running the project
1. Move into the first directory called `Beats_Binder`, which is on the same level as the file `manage.py`
2. Make sure you migrate your changes before running anything with the command `python manage.py migrate`
3. Run the command `python manage.py runserver` (or if you are a MacOS user, `python3 manage.py runserver`) in your terminal
4. Open `http://127.0.0.1:8000/` in your browser
5. Click on the button that says `Click me! :D` to populate some data into your database for testing

## API used in this project
- Deezer API: https://rapidapi.com/deezerdevs/api/deezer-1
- Billboard Charts Rankings: https://rapidapi.com/contact-cmWXEDTql/api/billboard-charts-rankings/

## Project Members
#### Hui Wen Weng
- hweng40@stuy.edu
- HuiWenWeng
- Responsible for home page and API calling

#### Zidanni Clerigo
- zclerigo40@stuy.edu
- zClerigo
- Responsible for songs inventory

#### Bushra Rahman
- brahman40@stuy.edu
- BushraRahman
- Responsible for databases and albums inventory

#### Sadat Ahmed
- sahmed40@stuy.edu
- Sadat40
- Responsible for artists inventory
