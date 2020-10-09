MENU_PROMPT = "/nEnter 'a' to add a movie, 's' to see your movie, 'f' to find a movie by title, or 'q' to quit "

movies = []


# function to add movie
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter thr movie release year: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })


# function to show movie
def show_movie():
    for movie in movies:
        print_movie(movie)


# function to print movie result
def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


# function to find movie
def find_movie():
    search_title = input("Enter your movie search title: ")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)


# dictionary to store user inputs for functions...
user_options = {
    "a": add_movie,
    "s": show_movie,
    "f": find_movie
}


# function for the app menu
def app_menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]  # first class function to control menu
            selected_function()
        else:
            print('unknown command. Please try again.')

        selection = input(MENU_PROMPT)


app_menu()

