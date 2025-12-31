titles = []
authors = []
genres = []

def add_book(title,author,genre):
    global titles
    global authors
    global genres
    titles.append(title)
    authors.append(author)
    genres.append(genre)

def search_book_by_genre():
    global titles
    searched_books = []
    req_genre = input("Enter the genre of which books are required: ").strip().lower()
    for i in range(len(titles)):
        if genres[i].lower() == req_genre:
            searched_books.append(titles[i])
    return searched_books

def remove_book(title_keyword):
    global titles, authors, genres

    new_titles = []
    new_authors = []
    new_genres = []

    for i in range(len(titles)):
        if title_keyword.lower() not in titles[i].lower():
            new_titles.append(titles[i])
            new_authors.append(authors[i])
            new_genres.append(genres[i])

    titles = new_titles
    authors = new_authors
    genres = new_genres


print("Welcome to Books Management System")
choice = 0
while choice != 4:
    print("1. Add a book")
    print("2. Search a book")
    print("3. Remove a book")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter the title of the book: ")
        author = input("Enter the name of the author: ")
        genre = input("Enter the genre of the book: ")
        add_book(title, author, genre )

    if choice == 2:
        searched_books = search_book_by_genre()
        for i in range(len(searched_books)):
            print("-",searched_books[i])
        print()

    if choice == 3:
        keyword = input("Enter the keyword to remove the books having that word: ")
        remove_book(keyword)

    if choice == 4:
        break
