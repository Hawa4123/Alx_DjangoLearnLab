from relationship_app.models import Author, Book, Library, Librarian

# -------------------------
# Query 1: All books by a specific author
# -------------------------
def get_books_by_author(author_name):
    """
    Returns all books written by the author with the given name.
    """
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return Book.objects.none()


# -------------------------
# Query 2: All books in a library
# -------------------------
def get_books_in_library(library_name):
    """
    Returns all books in the library with the given name.
    If the library does not exist, returns an empty queryset.
    """
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return Book.objects.none()


# -------------------------
# Query 3: Retrieve the librarian for a library
# -------------------------
def get_librarian_for_library(library_name):
    """
    Returns the librarian associated with the library.
    If the library does not exist, returns None.
    """
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist, AttributeError):
        return None


# -------------------------
# Sample usage
# -------------------------
if __name__ == "__main__":
    author_name = "J.K. Rowling"
    library_name = "Central Library"

    print(f"Books by {author_name}:")
    for book in get_books_by_author(author_name):
        print(f"- {book.title}")

    print(f"\nBooks in {library_name}:")
    for book in get_books_in_library(library_name):
        print(f"- {book.title}")

    librarian = get_librarian_for_library(library_name)
    print(f"\nLibrarian of {library_name}: {librarian if librarian else 'No librarian assigned'}")


