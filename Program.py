# creating main lists to hold data in a parallel format
titles = []
authors = []
genres = []

#A function to add books accepting title, author and genre as parameters
def add_book(title,author,genre):
    global titles
    global authors
    global genres
    titles.append(title)
    authors.append(author)
    genres.append(genre)

#A function to search a specific book based on it's genre, this functions returns a list
def search_book_by_genre():
    global titles
    searched_books = []
    req_genre = input("Enter the genre of which books are required: ").strip().lower()
    for i in range(len(titles)):
        if genres[i].lower() == req_genre:
            searched_books.append(titles[i])
    return searched_books

#A function to remove a book by taking a keyword and removing items having that keyword from the lists along with from authors and genres list 
def remove_book(title_keyword):
    global titles, authors, genres
    # creating new lists for updated data 
    new_titles = []
    new_authors = []
    new_genres = []
    # looping over the whole lists
    for i in range(len(titles)):
        if title_keyword.lower() not in titles[i].lower():
            new_titles.append(titles[i])
            new_authors.append(authors[i])
            new_genres.append(genres[i])
    # replacing old lists with new lists having updated data
    titles = new_titles
    authors = new_authors
    genres = new_genres

# main entry point of the program
print("Welcome to Books Management System")
choice = 0
while choice != 4:
    # displaying a menu
    print("1. Add a book")
    print("2. Search a book")
    print("3. Remove a book")
    print("4. Exit")
    # taking user's choice
    choice = int(input("Enter your choice: "))
    # proceeding for choice = 1
    if choice == 1:
        title = input("Enter the title of the book: ")
        author = input("Enter the name of the author: ")
        genre = input("Enter the genre of the book: ")
        add_book(title, author, genre )
    # proceeding for choice = 1
    elif choice == 2:
        searched_books = search_book_by_genre()
        for i in range(len(searched_books)):
            print("-",searched_books[i])
        print()
    # proceeding for choice = 1
    elif choice == 3:
        keyword = input("Enter the keyword to remove the books having that word: ")
        remove_book(keyword)
    # proceeding for choice = 1
    elif choice == 4:
        break
