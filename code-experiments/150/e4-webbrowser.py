import webbrowser

URL = "https://google.com/search?q="
search_term = input("Enter a search term: ").replace(" ", "+")
webbrowser.open(URL + search_term)

